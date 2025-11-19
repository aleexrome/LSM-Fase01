#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para Raspberry Pi - Grabación de video LSM con timestamps
Registra las señas en un archivo CSV en lugar de codificar audio FSK
"""

import time
import csv
from datetime import datetime
from pathlib import Path
import RPi.GPIO as GPIO

# Configuración de pines GPIO
BUTTON_START_PIN = 17  # Botón para iniciar una seña (conectado a GPIO17)
BUTTON_ERROR_PIN = 27  # Botón para marcar error (conectado a GPIO27)

# Archivo de timestamps
TIMESTAMPS_FILE = "timestamps.csv"

class TimestampRecorder:
    """Grabador de timestamps para señas LSM."""

    def __init__(self, video_filename: str):
        """
        Inicializa el grabador de timestamps.

        Args:
            video_filename: Nombre del archivo de video que se está grabando
        """
        self.video_filename = video_filename
        self.csv_filename = video_filename.replace('.mp4', '_timestamps.csv')
        self.start_time = None
        self.current_sign_id = 0
        self.recording = False

        # Configurar GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUTTON_START_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BUTTON_ERROR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Crear archivo CSV con encabezados
        self._init_csv()

    def _init_csv(self):
        """Inicializa el archivo CSV con los encabezados."""
        with open(self.csv_filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'event_type', 'sign_id'])

        print(f"✓ Archivo CSV creado: {self.csv_filename}")

    def start_recording(self):
        """Inicia la grabación de timestamps."""
        self.start_time = time.time()
        self.recording = True
        print(f"✓ Grabación iniciada en {datetime.now().strftime('%H:%M:%S')}")
        print(f"  Video: {self.video_filename}")
        print(f"  CSV: {self.csv_filename}")
        print("\nPresiona los botones:")
        print(f"  - GPIO{BUTTON_START_PIN}: Iniciar seña (incrementa ID automáticamente)")
        print(f"  - GPIO{BUTTON_ERROR_PIN}: Marcar error")
        print("  - Ctrl+C: Finalizar grabación\n")

    def get_current_timestamp(self) -> float:
        """Obtiene el timestamp actual relativo al inicio de la grabación."""
        if not self.start_time:
            return 0.0
        return time.time() - self.start_time

    def record_sign_start(self):
        """Registra el inicio de una seña."""
        self.current_sign_id += 1
        timestamp = self.get_current_timestamp()

        with open(self.csv_filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([f"{timestamp:.2f}", "inicio_seña", self.current_sign_id])

        print(f"[{timestamp:6.2f}s] SEÑA ID {self.current_sign_id:3d} - Inicio registrado")

    def record_error(self):
        """Registra un evento de error."""
        timestamp = self.get_current_timestamp()

        with open(self.csv_filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([f"{timestamp:.2f}", "error", ""])

        print(f"[{timestamp:6.2f}s] ERROR - Marcado")

    def run(self):
        """Loop principal del grabador."""
        self.start_recording()

        try:
            # Callback para botón de inicio de seña
            GPIO.add_event_detect(
                BUTTON_START_PIN,
                GPIO.FALLING,
                callback=lambda x: self.record_sign_start(),
                bouncetime=300  # Debounce de 300ms
            )

            # Callback para botón de error
            GPIO.add_event_detect(
                BUTTON_ERROR_PIN,
                GPIO.FALLING,
                callback=lambda x: self.record_error(),
                bouncetime=300
            )

            # Mantener el programa corriendo
            print("Sistema listo. Esperando eventos...\n")
            while self.recording:
                time.sleep(0.1)

        except KeyboardInterrupt:
            print("\n\n✓ Grabación finalizada")
            self.stop_recording()

    def stop_recording(self):
        """Detiene la grabación y limpia recursos."""
        self.recording = False
        total_time = self.get_current_timestamp()

        print(f"\nResumen de la grabación:")
        print(f"  Duración total: {total_time:.1f} segundos")
        print(f"  Señas registradas: {self.current_sign_id}")
        print(f"  Archivo guardado: {self.csv_filename}")

        # Limpiar GPIO
        GPIO.cleanup()


def main():
    """Función principal."""
    import sys

    if len(sys.argv) < 2:
        print("Uso: python raspberry_recorder.py <nombre_video.mp4>")
        print("\nEjemplo: python raspberry_recorder.py origen.mp4")
        sys.exit(1)

    video_filename = sys.argv[1]

    # Verificar que el nombre termine en .mp4
    if not video_filename.endswith('.mp4'):
        video_filename += '.mp4'

    print("=" * 60)
    print("  Grabador de Timestamps LSM - Raspberry Pi")
    print("=" * 60)
    print()

    recorder = TimestampRecorder(video_filename)
    recorder.run()


if __name__ == "__main__":
    main()
