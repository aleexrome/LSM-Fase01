# 🌐 PROMPT COMPLETO: PÁGINA WEB DE DELIVERY "QUIÚBOLE!"

## 🎯 DESCRIPCIÓN GENERAL DEL PROYECTO

Crea una plataforma web moderna, responsiva y de alta performance para **"Quiúbole!"**, una plataforma de delivery multi-negocio. La web debe ser comparable a Rappi Web, Uber Eats Web o DiDi Food Web, con un diseño impactante, animaciones fluidas y experiencia de usuario excepcional.

---

## 🖥️ TIPOS DE PORTALES WEB

El sistema necesita **4 portales web diferentes:**

### 1. PORTAL DE CLIENTES (Público)
- Página principal (landing)
- Explorar restaurantes y negocios
- Hacer pedidos
- Rastrear entregas en tiempo real
- Gestionar cuenta y perfil
- Historial de pedidos
- Pagos y facturación

### 2. PORTAL DE REPARTIDORES
- Dashboard de entregas
- Gestión de disponibilidad
- Historial y ganancias
- Perfil y documentación

### 3. PORTAL DE RESTAURANTES/NEGOCIOS
- Dashboard administrativo
- Gestión de menú y productos
- Pedidos en tiempo real
- Estadísticas de ventas
- Configuración del negocio

### 4. PORTAL DE ADMINISTRADORES
- Dashboard completo con analytics
- Gestión de todos los usuarios
- Monitoreo en tiempo real
- Reportes y métricas
- Configuración de plataforma
- Gestión de comisiones y pagos

---

## 🎨 DISEÑO Y EXPERIENCIA DE USUARIO

### Requisitos Visuales:
- **Diseño responsive:** Perfecto en Desktop (1920px), Laptop (1366px), Tablet (768px), Mobile (375px)
- **Animaciones modernas:** Scroll animations, parallax, hover effects, transiciones suaves
- **Componentes interactivos:** Cards con hover, botones con feedback, loading states
- **Micro-interacciones:** Botones que reaccionan, elementos que se animan al aparecer
- **Glassmorphism y gradientes** en elementos destacados
- **Imágenes optimizadas:** WebP con fallback, lazy loading
- **Modo oscuro y claro**
- **Accesibilidad WCAG 2.1 AA**

### Paleta de Colores (Misma que la app):
```
OPCIÓN 1 (Recomendada - Energética):
- Principal: #FF6B35 (Naranja coral)
- Secundario: #4ECB71 (Verde lima)
- Acento: #1A1A2E (Azul oscuro)
- Fondo: #FFFFFF (Blanco)
- Fondo secundario: #F8F9FA
- Texto: #2D3142 (Gris oscuro)

OPCIÓN 2 (Profesional):
- Principal: #0066FF (Azul eléctrico)
- Secundario: #FFD600 (Amarillo)
- Acento: #2D3142 (Gris)
- Fondo: #F8F9FA (Gris claro)
- Texto: #212529 (Negro)

OPCIÓN 3 (Vibrante):
- Principal: #8B5CF6 (Morado)
- Secundario: #EC4899 (Rosa)
- Acento: #0F172A (Negro azulado)
- Fondo: #FFFFFF (Blanco)
- Texto: #1F2937 (Gris oscuro)
```

### Tipografía:
- **Títulos:** Poppins Bold/Inter Bold (32-72px)
- **Subtítulos:** Poppins SemiBold (24-32px)
- **Cuerpo:** Inter Regular (16-18px)
- **Pequeño:** Inter Regular (14px)
- **Números:** SF Mono/Roboto Mono

---

## 🚀 FUNCIONALIDADES PRINCIPALES

### A. PORTAL DE CLIENTES

#### 🏠 Landing Page (Página Principal)

**Hero Section:**
- Header transparente que se vuelve sólido al hacer scroll
  - Logo "Quiúbole!"
  - Menú: Inicio, Restaurantes, Conviértete en socio, Ayuda
  - Botones: Iniciar sesión, Registrarse
- Hero principal con:
  - Título impactante: "Tu ciudad en delivery"
  - Subtítulo: "Comida, compras y más en minutos"
  - Barra de búsqueda grande con autocompletado
  - Input de dirección con geolocalización
  - Imagen/ilustración atractiva o video de fondo
  - CTA prominente: "Explorar restaurantes"

**Sección "¿Cómo funciona?":**
- 3-4 pasos visuales con iconos animados
  1. Elige tu restaurante favorito
  2. Selecciona lo que quieres
  3. Paga de forma segura
  4. Recibe en minutos
- Animación al hacer scroll

**Sección "Categorías":**
- Grid de categorías con iconos grandes y coloridos
- Hover effects atractivos
- Categorías: Restaurantes, Supermercado, Farmacia, Mascotas, Flores, Licores, etc.

**Sección "Restaurantes Destacados":**
- Carrusel horizontal infinito
- Cards de restaurantes con:
  - Imagen grande
  - Logo del restaurante
  - Nombre
  - Calificación (estrellas)
  - Tiempo de entrega
  - Costo de envío
  - Etiquetas (Promoción, Nuevo, Gratis envío)
- Hover effect: elevación y scale

**Sección "Promociones":**
- Banner grande con ofertas destacadas
- Countdown timer para ofertas limitadas
- CTA atractivo

**Sección "Para Negocios":**
- Subtítulo: "¿Tienes un negocio?"
- Texto: "Únete a Quiúbole! y llega a más clientes"
- CTA: "Conviértete en socio"
- Imagen de comerciantes felices

**Sección "Para Repartidores":**
- Subtítulo: "Gana dinero entregando"
- Texto: "Horarios flexibles, pagos semanales"
- CTA: "Únete como repartidor"
- Imagen de repartidor

**Sección "Descarga la App":**
- "Lleva Quiúbole! a todas partes"
- Botones: App Store, Google Play
- Mockup del celular con la app

**Footer:**
- Logo
- Links: Sobre nosotros, Términos, Privacidad, Contacto
- Redes sociales
- Newsletter signup
- Copyright

---

#### 🔐 Registro y Login

**Página de Registro:**
- Formulario limpio y moderno
- Campos:
  - Nombre completo
  - Email (con validación en tiempo real)
  - Teléfono
  - Contraseña (con indicador de fortaleza)
  - Confirmar contraseña
  - Checkbox: Acepto términos y condiciones
- Botón de registro grande
- Divider: "O regístrate con"
- Botones sociales: Google, Facebook
- Link: "¿Ya tienes cuenta? Inicia sesión"

**Página de Login:**
- Formulario simple
- Email y contraseña
- Checkbox: "Recordarme"
- Link: "¿Olvidaste tu contraseña?"
- Botón de login grande
- Login con redes sociales
- Link: "¿No tienes cuenta? Regístrate"

---

#### 🍽️ Exploración de Restaurantes

**Página de Restaurantes:**
- Header sticky:
  - Barra de búsqueda
  - Ubicación actual (editable)
  - Carrito (badge con cantidad)
  - Perfil usuario

- Sidebar izquierdo (filtros):
  - Categorías (checkboxes)
  - Precio ($ - $$$$)
  - Calificación (4+ estrellas, etc.)
  - Tiempo de entrega (< 30min, < 60min)
  - Opciones especiales:
    * Envío gratis
    * Ofertas
    * Abierto ahora
    * Vegetariano
    * Sin gluten
  - Botón: "Limpiar filtros"

- Contenido principal:
  - Breadcrumb: Inicio > Restaurantes
  - Título: "Restaurantes en [ubicación]"
  - Ordenar por: Recomendados, Más cercanos, Mejor calificados, Menor tiempo, A-Z
  - Grid de restaurantes (3-4 columnas en desktop)
    * Card con imagen grande
    * Badge de estado (Abierto/Cerrado)
    * Logo circular sobre la imagen
    * Nombre del restaurante
    * Categoría (Italiana, Mexicana, etc.)
    * Calificación + número de reseñas
    * Tiempo estimado
    * Costo de envío (o "Envío gratis")
    * Etiqueta de promoción si aplica
    * Hover: Shadow elevation
  - Paginación o infinite scroll

---

#### 🍕 Detalle de Restaurante

**Header del Restaurante:**
- Banner grande con foto del restaurante
- Overlay con gradiente
- Botón atrás (top left)
- Info del restaurante sobre la foto:
  - Logo grande
  - Nombre
  - Categoría
  - Calificación (con estrellas grandes) + link "Ver reseñas"
  - Dirección
  - Estado: Abierto/Cerrado + horarios

**Información Rápida (sticky bar):**
- Tiempo estimado de entrega
- Costo de envío
- Pedido mínimo
- Calificación
- Botón: "Ver carrito"

**Navegación Tabs:**
- Menú (default)
- Información
- Reseñas

**Tab "Menú":**
- Sidebar izquierdo con categorías del menú (sticky)
  - Al click, scroll suave a la categoría
  - Indicador activo según scroll

- Contenido principal:
  - Buscador interno: "Buscar en el menú"
  - Si hay promociones: Banner destacado

  - Por cada categoría:
    * Título de categoría
    * Grid de productos (2 columnas en desktop)
    * Cada producto:
      - Imagen (cuadrada)
      - Nombre
      - Descripción breve
      - Precio
      - Badge si hay descuento
      - Botón "+" (agregar rápido) o click para ver detalle

**Modal de Producto:**
- Se abre al hacer click en un producto
- Imagen grande
- Nombre y descripción completa
- Precio
- Sección "Personaliza tu orden":
  - Modificadores (radio buttons):
    * Ejemplo: Tamaño (Chico, Mediano, Grande)
  - Extras (checkboxes con precio):
    * Ejemplo: + Queso extra ($10)
    * Ejemplo: + Aguacate ($15)
- Instrucciones especiales (textarea)
- Selector de cantidad (- 1 +)
- Precio total calculado en tiempo real
- Botón grande: "Agregar al carrito $XX"
- Botón: "Cancelar"

**Tab "Información":**
- Horarios de atención
- Dirección completa
- Teléfono
- Mapa embebido (Google Maps)
- Método de pago aceptados
- Tiempo promedio de preparación

**Tab "Reseñas":**
- Resumen:
  - Calificación promedio grande (4.5/5)
  - Barras con distribución (5★: 80%, 4★: 15%, etc.)
  - Total de reseñas
- Filtros: Más recientes, Más útiles, Positivas, Negativas
- Lista de reseñas:
  - Foto y nombre del usuario
  - Calificación (estrellas)
  - Fecha
  - Comentario
  - Fotos de la comida (si hay)
  - Respuesta del restaurante (si hay)
  - Botones: Útil (👍 contador)

---

#### 🛒 Carrito de Compras

**Sidebar derecho (o página completa en mobile):**
- Header: "Tu pedido en [Nombre Restaurante]"
- Lista de productos:
  - Miniatura
  - Nombre + modificadores
  - Precio unitario
  - Selector de cantidad
  - Botón eliminar
  - Subtotal por producto

- Subtotal de productos
- Costo de envío
- Descuentos aplicados
- Campo: "Código de cupón" con botón "Aplicar"
- Propina sugerida:
  - Botones: $0, 10%, 15%, 20%
  - Input custom
- Total (grande y destacado)

- Botón grande: "Continuar a pagar"
- Link: "Agregar más productos"

---

#### 💳 Checkout

**Página dividida en 2 columnas:**

**Columna Izquierda (Formulario):**

1. **Dirección de entrega:**
   - Selector de direcciones guardadas
   - O agregar nueva dirección:
     * Calle y número
     * Colonia
     * Referencias
     * Indicaciones especiales
   - Mapa interactivo para confirmar ubicación
   - Botón: "Guardar dirección"

2. **Método de pago:**
   - Tarjetas guardadas (radio buttons)
   - O agregar nueva tarjeta:
     * Número de tarjeta (con validación)
     * Nombre
     * Fecha de expiración
     * CVV
     * Checkbox: "Guardar tarjeta"
   - Opción: "Efectivo"
   - Logos de tarjetas aceptadas

3. **Información adicional:**
   - Teléfono de contacto
   - Instrucciones de entrega (textarea)
   - Checkbox: "Dejar en la puerta"
   - Checkbox: "Recibir factura"

**Columna Derecha (Resumen):**
- Resumen del pedido (sticky)
- Productos (lista resumida)
- Restaurante
- Dirección de entrega
- Subtotal
- Envío
- Descuentos
- Propina
- **Total**
- Tiempo estimado de entrega
- Botón grande: "Realizar pedido"
- Texto pequeño: "Al realizar el pedido aceptas los términos"

---

#### 📍 Seguimiento en Tiempo Real

**Pantalla completa dividida:**

**Sección Superior (Mapa - 60%):**
- Mapa de Google Maps fullscreen
- Marcadores:
  - Pin del restaurante
  - Pin de tu ubicación (destino)
  - Marcador del repartidor (actualizado cada 5 seg)
- Ruta dibujada entre puntos
- Botón: "Centrar mapa"

**Sección Inferior (Info - 40%):**

- **Stepper horizontal con estados:**
  1. ✓ Pedido confirmado (completado)
  2. ⏱ En preparación (activo)
  3. ⭕ Repartidor en camino
  4. ⭕ Entregado

- **Card del Repartidor:**
  - Foto circular grande
  - Nombre
  - Calificación (★ 4.8)
  - Vehículo y placas
  - Botones:
    * 💬 Chat
    * 📞 Llamar

- **Detalles del Pedido:**
  - Tiempo estimado (grande): "Llega en 15 min"
  - Dirección de entrega
  - Resumen de productos (collapsible)
  - Total pagado

- **Botón:** "Ayuda / Reportar problema"

**Notificaciones en tiempo real:**
- Toast notifications cuando cambia el estado
- Sonido opcional

---

#### ✅ Pedido Completado

**Pantalla de éxito:**
- Icono grande de check animado
- "¡Tu pedido ha sido entregado!"
- Resumen del pedido
- Total pagado

**Sección de Calificación:**
- "¿Cómo estuvo tu experiencia?"
- **Calificar Restaurante:**
  - 5 estrellas interactivas
  - Textarea: "Cuéntanos sobre la comida"
  - Subir fotos (opcional)
- **Calificar Repartidor:**
  - 5 estrellas interactivas
  - Textarea: "Cuéntanos sobre la entrega"
- Botón: "Enviar calificación"

**Problemas:**
- Link: "¿Algo salió mal? Reportar un problema"

**Acciones:**
- Botón: "Ver detalles del pedido"
- Botón: "Reordenar"
- Botón: "Volver al inicio"

---

#### 📦 Historial de Pedidos

**Página completa:**
- Título: "Mis pedidos"
- Tabs/Filtros: Todos, En curso, Completados, Cancelados

**Lista de pedidos:**
- Cards por pedido:
  - Foto del restaurante
  - Nombre del restaurante
  - Fecha y hora
  - Estado con badge de color
  - Lista resumida de productos
  - Total
  - Botones:
    * "Ver detalles"
    * "Reordenar"
    * "Ayuda" (si aplica)
- Paginación

**Detalle de pedido (modal o página):**
- Toda la información completa:
  - Número de orden
  - Estado
  - Fecha y hora
  - Restaurante
  - Productos con precios
  - Subtotal, envío, descuentos, propina, total
  - Método de pago
  - Dirección de entrega
  - Repartidor (nombre y foto)
  - Calificaciones (si ya se dio)
- Botones:
  - "Reordenar"
  - "Descargar factura"
  - "Ayuda"

---

#### 👤 Perfil de Usuario

**Layout con sidebar:**

**Sidebar Izquierdo (Menú):**
- Foto de perfil + nombre
- Opciones:
  - 👤 Mi perfil
  - 📍 Mis direcciones
  - 💳 Métodos de pago
  - 🎫 Cupones
  - 📦 Historial de pedidos
  - ⭐ Mis reseñas
  - ❤️ Favoritos
  - 🔔 Notificaciones
  - 🌙 Modo oscuro
  - 🆘 Ayuda y soporte
  - 📄 Términos y privacidad
  - 🚪 Cerrar sesión

**Contenido Principal (cambia según selección):**

**Mi Perfil:**
- Formulario editable:
  - Foto de perfil (con opción de cambiar)
  - Nombre completo
  - Email (no editable)
  - Teléfono
  - Fecha de nacimiento
  - Género
- Botón: "Guardar cambios"
- Link: "Cambiar contraseña"

**Mis Direcciones:**
- Lista de direcciones guardadas
- Cards por dirección:
  - Etiqueta (Casa, Trabajo, etc.)
  - Dirección completa
  - Checkbox: "Dirección predeterminada"
  - Botones: Editar, Eliminar
- Botón: "+ Agregar nueva dirección"

**Métodos de Pago:**
- Lista de tarjetas guardadas
- Cards:
  - Logo de la tarjeta
  - •••• •••• •••• 1234
  - Nombre
  - Expira: 12/25
  - Badge: "Predeterminada"
  - Botones: Editar, Eliminar
- Botón: "+ Agregar nueva tarjeta"

**Cupones:**
- Lista de cupones disponibles y usados
- Card de cupón:
  - Código
  - Descripción: "20% de descuento"
  - Válido hasta: fecha
  - Botón: "Copiar código"
- Si no hay: "No tienes cupones disponibles"

**Favoritos:**
- Grid de restaurantes favoritos
- Mismo diseño que cards de restaurantes
- Botón: "Explorar más restaurantes"

**Notificaciones:**
- Switches para activar/desactivar:
  - Pedidos y entregas
  - Promociones
  - Nuevos restaurantes
  - Noticias de Quiúbole!
  - Email
  - Push notifications
  - SMS

---

### B. PORTAL DE REPARTIDORES

**Dashboard Principal:**
- Toggle grande: "Disponible / No disponible"
- Métricas del día:
  - Entregas completadas
  - Ganancias del día
  - Tiempo en línea
  - Calificación promedio

**Pedidos Disponibles:**
- Lista de pedidos para aceptar
- Card de pedido:
  - Restaurante
  - Distancia total
  - Ganancia estimada
  - Tiempo estimado
  - Mapa pequeño con ruta
  - Botón: "Aceptar"
- Temporizador para aceptar

**Pedido Activo:**
- Mapa con navegación
- Información del pedido
- Botones según estado:
  - "Llegué al restaurante"
  - "Pedido recogido"
  - "Pedido entregado"
- Info del cliente (sin datos sensibles)
- Chat y llamada

**Historial y Ganancias:**
- Resumen semanal/mensual
- Lista de entregas
- Detalles de pagos
- Propinas recibidas

**Perfil:**
- Datos personales
- Documentos (licencia, INE)
- Vehículo
- Métodos de pago para recibir

---

### C. PORTAL DE RESTAURANTES/NEGOCIOS

**Dashboard:**
- Resumen del día:
  - Pedidos
  - Ventas
  - Productos más vendidos
  - Calificación promedio
- Gráficas de ventas

**Pedidos en Tiempo Real:**
- Lista de pedidos entrantes
- Card de pedido:
  - Número de orden
  - Productos
  - Total
  - Dirección de entrega
  - Tiempo desde que se ordenó
  - Botones:
    * "Aceptar"
    * "Rechazar"
- Pedidos en preparación
- Pedidos listos para recoger

**Gestión de Menú:**
- Lista de categorías
- CRUD de productos:
  - Agregar/editar/eliminar
  - Subir fotos
  - Nombre, descripción, precio
  - Modificadores y extras
  - Disponibilidad
  - Stock

**Promociones:**
- Crear descuentos
- Productos en oferta
- Cupones exclusivos

**Analytics:**
- Gráficas de ventas por periodo
- Productos más/menos vendidos
- Horarios pico
- Calificaciones y reseñas

**Configuración:**
- Información del negocio
- Horarios de operación
- Tiempo de preparación promedio
- Métodos de pago aceptados
- Fotos del local

---

### D. PORTAL DE ADMINISTRADORES

**Dashboard General:**
- Métricas principales (KPIs):
  - Pedidos del día
  - Ventas totales
  - Usuarios activos
  - Repartidores en línea
  - Restaurantes activos
- Gráficas interactivas:
  - Ventas por periodo
  - Pedidos por categoría
  - Crecimiento de usuarios
  - Mapa de calor de entregas

**Gestión de Usuarios:**
- Tabs: Clientes, Repartidores, Restaurantes
- Tabla con búsqueda y filtros:
  - Nombre
  - Email
  - Teléfono
  - Fecha de registro
  - Estado (Activo/Bloqueado)
  - Acciones: Ver, Editar, Bloquear, Eliminar

**Pedidos en Tiempo Real:**
- Mapa con todos los pedidos activos
- Lista de pedidos en curso
- Filtros por estado
- Detalle completo de cada pedido
- Acciones: Cancelar, Reasignar repartidor, Reembolsar

**Reportes:**
- Exportar datos (CSV, Excel, PDF)
- Reportes personalizados
- Gráficas avanzadas
- Análisis de tendencias

**Configuración de Plataforma:**
- Comisiones:
  - % por pedido
  - % para repartidores
  - Costo de envío base
- Promociones globales
- Notificaciones masivas
- Términos y políticas
- Configuración de pagos

**Verificación:**
- Lista de solicitudes pendientes:
  - Nuevos restaurantes
  - Nuevos repartidores
- Verificar documentos
- Aprobar/rechazar

**Soporte:**
- Tickets de soporte
- Chat en vivo
- Historial de conversaciones
- Reembolsos y cancelaciones

---

## 🛠️ STACK TECNOLÓGICO RECOMENDADO

### Frontend:
```
- Framework: Next.js 14 (React con SSR/SSG)
- Lenguaje: TypeScript
- UI Library: Tailwind CSS + shadcn/ui
- Animaciones: Framer Motion
- Mapas: Google Maps API + @react-google-maps/api
- Estado Global: Zustand o Redux Toolkit
- Formularios: React Hook Form + Zod
- Tablas: TanStack Table (React Table v8)
- Gráficas: Recharts o Chart.js
- Notificaciones: React Hot Toast
- Iconos: Lucide React o Heroicons
```

### Backend (Compartido con la app):
```
- Backend: Node.js + Nest.js (TypeScript)
- Base de datos: PostgreSQL
- ORM: Prisma
- Realtime: Socket.io o Firebase Realtime Database
- API: REST + GraphQL (Apollo)
- Autenticación: JWT + Refresh Tokens
- Storage: AWS S3 / Cloudinary
```

### Servicios de Terceros:
```
- Mapas: Google Maps Platform
- Pagos: Stripe / Conekta
- Email: SendGrid / Resend
- SMS: Twilio
- Analytics: Google Analytics 4 + Mixpanel
- Error tracking: Sentry
- CDN: Cloudflare
```

### DevOps:
```
- Hosting: Vercel (Next.js) o AWS
- CI/CD: GitHub Actions
- Monitoreo: Vercel Analytics
- Testing: Jest + React Testing Library + Playwright
```

---

## 📐 ARQUITECTURA DE CÓDIGO

### Estructura de Carpetas (Next.js 14 con App Router):
```
quiubole-web/
├── app/
│   ├── (auth)/
│   │   ├── login/
│   │   │   └── page.tsx
│   │   ├── register/
│   │   │   └── page.tsx
│   │   └── layout.tsx
│   ├── (customer)/
│   │   ├── restaurants/
│   │   │   ├── [id]/
│   │   │   │   └── page.tsx
│   │   │   └── page.tsx
│   │   ├── cart/
│   │   │   └── page.tsx
│   │   ├── checkout/
│   │   │   └── page.tsx
│   │   ├── tracking/
│   │   │   └── [orderId]/
│   │   │       └── page.tsx
│   │   ├── orders/
│   │   │   └── page.tsx
│   │   ├── profile/
│   │   │   └── page.tsx
│   │   └── layout.tsx
│   ├── (driver)/
│   │   └── dashboard/
│   │       └── page.tsx
│   ├── (merchant)/
│   │   └── dashboard/
│   │       └── page.tsx
│   ├── (admin)/
│   │   └── dashboard/
│   │       └── page.tsx
│   ├── page.tsx              # Landing page
│   ├── layout.tsx            # Root layout
│   ├── globals.css
│   └── api/                  # API routes
│       └── [...]/
├── components/
│   ├── ui/                   # shadcn/ui components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── input.tsx
│   │   └── ...
│   ├── layout/
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   ├── Sidebar.tsx
│   │   └── MobileNav.tsx
│   ├── restaurant/
│   │   ├── RestaurantCard.tsx
│   │   ├── RestaurantGrid.tsx
│   │   ├── MenuCategory.tsx
│   │   └── ProductCard.tsx
│   ├── cart/
│   │   ├── CartSidebar.tsx
│   │   ├── CartItem.tsx
│   │   └── CartSummary.tsx
│   ├── order/
│   │   ├── OrderTracking.tsx
│   │   ├── OrderMap.tsx
│   │   └── OrderStatus.tsx
│   └── common/
│       ├── Loading.tsx
│       ├── ErrorBoundary.tsx
│       └── Modal.tsx
├── lib/
│   ├── api/                  # API client
│   │   ├── restaurants.ts
│   │   ├── orders.ts
│   │   ├── auth.ts
│   │   └── payments.ts
│   ├── hooks/
│   │   ├── useAuth.ts
│   │   ├── useCart.ts
│   │   ├── useOrders.ts
│   │   └── useGeolocation.ts
│   ├── store/                # Zustand store
│   │   ├── auth.ts
│   │   ├── cart.ts
│   │   └── ui.ts
│   ├── utils/
│   │   ├── formatters.ts
│   │   ├── validators.ts
│   │   └── constants.ts
│   └── types/
│       ├── models.ts
│       └── api.ts
├── public/
│   ├── images/
│   ├── icons/
│   └── fonts/
├── styles/
│   └── globals.css
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── next.config.js
```

---

## 🎯 REQUERIMIENTOS TÉCNICOS

### Performance:
- **First Contentful Paint:** < 1.5s
- **Time to Interactive:** < 3.5s
- **Lighthouse Score:** > 90
- **Core Web Vitals:**
  - LCP < 2.5s
  - FID < 100ms
  - CLS < 0.1

### SEO:
- Meta tags optimizados
- Open Graph tags
- Schema.org markup (LocalBusiness, Restaurant)
- Sitemap.xml
- robots.txt
- URLs amigables

### Accesibilidad:
- ARIA labels
- Navegación por teclado
- Contraste WCAG AA
- Screen reader friendly
- Focus states visibles

### Seguridad:
- HTTPS obligatorio
- Headers de seguridad (CSP, HSTS)
- CORS configurado
- Rate limiting
- Sanitización de inputs
- Protección XSS y CSRF

### Responsive:
- Mobile first approach
- Breakpoints:
  - sm: 640px
  - md: 768px
  - lg: 1024px
  - xl: 1280px
  - 2xl: 1536px

---

## 🚀 PROMPT LISTO PARA USAR

```
Necesito que crees una plataforma web profesional llamada "Quiúbole!"
para un sistema de delivery multi-negocio tipo Rappi/Uber Eats.

REQUERIMIENTOS:

1. TIPOS DE PORTALES (4 en total):
   - Portal para Clientes (público, ordenar comida/productos)
   - Portal para Repartidores (gestión de entregas)
   - Portal para Negocios/Restaurantes (gestión de pedidos)
   - Portal para Administradores (gestión completa de plataforma)

2. FUNCIONALIDADES PRINCIPALES:
   - Landing page impactante con animaciones
   - Exploración de restaurantes con filtros avanzados
   - Sistema de pedidos completo
   - Rastreo en tiempo real con Google Maps
   - Checkout con múltiples métodos de pago
   - Sistema de calificaciones y reseñas
   - Dashboards con analytics y gráficas
   - Gestión completa de menús y productos
   - Chat en tiempo real

3. TECNOLOGÍAS A USAR:
   - Next.js 14 (App Router) + TypeScript
   - Tailwind CSS + shadcn/ui
   - Framer Motion (animaciones)
   - Zustand (estado global)
   - React Hook Form + Zod (formularios)
   - Google Maps API
   - Socket.io (tiempo real)
   - Recharts (gráficas)

4. DISEÑO:
   - Moderno, limpio y profesional
   - Completamente responsive (mobile-first)
   - Paleta: Naranja coral (#FF6B35) principal,
     Verde lima (#4ECB71) secundario, Azul oscuro (#1A1A2E) acento
   - Animaciones fluidas con Framer Motion
   - Micro-interacciones en botones y cards
   - Modo claro y oscuro
   - Glassmorphism en elementos destacados
   - Tipografía: Poppins para títulos, Inter para cuerpo

5. PÁGINAS PRINCIPALES (CLIENTES):

   A) Landing Page:
      - Hero con título impactante, búsqueda y CTA
      - Sección "Cómo funciona" (4 pasos con iconos)
      - Grid de categorías con hover effects
      - Carrusel de restaurantes destacados
      - Sección de promociones
      - Secciones para negocios y repartidores
      - Footer completo

   B) Exploración:
      - Header sticky con búsqueda, ubicación, carrito
      - Sidebar con filtros (categorías, precio, calificación, tiempo)
      - Grid responsive de restaurantes
      - Infinite scroll o paginación

   C) Detalle de Restaurante:
      - Banner grande con foto
      - Tabs: Menú, Info, Reseñas
      - Menú con categorías sticky sidebar
      - Modal de producto con personalización
      - Carrito flotante

   D) Checkout:
      - 2 columnas: formulario + resumen
      - Dirección con mapa interactivo
      - Múltiples métodos de pago
      - Resumen sticky

   E) Rastreo en Tiempo Real:
      - Mapa fullscreen con marcadores
      - Info del pedido y repartidor
      - Stepper de estados
      - Actualización cada 5 segundos

   F) Perfil:
      - Sidebar con menú
      - Secciones: perfil, direcciones, pagos, cupones,
        historial, reseñas, favoritos, notificaciones

6. PORTALES ADICIONALES:

   - REPARTIDORES: Dashboard con toggle disponibilidad, lista de
     pedidos, mapa con navegación, historial de ganancias

   - NEGOCIOS: Dashboard con métricas, gestión de pedidos en tiempo
     real, CRUD de menú, analytics, configuración

   - ADMIN: Dashboard con KPIs, gestión de usuarios, monitoreo de
     pedidos, reportes, configuración de comisiones, soporte

7. FEATURES TÉCNICOS:
   - SSR/SSG con Next.js 14
   - Optimización de imágenes (WebP, lazy loading)
   - Core Web Vitals optimizados
   - SEO completo (meta tags, schema.org)
   - Accesibilidad WCAG 2.1 AA
   - TypeScript estricto
   - Componentes reutilizables
   - API con validación (Zod)

8. INTEGRACIONES:
   - Google Maps (mapas, direcciones, places)
   - Stripe (pagos)
   - Socket.io (tiempo real)
   - Cloudinary (imágenes)
   - SendGrid (emails)

POR FAVOR:
- Genera código limpio, TypeScript estricto
- Componentes pequeños y reutilizables
- Animaciones fluidas y performantes
- Responsive perfecto en todos los breakpoints
- Manejo de errores robusto
- Loading states en toda la app
- Validaciones en formularios

COMIENZA CON:
1. Setup de Next.js 14 + TypeScript + Tailwind
2. Configuración de shadcn/ui
3. Estructura de carpetas completa
4. Theme provider (dark/light mode)
5. Landing page con hero y secciones principales
6. Sistema de navegación
7. Páginas de auth (login/register)
8. Página de exploración de restaurantes

¿Puedes comenzar con la configuración inicial y crear la landing page?
```

---

## 📊 MÉTRICAS DE ÉXITO

La plataforma web estará completa cuando:
- ✅ Los 4 portales funcionen completamente
- ✅ Lighthouse Score > 90
- ✅ Diseño responsive perfecto en todos los dispositivos
- ✅ Animaciones fluidas (60fps)
- ✅ Rastreo en tiempo real funcionando
- ✅ Pagos integrados correctamente
- ✅ SEO optimizado
- ✅ Accesibilidad WCAG AA
- ✅ Tests pasando
- ✅ Documentación básica

---

## 🎯 FASES DE DESARROLLO

### Fase 1 (MVP):
1. Landing page
2. Auth (login/register)
3. Exploración de restaurantes
4. Detalle y menú
5. Carrito y checkout básico
6. Rastreo simple

### Fase 2:
1. Perfiles completos
2. Historial de pedidos
3. Calificaciones y reseñas
4. Portal de repartidores
5. Portal de negocios básico

### Fase 3:
1. Portal de admin completo
2. Analytics avanzados
3. Sistema de cupones
4. Chat en tiempo real
5. Notificaciones push
6. Dashboard avanzado con gráficas

---

## 💡 MEJORES PRÁCTICAS

### Performance:
- Lazy load de imágenes
- Code splitting por ruta
- Prefetch de páginas críticas
- Caché estratégico
- Minimizar bundle size
- Usar WebP para imágenes

### UX:
- Feedback inmediato en acciones
- Loading states informativos
- Mensajes de error claros
- Confirmaciones antes de acciones destructivas
- Atajos de teclado
- Búsqueda instantánea

### Desarrollo:
- Commits atómicos
- Nombres descriptivos
- Comentarios en lógica compleja
- Tests para funciones críticas
- PR reviews
- Changelog actualizado

---

**¡Éxito con tu plataforma web Quiúbole!** 🌐🚀
