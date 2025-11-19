# Sistema de Procesamiento de Videos LSM

Sistema para grabar y procesar videos de Lengua de Señas Mexicana (LSM) con detección automática de clips mediante timestamps CSV.

## 📁 Estructura del Proyecto

```
LSMProcessor/
├── raspberry_recorder.py      # Grabador para Raspberry Pi (GPIO)
├── keyboard_recorder.py        # Grabador simulado (teclado)
├── lsm_processor_csv.py       # Procesador de videos
├── origen_timestamps.csv       # Ejemplo de timestamps
├── extraidos/                  # Clips procesados (salida)
│   ├── c001.mp4
│   ├── c001.npy
│   └── ...
└── docs/
    ├── README_CSV_SYSTEM.md   # Manual completo
    ├── MIGRATION_GUIDE.md     # Guía técnica
    └── RESUMEN_CAMBIOS.md     # Resumen ejecutivo
```

## 🚀 Inicio Rápido

### Para Raspberry Pi (Grabación):

```bash
# 1. Conectar botones GPIO:
#    - GPIO17: Botón de inicio de seña
#    - GPIO27: Botón de error

# 2. Ejecutar grabador
python3 raspberry_recorder.py mi_video.mp4

# 3. Presionar botones durante la grabación
# 4. Ctrl+C para finalizar
# 5. Se genera: mi_video_timestamps.csv
```

### Para PC (Procesamiento):

```bash
# Procesar video con timestamps
python lsm_processor_csv.py --input mi_video.mp4

# Clips generados en: extraidos/
# - c001.mp4, c001.npy (video + landmarks)
# - c002.mp4, c002.npy
# - etc.
```

## 📝 Formato del CSV

```csv
timestamp,event_type,sign_id
10.25,inicio_seña,1
14.00,inicio_seña,5
24.62,inicio_seña,7
```

**Columnas:**
- `timestamp`: Tiempo en segundos desde inicio del video
- `event_type`: "inicio_seña" o "error"
- `sign_id`: ID de la seña (1-255), vacío para errores

## 🎯 Características

- ✅ **100% Confiable**: Sistema basado en timestamps CSV
- ✅ **Fácil de Usar**: Solo presionar botones durante grabación
- ✅ **Editable**: Corregir timestamps manualmente si es necesario
- ✅ **Sin Dependencias de Audio**: No requiere codificación FSK
- ✅ **Detección Automática**: Detecta fin de seña por posición de muñecas
- ✅ **Extracción de Landmarks**: MediaPipe Holistic (pose, cara, manos)

## 📦 Requisitos

### Raspberry Pi:
```bash
sudo apt-get install python3-rpi.gpio
```

### PC:
```bash
pip install opencv-python mediapipe numpy scipy moviepy soundfile
```

## 📚 Documentación Completa

- **[README_CSV_SYSTEM.md](README_CSV_SYSTEM.md)**: Manual completo del usuario
- **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)**: Guía técnica de migración
- **[RESUMEN_CAMBIOS.md](RESUMEN_CAMBIOS.md)**: Resumen de cambios

## 🎮 Controles

### Raspberry Pi (GPIO):
- **GPIO17 + GND**: Registrar inicio de seña
- **GPIO27 + GND**: Marcar error
- **Ctrl+C**: Finalizar grabación

### PC Modo Prueba (Teclado):
```bash
python keyboard_recorder.py test_video.mp4
```
- **ESPACIO**: Registrar inicio de seña
- **E**: Marcar error
- **Q**: Finalizar

## 🔧 Uso Avanzado

### Opciones del procesador:

```bash
# Especificar archivo CSV manualmente
python lsm_processor_csv.py --input video.mp4 --csv timestamps.csv

# Cambiar directorio de salida
python lsm_processor_csv.py --input video.mp4 --output mis_clips/

# Modo debug
python lsm_processor_csv.py --input video.mp4 --log-level DEBUG
```

### Editar timestamps manualmente:

```bash
# Abrir CSV en editor
nano mi_video_timestamps.csv

# Añadir, corregir o eliminar líneas
# Formato: timestamp,event_type,sign_id
```

## 📊 Ejemplo de Flujo Completo

### 1. Grabación en Raspberry Pi:
```bash
# Iniciar cámara
raspivid -o video.h264 -t 60000 &

# Iniciar grabador de timestamps
python3 raspberry_recorder.py video.mp4

# Realizar señas, presionando botón al inicio de cada una
# Ctrl+C al finalizar

# Transferir archivos a PC
scp video.h264 video_timestamps.csv user@pc:/ruta/
```

### 2. Conversión de video (si es necesario):
```bash
ffmpeg -i video.h264 -c:v copy video.mp4
```

### 3. Procesamiento en PC:
```bash
python lsm_processor_csv.py --input video.mp4

# Ver resultados
ls -lh extraidos/
```

## 🎓 Detalles Técnicos

### Procesamiento:
- **MediaPipe Holistic**: Extracción de landmarks
  - Pose: 33 puntos (posición del cuerpo)
  - Cara: 468 puntos (expresiones faciales)
  - Manos: 21 puntos × 2 (ambas manos)

### Detección de Fin de Seña:
- **Método 1**: Siguiente evento de inicio
- **Método 2**: Muñecas por debajo del umbral (Y > 0.75)
- **Método 3**: Timeout de 6 segundos

### Validación de Clips:
- Duración mínima: 0.5 segundos
- Duración máxima: 6.0 segundos
- Sin señales de error posteriores

## ❓ Preguntas Frecuentes

### ¿Qué pasa si olvidé presionar el botón?
Edita manualmente el CSV y añade la línea con el timestamp correcto.

### ¿Puedo usar el sistema sin Raspberry Pi?
Sí, usa `keyboard_recorder.py` para pruebas en PC con teclado.

### ¿Necesito audio en el video?
No, el sistema no depende del audio. Solo usa timestamps del CSV.

### ¿Cómo verifico los clips generados?
```bash
ls -lh extraidos/
# Reproduce con: vlc extraidos/c001.mp4
```

### ¿Puedo cambiar los IDs de las señas?
Sí, edita el CSV antes de procesar y cambia la columna `sign_id`.

## 🐛 Resolución de Problemas

### Error: "Archivo CSV no encontrado"
```bash
# Verificar que existe el CSV
ls -l *timestamps.csv

# Especificar manualmente
python lsm_processor_csv.py --input video.mp4 --csv ruta/al/archivo.csv
```

### Error: "Archivo de video no encontrado"
```bash
# Verificar ruta del video
ls -l *.mp4

# Usar ruta completa
python lsm_processor_csv.py --input ./video.mp4
```

### No se generan clips
```bash
# Verificar timestamps en CSV
cat video_timestamps.csv

# Ver logs detallados
python lsm_processor_csv.py --input video.mp4 --log-level DEBUG
```

## 📈 Estadísticas de Ejemplo

```
Total señas detectadas: 6
Clips válidos creados: 4
Clips descartados: 2
Tasa de éxito: 66.7%

Clips descartados por:
- Timeout (>6s): 1
- Duración inválida: 0
- Error posterior: 1
```

## 🤝 Contribuir

Para reportar problemas o sugerir mejoras:
1. Revisar documentación en `README_CSV_SYSTEM.md`
2. Ejecutar con `--log-level DEBUG` y guardar el log
3. Compartir video de prueba y CSV de timestamps

## 📄 Licencia

Este proyecto está desarrollado para investigación en Lengua de Señas Mexicana.

## 🔗 Referencias

- MediaPipe: https://google.github.io/mediapipe/
- OpenCV: https://opencv.org/
- Raspberry Pi GPIO: https://www.raspberrypi.org/documentation/

---

**Versión**: 2.0 (Sistema CSV)
**Fecha**: Noviembre 2025
**Autor**: Sistema generado por Claude
