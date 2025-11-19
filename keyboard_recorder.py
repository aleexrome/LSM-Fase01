#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simulador de grabación de timestamps usando teclado
Útil para pruebas sin hardware Raspberry Pi
"""

import time
import csv
from datetime import datetime
from pathlib import Path
import sys
import threading

# Para detectar teclas en tiempo real
try:
    import msvcrt  # Windows
    IS_WINDOWS = True
except ImportError:
    import tty
    import termios
    IS_WINDOWS = False


class KeyboardRecorder:
    """Grabador de timestamps usando teclado (sin GPIO)."""

    def __init__(self, video_filename: str):
        """
        Inicializa el grabador de timestamps.

        Args:
            video_filename: Nombre del archivo de video
        """
        self.video_filename = video_filename
        self.csv_filename = video_filename.replace('.mp4', '_timestamps.csv')
        self.start_time = None
        self.current_sign_id = 0
        self.recording = False

        # Crear archivo CSV con encabezados
        self._init_csv()

    def _init_csv(self):
        """Inicializa el archivo CSV con los encabezados."""
        with open(self.csv_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'event_type', 'sign_id'])

        print(f"✓ Archivo CSV creado: {self.csv_filename}")

    def start_recording(self):
        """Inicia la grabación de timestamps."""
        self.start_time = time.time()
        self.recording = True
        print(f"\n{'='*60}")
        print(f"  Grabador de Timestamps LSM - Modo Teclado")
        print(f"{'='*60}")
        print(f"✓ Grabación iniciada en {datetime.now().strftime('%H:%M:%S')}")
        print(f"  Video: {self.video_filename}")
        print(f"  CSV: {self.csv_filename}")
        print(f"\n{'='*60}")
        print("  CONTROLES:")
        print("  - Presiona ESPACIO: Registrar inicio de seña")
        print("  - Presiona E: Marcar error")
        print("  - Presiona Q: Finalizar grabación")
        print(f"{'='*60}\n")

    def get_current_timestamp(self) -> float:
        """Obtiene el timestamp actual relativo al inicio."""
        if not self.start_time:
            return 0.0
        return time.time() - self.start_time

    def record_sign_start(self):
        """Registra el inicio de una seña."""
        self.current_sign_id += 1
        timestamp = self.get_current_timestamp()

        with open(self.csv_filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([f"{timestamp:.2f}", "inicio_seña", self.current_sign_id])

        print(f"[{timestamp:6.2f}s] ✓ SEÑA ID {self.current_sign_id:3d} - Registrada")

    def record_error(self):
        """Registra un evento de error."""
        timestamp = self.get_current_timestamp()

        with open(self.csv_filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([f"{timestamp:.2f}", "error", ""])

        print(f"[{timestamp:6.2f}s] ⚠ ERROR - Marcado")

    def get_key_windows(self):
        """Lee tecla en Windows."""
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            return key
        return None

    def get_key_unix(self):
        """Lee tecla en Unix/Linux."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch.lower()

    def run(self):
        """Loop principal del grabador."""
        self.start_recording()

        try:
            while self.recording:
                # Leer tecla según el sistema operativo
                if IS_WINDOWS:
                    key = self.get_key_windows()
                    if key is None:
                        time.sleep(0.01)
                        continue
                else:
                    key = self.get_key_unix()

                # Procesar tecla
                if key == ' ':  # Espacio
                    self.record_sign_start()
                elif key == 'e':
                    self.record_error()
                elif key == 'q':
                    print("\n\n✓ Finalizando grabación...")
                    self.stop_recording()
                    break

        except KeyboardInterrupt:
            print("\n\n✓ Grabación interrumpida")
            self.stop_recording()

    def stop_recording(self):
        """Detiene la grabación."""
        self.recording = False
        total_time = self.get_current_timestamp()

        print(f"\n{'='*60}")
        print("  RESUMEN DE LA GRABACIÓN")
        print(f"{'='*60}")
        print(f"  Duración total: {total_time:.1f} segundos")
        print(f"  Señas registradas: {self.current_sign_id}")
        print(f"  Archivo guardado: {self.csv_filename}")
        print(f"{'='*60}\n")


def main():
    """Función principal."""
    if len(sys.argv) < 2:
        print("\n" + "="*60)
        print("  Grabador de Timestamps LSM - Modo Teclado")
        print("="*60)
        print("\nUso: python keyboard_recorder.py <nombre_video.mp4>")
        print("\nEjemplo:")
        print("  python keyboard_recorder.py mi_video.mp4")
        print("\nEsto creará el archivo: mi_video_timestamps.csv")
        print("="*60 + "\n")
        sys.exit(1)

    video_filename = sys.argv[1]

    # Verificar que el nombre termine en .mp4
    if not video_filename.endswith('.mp4'):
        video_filename += '.mp4'

    recorder = KeyboardRecorder(video_filename)
    recorder.run()


if __name__ == "__main__":
    main()
