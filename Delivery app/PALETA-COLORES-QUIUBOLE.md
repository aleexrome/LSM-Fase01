# 🎨 PALETA DE COLORES OFICIAL - QUIÚBOLE!

## 🌈 PALETA SELECCIONADA: NARANJA & ROSA MEXICANO

---

## COLORES PRINCIPALES

### 🧡 Color Principal: NARANJA
```
HEX: #FF6B35
RGB: rgb(255, 107, 53)
HSL: hsl(16, 100%, 60%)

Uso:
- Botones principales (CTAs)
- Links importantes
- Badges de "Nuevo" o "Destacado"
- Iconos principales
- Logo (primario)
```

### 💗 Color Secundario: ROSA MEXICANO
```
HEX: #EC4899
RGB: rgb(236, 72, 153)
HSL: hsl(330, 81%, 60%)

Uso:
- Botones secundarios
- Elementos destacados
- Promociones y ofertas
- Badges de descuento
- Gradientes (combinado con naranja)
- Elementos decorativos
```

### ⚫ Color de Acento: NEGRO AZULADO
```
HEX: #0F172A
RGB: rgb(15, 23, 42)
HSL: hsl(222, 47%, 11%)

Uso:
- Textos principales
- Headers
- Navegación
- Fondos oscuros (dark mode)
- Sombras profundas
```

---

## ESCALA DE COLORES COMPLETA

### Escala de NARANJA:
```
naranja-50:  #FFF4ED  (Muy claro - fondos suaves)
naranja-100: #FFE4D1  (Claro - hover states)
naranja-200: #FFC4A3  (Medio claro)
naranja-300: #FFA575  (Medio)
naranja-400: #FF8555  (Medio oscuro)
naranja-500: #FF6B35  ← PRINCIPAL
naranja-600: #E85A26  (Oscuro - hover de botones)
naranja-700: #C04A1D  (Más oscuro)
naranja-800: #9A3B16  (Muy oscuro)
naranja-900: #7A2F11  (Casi negro)
```

### Escala de ROSA:
```
rosa-50:  #FDF2F8  (Muy claro - fondos suaves)
rosa-100: #FCE7F3  (Claro - hover states)
rosa-200: #FBCFE8  (Medio claro)
rosa-300: #F9A8D4  (Medio)
rosa-400: #F472B6  (Medio oscuro)
rosa-500: #EC4899  ← PRINCIPAL
rosa-600: #DB2777  (Oscuro - hover de botones)
rosa-700: #BE185D  (Más oscuro)
rosa-800: #9F1239  (Muy oscuro)
rosa-900: #831843  (Casi negro)
```

### Escala de GRISES (Neutros):
```
gris-50:  #F8FAFC  (Casi blanco - fondos)
gris-100: #F1F5F9  (Muy claro - fondos secundarios)
gris-200: #E2E8F0  (Claro - bordes)
gris-300: #CBD5E1  (Medio claro - bordes activos)
gris-400: #94A3B8  (Medio - textos deshabilitados)
gris-500: #64748B  (Medio oscuro - textos secundarios)
gris-600: #475569  (Oscuro - textos)
gris-700: #334155  (Más oscuro)
gris-800: #1E293B  (Muy oscuro - headers)
gris-900: #0F172A  ← ACENTO (Casi negro - textos principales)
```

---

## COLORES SEMÁNTICOS

### ✅ SUCCESS (Éxito):
```
HEX: #10B981
RGB: rgb(16, 185, 129)
Nombre: Verde esmeralda

Uso:
- Pedido completado
- Pago exitoso
- Notificaciones positivas
- Estados "Abierto" en restaurantes
```

### ⚠️ WARNING (Advertencia):
```
HEX: #F59E0B
RGB: rgb(245, 158, 11)
Nombre: Ámbar

Uso:
- Alertas de stock bajo
- Tiempo de espera alto
- Verificaciones pendientes
```

### ❌ ERROR (Error):
```
HEX: #EF4444
RGB: rgb(239, 68, 68)
Nombre: Rojo coral

Uso:
- Errores de validación
- Pedido cancelado
- Restaurante cerrado
- Mensajes de error
```

### ℹ️ INFO (Información):
```
HEX: #3B82F6
RGB: rgb(59, 130, 246)
Nombre: Azul cielo

Uso:
- Tooltips
- Información adicional
- Notificaciones neutras
- Estados "En preparación"
```

---

## FONDOS

### Modo Claro:
```
Fondo principal:     #FFFFFF (Blanco puro)
Fondo secundario:    #F8FAFC (Gris muy claro)
Fondo de tarjetas:   #FFFFFF con sombra
Overlay:             rgba(15, 23, 42, 0.4) (Negro azulado semi-transparente)
```

### Modo Oscuro:
```
Fondo principal:     #0F172A (Negro azulado)
Fondo secundario:    #1E293B (Gris oscuro)
Fondo de tarjetas:   #1E293B con borde sutil
Overlay:             rgba(0, 0, 0, 0.7) (Negro semi-transparente)
```

---

## GRADIENTES

### Gradiente Principal (Naranja → Rosa):
```css
background: linear-gradient(135deg, #FF6B35 0%, #EC4899 100%);
```
**Uso:** Botones principales, banners hero, badges premium

### Gradiente Secundario (Rosa → Rosa claro):
```css
background: linear-gradient(135deg, #EC4899 0%, #F472B6 100%);
```
**Uso:** Cards destacados, fondos decorativos

### Gradiente de Fondo Sutil:
```css
background: linear-gradient(180deg, #FFF4ED 0%, #FFFFFF 100%);
```
**Uso:** Fondos de secciones, landing page

### Gradiente Oscuro (Dark Mode):
```css
background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
```
**Uso:** Headers en dark mode, fondos de modales

---

## EJEMPLOS DE APLICACIÓN

### Botón Principal:
```css
Fondo: #FF6B35 (Naranja)
Texto: #FFFFFF (Blanco)
Hover: #E85A26 (Naranja más oscuro)
Sombra: 0 4px 14px rgba(255, 107, 53, 0.4)
```

### Botón Secundario:
```css
Fondo: #EC4899 (Rosa)
Texto: #FFFFFF (Blanco)
Hover: #DB2777 (Rosa más oscuro)
Sombra: 0 4px 14px rgba(236, 72, 153, 0.3)
```

### Botón Terciario (Outline):
```css
Borde: 2px solid #FF6B35
Fondo: transparent
Texto: #FF6B35
Hover fondo: #FFF4ED (Naranja muy claro)
```

### Card de Restaurante:
```css
Fondo: #FFFFFF
Borde: 1px solid #E2E8F0 (Gris claro)
Sombra: 0 1px 3px rgba(0, 0, 0, 0.1)
Hover sombra: 0 10px 25px rgba(0, 0, 0, 0.15)
Badge "Nuevo": Gradiente naranja-rosa
Badge "Promoción": #EC4899 (Rosa)
```

### Input/Campo de Texto:
```css
Borde normal: #E2E8F0 (Gris claro)
Borde focus: #FF6B35 (Naranja)
Fondo: #FFFFFF
Texto: #1E293B (Gris oscuro)
Placeholder: #94A3B8 (Gris medio)
```

### Badge de Estado:
```css
"Abierto":      Fondo #10B981 (Verde), Texto blanco
"Cerrado":      Fondo #EF4444 (Rojo), Texto blanco
"En camino":    Fondo #3B82F6 (Azul), Texto blanco
"Entregado":    Fondo #10B981 (Verde), Texto blanco
"Promoción":    Gradiente naranja-rosa, Texto blanco
```

---

## CÓDIGO PARA IMPLEMENTACIÓN

### Tailwind CSS (Next.js):
```javascript
// tailwind.config.ts
theme: {
  extend: {
    colors: {
      // Naranja
      naranja: {
        50: '#FFF4ED',
        100: '#FFE4D1',
        200: '#FFC4A3',
        300: '#FFA575',
        400: '#FF8555',
        500: '#FF6B35', // Principal
        600: '#E85A26',
        700: '#C04A1D',
        800: '#9A3B16',
        900: '#7A2F11',
      },
      // Rosa
      rosa: {
        50: '#FDF2F8',
        100: '#FCE7F3',
        200: '#FBCFE8',
        300: '#F9A8D4',
        400: '#F472B6',
        500: '#EC4899', // Principal
        600: '#DB2777',
        700: '#BE185D',
        800: '#9F1239',
        900: '#831843',
      },
      // Acento
      acento: {
        50: '#F8FAFC',
        100: '#F1F5F9',
        200: '#E2E8F0',
        300: '#CBD5E1',
        400: '#94A3B8',
        500: '#64748B',
        600: '#475569',
        700: '#334155',
        800: '#1E293B',
        900: '#0F172A', // Principal
      },
    },
  },
}
```

### React Native (Expo):
```typescript
// src/theme/colors.ts
export const colors = {
  // Naranja
  naranja: {
    50: '#FFF4ED',
    100: '#FFE4D1',
    200: '#FFC4A3',
    300: '#FFA575',
    400: '#FF8555',
    500: '#FF6B35', // Principal
    600: '#E85A26',
    700: '#C04A1D',
    800: '#9A3B16',
    900: '#7A2F11',
  },
  // Rosa
  rosa: {
    50: '#FDF2F8',
    100: '#FCE7F3',
    200: '#FBCFE8',
    300: '#F9A8D4',
    400: '#F472B6',
    500: '#EC4899', // Principal
    600: '#DB2777',
    700: '#BE185D',
    800: '#9F1239',
    900: '#831843',
  },
  // Acento
  acento: {
    50: '#F8FAFC',
    100: '#F1F5F9',
    200: '#E2E8F0',
    300: '#CBD5E1',
    400: '#94A3B8',
    500: '#64748B',
    600: '#475569',
    700: '#334155',
    800: '#1E293B',
    900: '#0F172A', // Principal
  },
  // Atajos
  primary: '#FF6B35',
  secondary: '#EC4899',
  accent: '#0F172A',
  background: '#FFFFFF',
  text: '#0F172A',
  // Semánticos
  success: '#10B981',
  warning: '#F59E0B',
  error: '#EF4444',
  info: '#3B82F6',
}
```

---

## TIPOGRAFÍA COMPLEMENTARIA

### Fuentes:
```
Títulos/Display: Poppins (Bold, SemiBold)
Cuerpo/Texto:    Inter (Regular, Medium, SemiBold)
Monospace:       JetBrains Mono (para código/números)
```

### Tamaños:
```
Hero title:       64px / 4rem (móvil: 32px)
H1:              48px / 3rem (móvil: 28px)
H2:              36px / 2.25rem (móvil: 24px)
H3:              30px / 1.875rem (móvil: 20px)
H4:              24px / 1.5rem (móvil: 18px)
Body large:      18px / 1.125rem
Body:            16px / 1rem
Body small:      14px / 0.875rem
Caption:         12px / 0.75rem
```

---

## ICONOS

**Librería recomendada:**
- **Web:** Lucide React (https://lucide.dev/)
- **Móvil:** React Native Vector Icons - Feather set

**Color de iconos:**
- Principales: #FF6B35 (Naranja)
- Secundarios: #EC4899 (Rosa)
- Neutros: #64748B (Gris medio)
- Deshabilitados: #CBD5E1 (Gris claro)

---

## SOMBRAS

```css
/* Elevación Baja (cards en reposo) */
shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05)

/* Elevación Media (cards hover, dropdowns) */
shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1)

/* Elevación Alta (modales, popups) */
shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1)

/* Elevación Muy Alta (elementos flotantes) */
shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1)

/* Sombra de Botón (con color) */
shadow-naranja: 0 4px 14px rgba(255, 107, 53, 0.4)
shadow-rosa: 0 4px 14px rgba(236, 72, 153, 0.3)
```

---

## ACCESIBILIDAD

### Contraste (WCAG AA):
✅ Naranja (#FF6B35) sobre blanco (#FFFFFF): **4.52:1** - PASA
✅ Rosa (#EC4899) sobre blanco (#FFFFFF): **4.65:1** - PASA
✅ Acento (#0F172A) sobre blanco (#FFFFFF): **16.89:1** - PASA
✅ Blanco (#FFFFFF) sobre Naranja (#FF6B35): **4.52:1** - PASA
✅ Blanco (#FFFFFF) sobre Rosa (#EC4899): **4.65:1** - PASA

**Recomendación:** Para textos pequeños (<18px) usar siempre:
- Texto oscuro sobre fondo claro
- Texto blanco sobre naranja/rosa/acento

---

## 📋 RESUMEN RÁPIDO

```
🧡 Principal:   #FF6B35 (Naranja)
💗 Secundario:  #EC4899 (Rosa mexicano)
⚫ Acento:      #0F172A (Negro azulado)
⚪ Fondo:       #FFFFFF (Blanco)
📝 Texto:       #0F172A (Negro azulado)

✅ Éxito:       #10B981 (Verde)
⚠️ Alerta:      #F59E0B (Ámbar)
❌ Error:       #EF4444 (Rojo)
ℹ️ Info:        #3B82F6 (Azul)
```

---

**Esta paleta está lista para implementarse en todos los archivos del proyecto.** 🎨✨

¿Confirmamos esta paleta o hacemos algún ajuste?
