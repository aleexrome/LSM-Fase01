#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizador de archivos NPY generados por LSM_Processor_CSV
Permite ver frames dinámicamente y generar videos con landmarks dibujados
Autor: Script generado por Claude
Fecha: 2025
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import cv2
import numpy as np
import mediapipe as mp
from pathlib import Path
from PIL import Image, ImageTk
from typing import Dict, List, Optional, Any
import threading


class MovementStats:
    """Calcula estadísticas de movimiento a partir de landmarks."""

    @staticmethod
    def calculate_velocity(landmarks_sequence: List[np.ndarray], fps: float) -> Dict[str, float]:
        """
        Calcula velocidad promedio de movimiento de las muñecas.

        Args:
            landmarks_sequence: Secuencia de pose landmarks
            fps: Frames por segundo

        Returns:
            Diccionario con velocidades promedio
        """
        if not landmarks_sequence or len(landmarks_sequence) < 2:
            return {'left_wrist': 0.0, 'right_wrist': 0.0, 'avg': 0.0}

        left_velocities = []
        right_velocities = []

        for i in range(1, len(landmarks_sequence)):
            prev = landmarks_sequence[i-1]
            curr = landmarks_sequence[i]

            if prev is not None and curr is not None:
                # Muñeca izquierda (índice 15)
                if len(prev) > 15 and len(curr) > 15:
                    left_dist = np.sqrt(
                        (curr[15][0] - prev[15][0])**2 +
                        (curr[15][1] - prev[15][1])**2
                    )
                    left_velocities.append(left_dist * fps)

                # Muñeca derecha (índice 16)
                if len(prev) > 16 and len(curr) > 16:
                    right_dist = np.sqrt(
                        (curr[16][0] - prev[16][0])**2 +
                        (curr[16][1] - prev[16][1])**2
                    )
                    right_velocities.append(right_dist * fps)

        left_avg = np.mean(left_velocities) if left_velocities else 0.0
        right_avg = np.mean(right_velocities) if right_velocities else 0.0

        return {
            'left_wrist': left_avg,
            'right_wrist': right_avg,
            'avg': (left_avg + right_avg) / 2
        }

    @staticmethod
    def calculate_total_distance(landmarks_sequence: List[np.ndarray]) -> Dict[str, float]:
        """
        Calcula distancia total recorrida por las muñecas.

        Args:
            landmarks_sequence: Secuencia de pose landmarks

        Returns:
            Diccionario con distancias totales
        """
        if not landmarks_sequence or len(landmarks_sequence) < 2:
            return {'left_wrist': 0.0, 'right_wrist': 0.0, 'total': 0.0}

        left_total = 0.0
        right_total = 0.0

        for i in range(1, len(landmarks_sequence)):
            prev = landmarks_sequence[i-1]
            curr = landmarks_sequence[i]

            if prev is not None and curr is not None:
                # Muñeca izquierda
                if len(prev) > 15 and len(curr) > 15:
                    left_total += np.sqrt(
                        (curr[15][0] - prev[15][0])**2 +
                        (curr[15][1] - prev[15][1])**2
                    )

                # Muñeca derecha
                if len(prev) > 16 and len(curr) > 16:
                    right_total += np.sqrt(
                        (curr[16][0] - prev[16][0])**2 +
                        (curr[16][1] - prev[16][1])**2
                    )

        return {
            'left_wrist': left_total,
            'right_wrist': right_total,
            'total': left_total + right_total
        }


class LSMVisualizer:
    """Visualizador interactivo de archivos NPY con landmarks de señas."""

    def __init__(self, root: tk.Tk):
        """
        Inicializa el visualizador.

        Args:
            root: Ventana principal de tkinter
        """
        self.root = root
        self.root.title("LSM Visualizer - Visualizador de Señas")
        self.root.geometry("1200x800")

        # MediaPipe drawing utilities
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic
        self.mp_hands = mp.solutions.hands

        # Estilos de dibujo
        self.pose_style = self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)
        self.face_style = self.mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=1)
        self.hand_style = self.mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=2)

        # Datos cargados
        self.data: Optional[Dict[str, Any]] = None
        self.current_frame_idx: int = 0
        self.total_frames: int = 0
        self.video_frames: List[np.ndarray] = []
        self.npy_path: Optional[Path] = None

        # Reproducción
        self.is_playing = False
        self.play_thread: Optional[threading.Thread] = None

        # Configurar GUI
        self._setup_gui()

    def _setup_gui(self):
        """Configura la interfaz gráfica."""
        # Menú superior
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Cargar archivo .npy", command=self.load_npy_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)

        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Panel izquierdo: Canvas para video
        left_panel = ttk.Frame(main_frame)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Canvas
        self.canvas = tk.Canvas(left_panel, bg='black', width=640, height=480)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Controles de reproducción
        controls_frame = ttk.Frame(left_panel)
        controls_frame.pack(fill=tk.X, pady=10)

        self.play_button = ttk.Button(
            controls_frame,
            text="▶ Play",
            command=self.toggle_play,
            state=tk.DISABLED
        )
        self.play_button.pack(side=tk.LEFT, padx=5)

        # Slider de frames
        slider_frame = ttk.Frame(left_panel)
        slider_frame.pack(fill=tk.X, pady=5)

        ttk.Label(slider_frame, text="Frame:").pack(side=tk.LEFT, padx=5)

        self.frame_slider = ttk.Scale(
            slider_frame,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            command=self.on_slider_change
        )
        self.frame_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.frame_slider.config(state=tk.DISABLED)

        self.frame_label = ttk.Label(slider_frame, text="0 / 0")
        self.frame_label.pack(side=tk.LEFT, padx=5)

        # Panel derecho: Información y controles
        right_panel = ttk.Frame(main_frame, width=300)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        right_panel.pack_propagate(False)

        # Información del archivo
        info_frame = ttk.LabelFrame(right_panel, text="Información", padding=10)
        info_frame.pack(fill=tk.X, pady=(0, 10))

        self.info_text = tk.Text(info_frame, height=8, width=30, state=tk.DISABLED)
        self.info_text.pack(fill=tk.BOTH, expand=True)

        # Estadísticas de movimiento
        stats_frame = ttk.LabelFrame(right_panel, text="Estadísticas de Movimiento", padding=10)
        stats_frame.pack(fill=tk.X, pady=(0, 10))

        self.stats_text = tk.Text(stats_frame, height=10, width=30, state=tk.DISABLED)
        self.stats_text.pack(fill=tk.BOTH, expand=True)

        # Controles de generación de video
        video_frame = ttk.LabelFrame(right_panel, text="Generar Video", padding=10)
        video_frame.pack(fill=tk.X)

        self.generate_button = ttk.Button(
            video_frame,
            text="Generar Video con Landmarks",
            command=self.generate_video,
            state=tk.DISABLED
        )
        self.generate_button.pack(fill=tk.X)

        self.progress_label = ttk.Label(video_frame, text="")
        self.progress_label.pack(fill=tk.X, pady=(5, 0))

    def load_npy_file(self):
        """Abre diálogo para cargar archivo .npy."""
        file_path = filedialog.askopenfilename(
            title="Seleccionar archivo .npy",
            filetypes=[("NumPy files", "*.npy"), ("All files", "*.*")]
        )

        if file_path:
            try:
                self.npy_path = Path(file_path)
                self.data = np.load(str(self.npy_path), allow_pickle=True).item()

                # Cargar video correspondiente
                video_path = self.npy_path.with_suffix('.mp4')
                if video_path.exists():
                    self._load_video_frames(video_path)
                else:
                    messagebox.showwarning(
                        "Video no encontrado",
                        f"No se encontró el video correspondiente: {video_path.name}\n"
                        "Se generarán frames en blanco."
                    )
                    self._generate_blank_frames()

                self._update_info()
                self._calculate_and_display_stats()
                self._enable_controls()
                self.current_frame_idx = 0
                self.show_frame(0)

            except Exception as e:
                messagebox.showerror("Error", f"Error cargando archivo:\n{str(e)}")

    def _load_video_frames(self, video_path: Path):
        """Carga todos los frames del video en memoria."""
        self.video_frames = []
        cap = cv2.VideoCapture(str(video_path))

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            self.video_frames.append(frame)

        cap.release()
        self.total_frames = len(self.video_frames)

    def _generate_blank_frames(self):
        """Genera frames en blanco si no hay video."""
        # Usar número de frames de timestamps
        num_frames = len(self.data.get('frame_timestamps', []))
        self.video_frames = [
            np.zeros((480, 640, 3), dtype=np.uint8)
            for _ in range(num_frames)
        ]
        self.total_frames = num_frames

    def _update_info(self):
        """Actualiza el panel de información."""
        if not self.data:
            return

        info_lines = [
            f"Archivo: {self.npy_path.name}",
            f"Sign ID: {self.data.get('sign_id', 'N/A')}",
            f"Total frames: {self.total_frames}",
            f"FPS: {self.data.get('fps', 0):.1f}",
            f"Duración: {self.total_frames / self.data.get('fps', 1):.2f}s",
            f"",
            f"Landmarks disponibles:",
            f"  - Pose: {'✓' if any(self.data.get('pose_landmarks', [])) else '✗'}",
            f"  - Face: {'✓' if any(self.data.get('face_landmarks', [])) else '✗'}",
            f"  - Left hand: {'✓' if any(self.data.get('left_hand_landmarks', [])) else '✗'}",
            f"  - Right hand: {'✓' if any(self.data.get('right_hand_landmarks', [])) else '✗'}",
        ]

        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, "\n".join(info_lines))
        self.info_text.config(state=tk.DISABLED)

    def _calculate_and_display_stats(self):
        """Calcula y muestra estadísticas de movimiento."""
        if not self.data:
            return

        pose_landmarks = self.data.get('pose_landmarks', [])
        fps = self.data.get('fps', 30.0)

        # Calcular estadísticas
        velocities = MovementStats.calculate_velocity(pose_landmarks, fps)
        distances = MovementStats.calculate_total_distance(pose_landmarks)

        stats_lines = [
            "Velocidad promedio (px/s):",
            f"  Muñeca izq: {velocities['left_wrist']:.2f}",
            f"  Muñeca der: {velocities['right_wrist']:.2f}",
            f"  Promedio: {velocities['avg']:.2f}",
            "",
            "Distancia total (px):",
            f"  Muñeca izq: {distances['left_wrist']:.2f}",
            f"  Muñeca der: {distances['right_wrist']:.2f}",
            f"  Total: {distances['total']:.2f}",
            "",
            "Actividad de manos:",
            f"  {'Alta' if velocities['avg'] > 100 else 'Media' if velocities['avg'] > 50 else 'Baja'}",
        ]

        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(1.0, "\n".join(stats_lines))
        self.stats_text.config(state=tk.DISABLED)

    def _enable_controls(self):
        """Habilita controles después de cargar datos."""
        self.play_button.config(state=tk.NORMAL)
        self.frame_slider.config(state=tk.NORMAL, to=self.total_frames - 1)
        self.generate_button.config(state=tk.NORMAL)

    def draw_landmarks_on_frame(self, frame: np.ndarray, frame_idx: int) -> np.ndarray:
        """
        Dibuja landmarks sobre un frame.

        Args:
            frame: Frame original
            frame_idx: Índice del frame

        Returns:
            Frame con landmarks dibujados
        """
        if not self.data:
            return frame

        frame_copy = frame.copy()
        height, width = frame_copy.shape[:2]

        # Crear objetos de landmarks para MediaPipe
        # Pose
        pose_data = self.data.get('pose_landmarks', [])[frame_idx]
        if pose_data is not None:
            pose_landmarks = self._create_landmark_list(pose_data)
            self.mp_drawing.draw_landmarks(
                frame_copy,
                pose_landmarks,
                self.mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=self.pose_style,
                connection_drawing_spec=self.pose_style
            )

        # Face
        face_data = self.data.get('face_landmarks', [])[frame_idx]
        if face_data is not None:
            face_landmarks = self._create_landmark_list(face_data)
            self.mp_drawing.draw_landmarks(
                frame_copy,
                face_landmarks,
                self.mp_holistic.FACEMESH_TESSELATION,
                landmark_drawing_spec=self.face_style,
                connection_drawing_spec=self.face_style
            )

        # Left hand
        left_hand_data = self.data.get('left_hand_landmarks', [])[frame_idx]
        if left_hand_data is not None:
            left_hand_landmarks = self._create_landmark_list(left_hand_data)
            self.mp_drawing.draw_landmarks(
                frame_copy,
                left_hand_landmarks,
                self.mp_hands.HAND_CONNECTIONS,
                landmark_drawing_spec=self.hand_style,
                connection_drawing_spec=self.hand_style
            )

        # Right hand
        right_hand_data = self.data.get('right_hand_landmarks', [])[frame_idx]
        if right_hand_data is not None:
            right_hand_landmarks = self._create_landmark_list(right_hand_data)
            self.mp_drawing.draw_landmarks(
                frame_copy,
                right_hand_landmarks,
                self.mp_hands.HAND_CONNECTIONS,
                landmark_drawing_spec=self.hand_style,
                connection_drawing_spec=self.hand_style
            )

        return frame_copy

    def _create_landmark_list(self, landmarks_array: np.ndarray):
        """Convierte array numpy a formato de landmarks de MediaPipe."""
        from mediapipe.framework.formats import landmark_pb2

        landmark_list = landmark_pb2.NormalizedLandmarkList()

        for point in landmarks_array:
            landmark = landmark_list.landmark.add()
            landmark.x = float(point[0])
            landmark.y = float(point[1])
            landmark.z = float(point[2])
            if len(point) > 3:  # visibility para pose
                landmark.visibility = float(point[3])

        return landmark_list

    def show_frame(self, frame_idx: int):
        """
        Muestra un frame específico en el canvas.

        Args:
            frame_idx: Índice del frame a mostrar
        """
        if frame_idx < 0 or frame_idx >= self.total_frames:
            return

        self.current_frame_idx = frame_idx

        # Obtener frame y dibujar landmarks
        frame = self.video_frames[frame_idx]
        frame_with_landmarks = self.draw_landmarks_on_frame(frame, frame_idx)

        # Convertir BGR a RGB
        frame_rgb = cv2.cvtColor(frame_with_landmarks, cv2.COLOR_BGR2RGB)

        # Redimensionar para canvas manteniendo aspect ratio
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if canvas_width > 1 and canvas_height > 1:
            h, w = frame_rgb.shape[:2]
            scale = min(canvas_width / w, canvas_height / h)
            new_w, new_h = int(w * scale), int(h * scale)
            frame_resized = cv2.resize(frame_rgb, (new_w, new_h))
        else:
            frame_resized = frame_rgb

        # Convertir a ImageTk
        image = Image.fromarray(frame_resized)
        photo = ImageTk.PhotoImage(image)

        # Mostrar en canvas
        self.canvas.delete("all")
        self.canvas.create_image(
            canvas_width // 2,
            canvas_height // 2,
            image=photo,
            anchor=tk.CENTER
        )
        self.canvas.image = photo  # Mantener referencia

        # Actualizar slider y label
        self.frame_slider.set(frame_idx)
        self.frame_label.config(text=f"{frame_idx + 1} / {self.total_frames}")

    def on_slider_change(self, value):
        """Callback para cambios en el slider."""
        frame_idx = int(float(value))
        self.show_frame(frame_idx)

    def toggle_play(self):
        """Alterna entre play y pause."""
        if self.is_playing:
            self.is_playing = False
            self.play_button.config(text="▶ Play")
        else:
            self.is_playing = True
            self.play_button.config(text="⏸ Pause")
            self.play_thread = threading.Thread(target=self._play_loop, daemon=True)
            self.play_thread.start()

    def _play_loop(self):
        """Loop de reproducción en thread separado."""
        fps = self.data.get('fps', 30.0)
        delay = 1.0 / fps

        while self.is_playing and self.current_frame_idx < self.total_frames - 1:
            self.current_frame_idx += 1
            self.root.after(0, self.show_frame, self.current_frame_idx)
            threading.Event().wait(delay)

        if self.current_frame_idx >= self.total_frames - 1:
            self.root.after(0, self._stop_playback)

    def _stop_playback(self):
        """Detiene la reproducción."""
        self.is_playing = False
        self.play_button.config(text="▶ Play")

    def generate_video(self):
        """Genera video con landmarks dibujados."""
        if not self.data or not self.video_frames:
            messagebox.showwarning("Advertencia", "Primero carga un archivo .npy")
            return

        # Pedir ubicación de guardado
        output_path = filedialog.asksaveasfilename(
            title="Guardar video como",
            defaultextension=".mp4",
            filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")],
            initialfile=f"{self.npy_path.stem}_with_landmarks.mp4"
        )

        if not output_path:
            return

        # Deshabilitar botón durante generación
        self.generate_button.config(state=tk.DISABLED)
        self.progress_label.config(text="Generando video...")

        # Generar en thread separado
        thread = threading.Thread(
            target=self._generate_video_thread,
            args=(output_path,),
            daemon=True
        )
        thread.start()

    def _generate_video_thread(self, output_path: str):
        """Thread para generar video sin bloquear GUI."""
        try:
            fps = self.data.get('fps', 30.0)
            height, width = self.video_frames[0].shape[:2]

            # Configurar codec H.264
            fourcc = cv2.VideoWriter_fourcc(*'avc1')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

            if not out.isOpened():
                # Fallback a x264
                fourcc = cv2.VideoWriter_fourcc(*'x264')
                out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

            # Procesar cada frame
            for i, frame in enumerate(self.video_frames):
                frame_with_landmarks = self.draw_landmarks_on_frame(frame, i)
                out.write(frame_with_landmarks)

                # Actualizar progreso
                progress = (i + 1) / self.total_frames * 100
                self.root.after(
                    0,
                    self.progress_label.config,
                    {'text': f"Progreso: {progress:.1f}%"}
                )

            out.release()

            # Notificar éxito
            self.root.after(
                0,
                lambda: messagebox.showinfo(
                    "Éxito",
                    f"Video generado exitosamente:\n{output_path}"
                )
            )

        except Exception as e:
            self.root.after(
                0,
                lambda: messagebox.showerror(
                    "Error",
                    f"Error generando video:\n{str(e)}"
                )
            )

        finally:
            # Re-habilitar botón
            self.root.after(0, self.generate_button.config, {'state': tk.NORMAL})
            self.root.after(0, self.progress_label.config, {'text': ''})


def main():
    """Función principal."""
    root = tk.Tk()
    app = LSMVisualizer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
