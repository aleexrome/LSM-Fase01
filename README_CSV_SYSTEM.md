# Sistema de Timestamps CSV para LSM

Este sistema reemplaza la codificación FSK en audio con un sistema más simple y confiable basado en archivos CSV.

## 🎯 Ventajas del nuevo sistema

- ✅ **100% confiable**: No hay problemas de decodificación de audio
- ✅ **Simple**: Solo se guardan timestamps en un archivo CSV
- ✅ **Flexible**: Fácil de editar y corregir manualmente
- ✅ **Rápido**: No requiere análisis FFT del audio
- ✅ **Debugging**: Los timestamps son legibles y editables

---

## 📁 Archivos del sistema

### Para Raspberry Pi (grabación):
- **`raspberry_recorder.py`**: Script que registra timestamps cuando se presionan botones

### Para PC (procesamiento):
- **`lsm_processor_csv.py`**: Procesa videos usando timestamps desde CSV
- **`<video>_timestamps.csv`**: Archivo CSV con los timestamps de las señas

---

## 🔧 Configuración en Raspberry Pi

### 1. Conexión de hardware

Conecta dos botones a la Raspberry Pi:

```
Botón de INICIO DE SEÑA:
  - Pin físico: GPIO17
  - Conectar entre GPIO17 y GND

Botón de ERROR:
  - Pin físico: GPIO27
  - Conectar entre GPIO27 y GND
```

### 2. Instalación de dependencias

```bash
sudo apt-get update
sudo apt-get install python3-rpi.gpio
```

### 3. Uso durante grabación

```bash
# Iniciar grabación de video (con cualquier método que uses)
# Por ejemplo:
raspivid -o mi_video.h264 -t 60000 &

# En otra terminal, iniciar el grabador de timestamps
python3 raspberry_recorder.py mi_video.mp4
```

**Durante la grabación:**
- Presiona el **botón GPIO17** cada vez que inicies una seña (el ID se incrementa automáticamente)
- Presiona el **botón GPIO27** si cometes un error
- Presiona **Ctrl+C** para finalizar

El script creará automáticamente un archivo `mi_video_timestamps.csv`

---

## 💻 Procesamiento en PC

### 1. Transferir archivos desde Raspberry Pi

Transfiere estos archivos a tu PC:
- El video: `mi_video.mp4` (o `.h264`)
- El CSV: `mi_video_timestamps.csv`

### 2. Convertir video (si es necesario)

Si el video está en formato `.h264`, conviértelo a MP4:

```bash
ffmpeg -i mi_video.h264 -c:v copy mi_video.mp4
```

### 3. Procesar el video

```bash
python lsm_processor_csv.py --input mi_video.mp4 --csv mi_video_timestamps.csv
```

Los clips se guardarán en la carpeta `extraidos/`:
- `c001.mp4`, `c001.npy` (video y landmarks de la seña ID 1)
- `c002.mp4`, `c002.npy` (video y landmarks de la seña ID 2)
- etc.

---

## 📝 Formato del archivo CSV

El archivo CSV tiene 3 columnas:

```csv
timestamp,event_type,sign_id
10.25,inicio_seña,1
14.00,inicio_seña,5
24.62,inicio_seña,7
27.25,inicio_seña,15
```

### Columnas:

- **`timestamp`**: Tiempo en segundos desde el inicio del video
- **`event_type`**: Tipo de evento (`inicio_seña` o `error`)
- **`sign_id`**: ID de la seña (número del 1 al 255), vacío para errores

### Edición manual:

Puedes editar este archivo manualmente para:
- Corregir timestamps incorrectos
- Añadir señas que olvidaste marcar
- Eliminar marcas incorrectas
- Cambiar IDs de señas

---

## 🎮 Ejemplo de flujo completo

### En Raspberry Pi:

1. Conectar botones a GPIO17 y GPIO27
2. Iniciar grabación de video
3. Ejecutar: `python3 raspberry_recorder.py mi_video.mp4`
4. Realizar señas, presionando el botón al inicio de cada una
5. Presionar Ctrl+C al finalizar
6. Transferir `mi_video.mp4` y `mi_video_timestamps.csv` al PC

### En PC:

1. Verificar que ambos archivos estén en la misma carpeta
2. Ejecutar: `python lsm_processor_csv.py --input mi_video.mp4`
3. Los clips procesados estarán en `extraidos/`

---

## 🔍 Verificación y debugging

### Ver los timestamps registrados:

```bash
cat mi_video_timestamps.csv
```

### Ver log detallado del procesamiento:

```bash
python lsm_processor_csv.py --input mi_video.mp4 --log-level DEBUG
```

### Ver estadísticas rápidas:

```bash
# Contar señas en el CSV
grep "inicio_seña" mi_video_timestamps.csv | wc -l

# Contar clips generados
ls extraidos/*.mp4 | wc -l
```

---

## 🆚 Comparación con sistema FSK

| Característica | Sistema FSK (viejo) | Sistema CSV (nuevo) |
|----------------|---------------------|---------------------|
| Confiabilidad | ~50% (problemas de audio) | 100% |
| Facilidad de uso | Complicado | Simple |
| Debugging | Difícil | Fácil (archivo legible) |
| Corrección manual | Imposible | Fácil (editar CSV) |
| Velocidad | Lento (FFT) | Rápido |
| Dependencias | Audio FSK | Solo timestamps |

---

## ❓ Preguntas frecuentes

### ¿Qué pasa si olvidé presionar el botón para una seña?

Edita manualmente el archivo CSV y añade la línea con el timestamp correcto:

```csv
23.50,inicio_seña,7
```

### ¿Puedo usar el mismo CSV para múltiples videos?

No, cada video debe tener su propio archivo CSV con timestamps específicos.

### ¿Qué pasa si presiono el botón por error?

Edita el CSV y elimina o corrige la línea incorrecta antes de procesar.

### ¿Necesito el audio en el video?

No, el audio ya no se usa para nada. Puedes grabar video sin audio si lo prefieres.

### ¿Puedo usar un teclado en lugar de botones GPIO?

Sí, puedes modificar `raspberry_recorder.py` para usar entradas de teclado en lugar de GPIO.

---

## 📊 Ejemplo de salida

```
12:49:27 - INFO - Iniciando procesamiento de video: mi_video.mp4
12:49:27 - INFO - Cargando timestamps desde: mi_video_timestamps.csv
12:49:27 - INFO - Cargados 6 eventos 'inicio_seña' y 0 eventos 'error'
12:49:27 - INFO - Video: 30.0 FPS, 2316 frames
12:49:41 - INFO - Clip c001: Creado exitosamente (3.7s, 112 frames)
12:49:53 - INFO - Clip c007: Creado exitosamente (2.2s, 68 frames)
12:50:11 - INFO - Clip c029: Creado exitosamente (4.1s, 124 frames)
12:50:38 - INFO - === ESTADÍSTICAS FINALES ===
12:50:38 - INFO - Total señas detectadas: 6
12:50:38 - INFO - Clips válidos creados: 3
12:50:38 - INFO - Clips descartados: 3
12:50:38 - INFO - Tasa de éxito: 50.0%
```

---

## 🎓 Sistema antiguo (FSK) vs nuevo (CSV)

Si quieres seguir usando el sistema antiguo con codificación FSK en audio:
- Usa `lsm_processor.py` (sistema viejo)

Si quieres usar el nuevo sistema con CSV (recomendado):
- Usa `raspberry_recorder.py` (para grabar)
- Usa `lsm_processor_csv.py` (para procesar)
