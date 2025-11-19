# 📑 Índice del Proyecto LSM Processor

## 🎯 Archivos Principales

### Scripts Ejecutables

| Archivo | Descripción | Plataforma | Uso |
|---------|-------------|------------|-----|
| **[raspberry_recorder.py](raspberry_recorder.py)** | Grabador con botones GPIO | Raspberry Pi | `python3 raspberry_recorder.py video.mp4` |
| **[keyboard_recorder.py](keyboard_recorder.py)** | Simulador con teclado | PC | `python keyboard_recorder.py test.mp4` |
| **[lsm_processor_csv.py](lsm_processor_csv.py)** | Procesador de videos | PC | `python lsm_processor_csv.py --input video.mp4` |

### Archivos de Datos

| Archivo | Descripción |
|---------|-------------|
| **[origen_timestamps.csv](origen_timestamps.csv)** | Ejemplo de archivo CSV con 6 señas |

### Directorios

| Directorio | Descripción |
|------------|-------------|
| **[extraidos/](extraidos/)** | Clips procesados (c001.mp4, c001.npy, etc.) |

---

## 📚 Documentación

### Para Empezar

| Documento | Audiencia | Contenido |
|-----------|-----------|-----------|
| **[README.md](README.md)** | Todos | Inicio rápido, instalación, ejemplos básicos |
| **[README_CSV_SYSTEM.md](README_CSV_SYSTEM.md)** | Usuarios | Manual completo con instrucciones detalladas |

### Documentación Técnica

| Documento | Audiencia | Contenido |
|-----------|-----------|-----------|
| **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)** | Desarrolladores | Guía técnica, comparación FSK vs CSV |
| **[RESUMEN_CAMBIOS.md](RESUMEN_CAMBIOS.md)** | Gestión | Resumen ejecutivo de cambios |

---

## 🚀 Flujo de Trabajo Típico

### 1️⃣ Grabación (Raspberry Pi)

```bash
# Usar: raspberry_recorder.py
python3 raspberry_recorder.py mi_video.mp4
```

**Genera:**
- `mi_video_timestamps.csv` (timestamps de las señas)

### 2️⃣ Procesamiento (PC)

```bash
# Usar: lsm_processor_csv.py
python lsm_processor_csv.py --input mi_video.mp4
```

**Lee:**
- `mi_video.mp4` (video)
- `mi_video_timestamps.csv` (timestamps)

**Genera:**
- `extraidos/c001.mp4`, `c001.npy` (clip + landmarks)
- `extraidos/c002.mp4`, `c002.npy`
- etc.

### 3️⃣ Pruebas (PC sin hardware)

```bash
# Usar: keyboard_recorder.py
python keyboard_recorder.py test.mp4
```

**Controles:**
- ESPACIO: Registrar seña
- E: Marcar error
- Q: Finalizar

---

## 📖 Orden de Lectura Recomendado

### Para Usuarios Nuevos:

1. **[README.md](README.md)** - Inicio rápido (5 min)
2. **[README_CSV_SYSTEM.md](README_CSV_SYSTEM.md)** - Manual completo (15 min)
3. Probar con `keyboard_recorder.py` (práctica)

### Para Desarrolladores:

1. **[RESUMEN_CAMBIOS.md](RESUMEN_CAMBIOS.md)** - Contexto del proyecto (10 min)
2. **[MIGRATION_GUIDE.md](MIGRATION_GUIDE.md)** - Detalles técnicos (20 min)
3. Revisar código fuente de `lsm_processor_csv.py`

### Para Gestión/Supervisores:

1. **[RESUMEN_CAMBIOS.md](RESUMEN_CAMBIOS.md)** - Resumen ejecutivo (5 min)
2. **[README.md](README.md)** - Características principales (5 min)

---

## 🎓 Tutoriales por Caso de Uso

### Caso 1: Primera vez usando el sistema

**Lectura:**
1. [README.md](README.md) - Sección "Inicio Rápido"
2. [README_CSV_SYSTEM.md](README_CSV_SYSTEM.md) - Sección "Configuración en Raspberry Pi"

**Práctica:**
```bash
python keyboard_recorder.py prueba.mp4
# Presionar ESPACIO 3-4 veces, luego Q
# Se crea: prueba_timestamps.csv
```

### Caso 2: Grabar video real en Raspberry Pi

**Lectura:**
1. [README_CSV_SYSTEM.md](README_CSV_SYSTEM.md) - Sección "Configuración en Raspberry Pi"

**Hardware:**
- Conectar botones a GPIO17 y GPIO27

**Comandos:**
```bash
python3 raspberry_recorder.py mi_video.mp4
# Presionar botón GPIO17 al inicio de cada seña
# Ctrl+C al finalizar
```

### Caso 3: Procesar video grabado

**Lectura:**
1. [README.md](README.md) - Sección "Uso Avanzado"

**Comandos:**
```bash
# Básico
python lsm_processor_csv.py --input video.mp4

# Con debug
python lsm_processor_csv.py --input video.mp4 --log-level DEBUG

# CSV en otra ubicación
python lsm_processor_csv.py --input video.mp4 --csv /ruta/timestamps.csv
```

### Caso 4: Corregir timestamps después de grabar

**Lectura:**
1. [README_CSV_SYSTEM.md](README_CSV_SYSTEM.md) - Sección "Formato del archivo CSV"

**Pasos:**
```bash
# 1. Abrir CSV
nano video_timestamps.csv

# 2. Editar, añadir o eliminar líneas
timestamp,event_type,sign_id
10.25,inicio_seña,1
14.00,inicio_seña,5
# Añadir nueva seña:
18.50,inicio_seña,7

# 3. Guardar y procesar
python lsm_processor_csv.py --input video.mp4
```

### Caso 5: Migrar desde sistema FSK antiguo

**Lectura:**
1. [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) - Completo

**Acción:**
- Revisar comparativa FSK vs CSV
- Seguir checklist de migración

---

## 🔍 Búsqueda Rápida

### Busco información sobre...

| Tema | Archivo | Sección |
|------|---------|---------|
| Instalar dependencias | [README.md](README.md) | "Requisitos" |
| Conectar GPIO | [README_CSV_SYSTEM.md](README_CSV_SYSTEM.md) | "Configuración en Raspberry Pi" |
| Formato del CSV | Todos los README | "Formato del CSV" |
| Solucionar errores | [README.md](README.md) | "Resolución de Problemas" |
| Ventajas del sistema | [RESUMEN_CAMBIOS.md](RESUMEN_CAMBIOS.md) | "Ventajas del Sistema CSV" |
| Comparar con FSK | [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) | "Comparación FSK vs CSV" |
| Editar timestamps | [README_CSV_SYSTEM.md](README_CSV_SYSTEM.md) | "Edición manual" |
| Opciones del procesador | [README.md](README.md) | "Uso Avanzado" |

---

## 📊 Archivos por Tamaño

```
lsm_processor_csv.py    25 KB  (644 líneas)
README_CSV_SYSTEM.md     6 KB
keyboard_recorder.py     6 KB  (173 líneas)
RESUMEN_CAMBIOS.md       6 KB
MIGRATION_GUIDE.md       7 KB
raspberry_recorder.py    5 KB  (287 líneas)
README.md                7 KB
origen_timestamps.csv   165 B
```

---

## 🔗 Enlaces Rápidos

### Archivos Más Consultados

- [Inicio Rápido](README.md#-inicio-rápido)
- [Formato CSV](README.md#-formato-del-csv)
- [Controles](README.md#-controles)
- [FAQ](README.md#-preguntas-frecuentes)
- [Ejemplos](README_CSV_SYSTEM.md#-ejemplo-de-flujo-completo)

### Código Fuente

- [Grabador GPIO](raspberry_recorder.py)
- [Grabador Teclado](keyboard_recorder.py)
- [Procesador](lsm_processor_csv.py)

---

## 📝 Notas Importantes

⚠️ **Archivos Obsoletos Eliminados:**
- Sistema FSK antiguo (`lsm_processor.py`) - Eliminado
- Scripts de análisis FSK - Eliminados
- Archivos de log de pruebas - Eliminados

✅ **Archivos Actuales:**
- Todo el contenido actual usa el **sistema CSV**
- No hay dependencias de codificación de audio
- 100% compatible con el nuevo flujo de trabajo

---

**Última actualización:** Noviembre 2025
**Versión del sistema:** 2.0 (CSV)
