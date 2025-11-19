# LSM Visualizer - Visualizador de Archivos NPY

Visualizador interactivo para archivos `.npy` generados por `lsm_processor_csv.py`. Permite explorar frames dinámicamente y generar videos con landmarks dibujados.

## Características

- **Navegación dinámica**: Slider para moverse entre frames
- **Reproducción**: Botón Play/Pause para ver la seña en movimiento
- **Visualización de landmarks**: Muestra todos los landmarks capturados:
  - Pose (33 puntos) - Verde
  - Face (468 puntos) - Amarillo
  - Manos izquierda y derecha (21 puntos cada una) - Magenta
- **Estadísticas de movimiento**: Calcula y muestra:
  - Velocidad promedio de muñecas (px/s)
  - Distancia total recorrida por las muñecas (px)
  - Nivel de actividad de las manos
- **Generación de video**: Exporta video MP4 con landmarks dibujados usando codec H.264

## Requisitos

```bash
pip install opencv-python numpy mediapipe pillow
```

## Uso

### Ejecución

```bash
python lsm_visualizer.py
```

### Interfaz

1. **Cargar archivo**: `Archivo > Cargar archivo .npy`
   - Selecciona un archivo `.npy` generado por `lsm_processor_csv.py`
   - El visualizador buscará automáticamente el video correspondiente (mismo nombre con extensión `.mp4`)

2. **Navegación**:
   - Usa el **slider** para moverte entre frames
   - **Play/Pause**: Reproduce la seña a velocidad normal
   - **Frame counter**: Muestra el frame actual y total

3. **Visualización**:
   - El canvas central muestra el frame actual con landmarks superpuestos
   - Colores:
     - 🟢 Verde: Pose corporal
     - 🟡 Amarillo: Rostro
     - 🟣 Magenta: Manos

4. **Estadísticas**:
   - Panel derecho muestra estadísticas de movimiento en tiempo real
   - Información del archivo (Sign ID, FPS, duración, etc.)

5. **Generar video**:
   - Click en **"Generar Video con Landmarks"**
   - Selecciona ubicación y nombre para guardar
   - El video se generará con codec H.264 y todos los landmarks dibujados
   - Barra de progreso muestra el avance

## Estructura de datos NPY

El visualizador espera archivos `.npy` con la siguiente estructura:

```python
{
    'pose_landmarks': List[np.ndarray],      # 33 puntos x (x, y, z, visibility)
    'face_landmarks': List[np.ndarray],      # 468 puntos x (x, y, z)
    'left_hand_landmarks': List[np.ndarray], # 21 puntos x (x, y, z)
    'right_hand_landmarks': List[np.ndarray],# 21 puntos x (x, y, z)
    'frame_timestamps': List[float],         # Timestamp de cada frame
    'fps': float,                            # Frames por segundo
    'sign_id': int                           # ID de la seña
}
```

## Ejemplos

### Cargar y visualizar una seña

```bash
# 1. Ejecutar visualizador
python lsm_visualizer.py

# 2. En la GUI: Archivo > Cargar archivo .npy
# 3. Seleccionar: extraidos/c001.npy
# 4. Usar slider para explorar frames
```

### Generar video con landmarks

```bash
# Desde la GUI después de cargar un .npy:
# 1. Click en "Generar Video con Landmarks"
# 2. Guardar como: c001_with_landmarks.mp4
# 3. Esperar a que complete el procesamiento
```

## Notas

- Si el video `.mp4` correspondiente no existe, se generarán frames en blanco
- La generación de video usa codec H.264 (avc1/x264) para mejor compresión
- El video generado mantiene el FPS original de la captura
- La reproducción se ejecuta en un thread separado para no bloquear la interfaz

## Troubleshooting

**Error: "Video no encontrado"**
- Asegúrate de que el archivo `.mp4` esté en la misma carpeta que el `.npy`
- Ejemplo: `c001.npy` requiere `c001.mp4`

**Error al generar video**
- Verifica que tienes instalado OpenCV con soporte H.264
- El visualizador intentará fallback a x264 si avc1 falla

**Landmarks no se ven**
- Verifica que el archivo `.npy` contiene datos de landmarks
- Checa el panel de información para confirmar landmarks disponibles
