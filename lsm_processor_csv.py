#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Procesamiento de Videos de Lengua de Señas Mexicana
Versión simplificada que lee timestamps desde archivo CSV
Autor: Script generado por Claude
Fecha: 2025
"""

import cv2
import numpy as np
import mediapipe as mp
import logging
import argparse
import csv
import shutil
from pathlib import Path
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional, Any
from dataclasses import dataclass


# Configuración de colores para logging en consola
class LogColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    ENDC = '\033[0m'


class ProcessingState(Enum):
    """Estados de la máquina de estados para procesamiento."""
    SEARCHING = "buscando_inicio"
    RECORDING = "grabando_seña"


@dataclass
class TimestampEvent:
    """Estructura para eventos leídos del CSV."""
    timestamp: float
    event_type: str  # 'inicio_seña' o 'error'
    sign_id: Optional[int] = None


class ColoredFormatter(logging.Formatter):
    """Formatter personalizado para logs con colores."""

    COLORS = {
        'DEBUG': LogColors.CYAN,
        'INFO': LogColors.GREEN,
        'WARNING': LogColors.YELLOW,
        'ERROR': LogColors.RED,
        'CRITICAL': LogColors.MAGENTA,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, LogColors.WHITE)
        record.levelname = f"{log_color}{record.levelname}{LogColors.ENDC}"
        return super().format(record)


class LSMProcessorCSV:
    """
    Procesador para videos de Lengua de Señas Mexicana.
    Lee timestamps desde archivo CSV en lugar de decodificar audio.
    """

    def __init__(self, input_file: str, csv_file: str = None,
                 output_dir: str = "extraidos"):
        """
        Inicializa el procesador LSM.

        Args:
            input_file: Ruta al archivo MP4 de entrada
            csv_file: Ruta al archivo CSV con timestamps (si None, se busca automáticamente)
            output_dir: Directorio de salida para clips procesados
        """
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)

        # Buscar archivo CSV si no se especificó
        if csv_file is None:
            self.csv_file = self.input_file.with_suffix('').with_name(
                self.input_file.stem + '_timestamps.csv'
            )
        else:
            self.csv_file = Path(csv_file)

        # Configuración de MediaPipe
        self.mp_holistic = None
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic_module = mp.solutions.holistic

        # Estado interno
        self.events: List[TimestampEvent] = []
        self.current_state = ProcessingState.SEARCHING
        self.frame_buffer = []
        self.landmarks_buffer = []
        self.clips_created = 0
        self.clips_discarded = 0

        # Configuración de logging
        self._setup_logging()

        # Validaciones iniciales
        self._validate_input()

    def _setup_logging(self):
        """Configura el sistema de logging con archivo y consola."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"lsm_processing_{timestamp}.log"

        # Configurar logger principal
        self.logger = logging.getLogger('LSMProcessor')
        self.logger.setLevel(logging.DEBUG)

        # Handler para archivo
        file_handler = logging.FileHandler(log_filename, encoding='utf-8')
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)

        # Handler para consola con colores
        console_handler = logging.StreamHandler()
        console_formatter = ColoredFormatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def _validate_input(self):
        """Valida los archivos de entrada y crea directorios necesarios."""
        if not self.input_file.exists():
            raise FileNotFoundError(f"Archivo de video no encontrado: {self.input_file}")

        if not self.input_file.suffix.lower() == '.mp4':
            raise ValueError(f"Formato de archivo no válido: {self.input_file.suffix}")

        if not self.csv_file.exists():
            raise FileNotFoundError(
                f"Archivo CSV no encontrado: {self.csv_file}\n"
                f"Asegúrate de que el archivo de timestamps existe."
            )

        # Crear directorios necesarios
        self.output_dir.mkdir(exist_ok=True)

        # Verificar espacio en disco
        stat = shutil.disk_usage(self.output_dir)
        free_gb = stat.free / (1024**3)
        if free_gb < 1:
            self.logger.warning(f"Poco espacio en disco: {free_gb:.1f}GB libres")

    def load_timestamps(self) -> List[TimestampEvent]:
        """
        Carga los timestamps desde el archivo CSV.

        Returns:
            Lista de eventos ordenados cronológicamente
        """
        self.logger.info(f"Cargando timestamps desde: {self.csv_file}")

        events = []

        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    timestamp = float(row['timestamp'])
                    event_type = row['event_type']
                    sign_id = int(row['sign_id']) if row['sign_id'] else None

                    events.append(TimestampEvent(timestamp, event_type, sign_id))

                    if event_type == 'inicio_seña':
                        self.logger.debug(f"Seña ID {sign_id} en timestamp {timestamp:.2f}s")
                    elif event_type == 'error':
                        self.logger.debug(f"Error en timestamp {timestamp:.2f}s")

            # Ordenar por timestamp
            events.sort(key=lambda x: x.timestamp)

            # Contar eventos
            sign_events = [e for e in events if e.event_type == 'inicio_seña']
            error_events = [e for e in events if e.event_type == 'error']

            self.logger.info(
                f"Cargados {len(sign_events)} eventos 'inicio_seña' y "
                f"{len(error_events)} eventos 'error'"
            )

            return events

        except Exception as e:
            self.logger.error(f"Error leyendo archivo CSV: {str(e)}")
            raise

    def initialize_mediapipe(self):
        """Inicializa MediaPipe Holistic con configuraciones optimizadas."""
        self.mp_holistic = self.mp_holistic_module.Holistic(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            enable_segmentation=False,
            smooth_segmentation=False,
            refine_face_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def check_end_condition(self, landmarks, log_positions=False) -> bool:
        """
        Verifica si ambas muñecas están en posición de fin de seña.

        Args:
            landmarks: Landmarks de pose de MediaPipe
            log_positions: Si True, registra las posiciones de las muñecas

        Returns:
            True si se cumple la condición de fin de seña
        """
        if not landmarks or not landmarks.pose_landmarks:
            return False

        pose_landmarks = landmarks.pose_landmarks.landmark

        # Índices de muñecas en MediaPipe
        left_wrist = pose_landmarks[15]
        right_wrist = pose_landmarks[16]

        if log_positions:
            self.logger.debug(f"Muñecas - Izq Y: {left_wrist.y:.3f}, Der Y: {right_wrist.y:.3f}")

        # Verificar si ambas muñecas están por debajo del umbral
        return left_wrist.y > 0.75 and right_wrist.y > 0.75

    def extract_landmarks_data(self, landmarks) -> Dict[str, Any]:
        """Extrae todos los landmarks de MediaPipe en formato estructurado."""
        data = {
            'pose_landmarks': None,
            'face_landmarks': None,
            'left_hand_landmarks': None,
            'right_hand_landmarks': None
        }

        # Pose landmarks (33 puntos x 4 dimensiones)
        if landmarks.pose_landmarks:
            pose_array = []
            for lm in landmarks.pose_landmarks.landmark:
                pose_array.append([lm.x, lm.y, lm.z, lm.visibility])
            data['pose_landmarks'] = np.array(pose_array)

        # Face landmarks (468 puntos x 3 dimensiones)
        if landmarks.face_landmarks:
            face_array = []
            for lm in landmarks.face_landmarks.landmark:
                face_array.append([lm.x, lm.y, lm.z])
            data['face_landmarks'] = np.array(face_array)

        # Left hand landmarks (21 puntos x 3 dimensiones)
        if landmarks.left_hand_landmarks:
            left_hand_array = []
            for lm in landmarks.left_hand_landmarks.landmark:
                left_hand_array.append([lm.x, lm.y, lm.z])
            data['left_hand_landmarks'] = np.array(left_hand_array)

        # Right hand landmarks (21 puntos x 3 dimensiones)
        if landmarks.right_hand_landmarks:
            right_hand_array = []
            for lm in landmarks.right_hand_landmarks.landmark:
                right_hand_array.append([lm.x, lm.y, lm.z])
            data['right_hand_landmarks'] = np.array(right_hand_array)

        return data

    def validate_clip(self, start_time: float, end_time: float, sign_id: int) -> bool:
        """Valida si un clip es válido según los criterios establecidos."""
        duration = end_time - start_time

        # Verificar duración válida (0.5 a 6 segundos)
        if duration < 0.5 or duration > 6.0:
            self.logger.warning(f"Clip c{sign_id:03d}: Duración inválida ({duration:.1f}s)")
            return False

        # Buscar eventos de error después del fin del clip
        for event in self.events:
            if event.timestamp > end_time and event.timestamp < end_time + 0.5:
                if event.event_type == 'error':
                    self.logger.warning(f"Clip c{sign_id:03d}: Descartado por señal de error")
                    return False

        return True

    def save_clip(self, frames: List[np.ndarray], landmarks_data: List[Dict],
                  timestamps: List[float], fps: float, sign_id: int):
        """Guarda un clip de video y sus landmarks correspondientes."""
        try:
            # Paths de salida
            video_path = self.output_dir / f"c{sign_id:03d}.mp4"
            landmarks_path = self.output_dir / f"c{sign_id:03d}.npy"

            # Guardar video
            if frames:
                height, width = frames[0].shape[:2]

                try:
                    fourcc = cv2.VideoWriter_fourcc(*'avc1')
                    out = cv2.VideoWriter(str(video_path), fourcc, fps, (width, height))

                    if not out.isOpened():
                        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                        out = cv2.VideoWriter(str(video_path), fourcc, fps, (width, height))

                    for frame in frames:
                        out.write(frame)
                    out.release()

                except Exception as e:
                    self.logger.error(f"Error guardando video: {str(e)}")
                    raise

            # Preparar datos de landmarks
            landmarks_output = {
                'pose_landmarks': [],
                'face_landmarks': [],
                'left_hand_landmarks': [],
                'right_hand_landmarks': [],
                'frame_timestamps': timestamps,
                'fps': fps,
                'sign_id': sign_id
            }

            # Organizar landmarks por tipo
            for frame_data in landmarks_data:
                for key in ['pose_landmarks', 'face_landmarks',
                           'left_hand_landmarks', 'right_hand_landmarks']:
                    landmarks_output[key].append(frame_data.get(key))

            # Guardar landmarks
            np.save(str(landmarks_path), landmarks_output)

            duration = timestamps[-1] - timestamps[0] if timestamps else 0
            self.logger.info(
                f"Clip c{sign_id:03d}: Creado exitosamente "
                f"({duration:.1f}s, {len(frames)} frames)"
            )
            self.clips_created += 1

        except Exception as e:
            self.logger.error(f"Error guardando clip c{sign_id:03d}: {str(e)}")
            self.clips_discarded += 1

    def process_video(self):
        """Procesa el video principal extrayendo clips de señas válidos."""
        self.logger.info("Iniciando procesamiento de video...")

        try:
            # Inicializar MediaPipe
            self.initialize_mediapipe()

            # Abrir video
            cap = cv2.VideoCapture(str(self.input_file))
            if not cap.isOpened():
                raise RuntimeError("No se pudo abrir el archivo de video")

            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            self.logger.info(f"Video: {fps:.1f} FPS, {total_frames} frames")

            # Variables de estado
            current_event_idx = 0
            frame_count = 0
            end_condition_counter = 0
            current_clip_start_time = None
            current_clip_start_frame = None

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                current_time = frame_count / fps
                frame_count += 1

                # Procesar frame con MediaPipe
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.mp_holistic.process(rgb_frame)

                # Máquina de estados
                if self.current_state == ProcessingState.SEARCHING:
                    # Buscar próximo evento de inicio
                    if current_event_idx < len(self.events):
                        next_event = self.events[current_event_idx]

                        if (next_event.event_type == 'inicio_seña' and
                            abs(current_time - next_event.timestamp) < 0.1):

                            # Cambiar a estado de grabación
                            self.current_state = ProcessingState.RECORDING
                            current_clip_start_time = current_time
                            current_clip_start_frame = frame_count
                            self.frame_buffer = [frame.copy()]
                            self.landmarks_buffer = [self.extract_landmarks_data(results)]
                            self.current_clip_data = next_event
                            end_condition_counter = 0

                            self.logger.debug(
                                f"Iniciando grabación de seña ID {next_event.sign_id}"
                            )
                            current_event_idx += 1

                elif self.current_state == ProcessingState.RECORDING:
                    # Calcular duración actual del clip
                    current_clip_duration = current_time - current_clip_start_time

                    # Log posiciones cada 30 frames
                    log_this_frame = (frame_count - current_clip_start_frame) % 30 == 0

                    # Verificar si hay un próximo evento de inicio
                    should_end_by_next_event = False
                    if current_event_idx < len(self.events):
                        next_event = self.events[current_event_idx]
                        if (next_event.event_type == 'inicio_seña' and
                            abs(current_time - next_event.timestamp) < 0.1):
                            should_end_by_next_event = True

                    # Timeout: Si el clip excede 6 segundos, forzar fin
                    if current_clip_duration > 6.0:
                        self.logger.debug(
                            f"Seña ID {self.current_clip_data.sign_id}: "
                            f"Timeout (>6s), descartando"
                        )
                        self.clips_discarded += 1

                        # Resetear estado
                        self.current_state = ProcessingState.SEARCHING
                        self.frame_buffer = []
                        self.landmarks_buffer = []
                        self.current_clip_data = None
                        end_condition_counter = 0

                    # Fin por próximo evento de inicio
                    elif should_end_by_next_event and current_clip_duration >= 0.5:
                        clip_end_time = current_time
                        clip_duration = clip_end_time - current_clip_start_time

                        self.logger.debug(
                            f"Seña ID {self.current_clip_data.sign_id}: "
                            f"Fin por próximo evento en {clip_duration:.2f}s"
                        )

                        # Generar timestamps para frames del clip
                        frame_timestamps = []
                        for i in range(len(self.frame_buffer)):
                            timestamp = current_clip_start_time + (i / fps)
                            frame_timestamps.append(timestamp)

                        # Validar y guardar clip
                        if self.validate_clip(
                            current_clip_start_time,
                            clip_end_time,
                            self.current_clip_data.sign_id
                        ):
                            self.save_clip(
                                self.frame_buffer,
                                self.landmarks_buffer,
                                frame_timestamps,
                                fps,
                                self.current_clip_data.sign_id
                            )
                        else:
                            self.clips_discarded += 1

                        # Resetear estado
                        self.current_state = ProcessingState.SEARCHING
                        self.frame_buffer = []
                        self.landmarks_buffer = []
                        self.current_clip_data = None
                        end_condition_counter = 0

                    # Verificar condición de fin por muñecas
                    elif self.check_end_condition(results, log_positions=log_this_frame):
                        end_condition_counter += 1
                        if end_condition_counter >= 3:  # 3 frames consecutivos
                            # Fin de seña detectado
                            clip_end_time = current_time
                            clip_duration = clip_end_time - current_clip_start_time

                            self.logger.debug(
                                f"Seña ID {self.current_clip_data.sign_id}: "
                                f"Fin por muñecas en {clip_duration:.2f}s"
                            )

                            # Generar timestamps
                            frame_timestamps = []
                            for i in range(len(self.frame_buffer)):
                                timestamp = current_clip_start_time + (i / fps)
                                frame_timestamps.append(timestamp)

                            # Validar y guardar clip
                            if self.validate_clip(
                                current_clip_start_time,
                                clip_end_time,
                                self.current_clip_data.sign_id
                            ):
                                self.save_clip(
                                    self.frame_buffer,
                                    self.landmarks_buffer,
                                    frame_timestamps,
                                    fps,
                                    self.current_clip_data.sign_id
                                )
                            else:
                                self.clips_discarded += 1

                            # Resetear estado
                            self.current_state = ProcessingState.SEARCHING
                            self.frame_buffer = []
                            self.landmarks_buffer = []
                            self.current_clip_data = None
                            end_condition_counter = 0
                    else:
                        # Seguir agregando frames
                        self.frame_buffer.append(frame.copy())
                        self.landmarks_buffer.append(self.extract_landmarks_data(results))
                        end_condition_counter = 0

                # Mostrar progreso cada 1000 frames
                if frame_count % 1000 == 0:
                    progress = (frame_count / total_frames) * 100
                    self.logger.info(
                        f"Progreso: {progress:.1f}% ({frame_count}/{total_frames})"
                    )

            cap.release()
            self.mp_holistic.close()

            sign_count = len([e for e in self.events if e.event_type == 'inicio_seña'])
            self.logger.info(
                f"Procesamiento completado: {self.clips_created}/{sign_count} "
                f"clips válidos guardados"
            )

        except Exception as e:
            self.logger.error(f"Error procesando video: {str(e)}")
            raise

    def run(self):
        """Ejecuta el procesamiento completo del video LSM."""
        try:
            self.logger.info(f"Iniciando procesamiento de video: {self.input_file}")

            # Cargar timestamps desde CSV
            self.events = self.load_timestamps()

            # Procesar video
            self.process_video()

            # Estadísticas finales
            total_signs = len([e for e in self.events if e.event_type == 'inicio_seña'])
            success_rate = (self.clips_created / total_signs * 100) if total_signs > 0 else 0

            self.logger.info(f"=== ESTADÍSTICAS FINALES ===")
            self.logger.info(f"Total señas detectadas: {total_signs}")
            self.logger.info(f"Clips válidos creados: {self.clips_created}")
            self.logger.info(f"Clips descartados: {self.clips_discarded}")
            self.logger.info(f"Tasa de éxito: {success_rate:.1f}%")

        except Exception as e:
            self.logger.error(f"Error crítico durante procesamiento: {str(e)}")
            raise


def main():
    """Función principal con interfaz de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Procesador de videos de Lengua de Señas Mexicana (CSV)",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--input',
        required=True,
        help='Archivo MP4 de entrada con video de señas'
    )

    parser.add_argument(
        '--csv',
        help='Archivo CSV con timestamps (por defecto: <input>_timestamps.csv)'
    )

    parser.add_argument(
        '--output',
        default='extraidos',
        help='Directorio de salida para clips procesados (default: extraidos/)'
    )

    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO',
        help='Nivel de logging (default: INFO)'
    )

    args = parser.parse_args()

    try:
        # Configurar nivel de logging global
        logging.getLogger().setLevel(getattr(logging, args.log_level))

        # Crear y ejecutar procesador
        processor = LSMProcessorCSV(
            input_file=args.input,
            csv_file=args.csv,
            output_dir=args.output
        )

        processor.run()

        print(f"\n{LogColors.GREEN}OK Procesamiento completado exitosamente{LogColors.ENDC}")

    except KeyboardInterrupt:
        print(f"\n{LogColors.YELLOW}! Procesamiento interrumpido por el usuario{LogColors.ENDC}")
    except Exception as e:
        print(f"\n{LogColors.RED}X Error: {str(e)}{LogColors.ENDC}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
