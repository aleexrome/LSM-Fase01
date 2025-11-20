# 🚀 Quiúbole! - Plataforma de Delivery Multi-Negocio

Documentación completa para crear una plataforma de delivery profesional tipo Rappi, Uber Eats o DiDi Food.

## 📱 ¿Qué incluye este proyecto?

Este repositorio contiene toda la documentación y prompts necesarios para desarrollar **Quiúbole!**, una plataforma completa de delivery que conecta clientes, repartidores, negocios y administradores.

---

## 📄 Archivos Principales

### 1. 🎨 **PALETA-COLORES-QUIUBOLE.md**
Paleta de colores oficial de la marca:
- **Principal:** Naranja (#FF6B35) 🧡
- **Secundario:** Rosa Mexicano (#EC4899) 💗
- **Acento:** Negro Azulado (#0F172A) ⚫

Incluye:
- Escalas completas de colores
- Gradientes listos para usar
- Código para Tailwind CSS y React Native
- Ejemplos de aplicación
- Verificación de accesibilidad WCAG AA

---

### 2. 📱 **prompt-app-movil-delivery.md**
Prompt completo para crear la **aplicación móvil híbrida** (iOS + Android).

**Stack Tecnológico:**
- React Native + TypeScript
- Expo (desarrollo rápido)
- Redux Toolkit / Zustand (estado)
- React Navigation 6
- Firebase (tiempo real)
- Google Maps API
- Stripe (pagos)

**Incluye 4 aplicaciones:**
1. **App de Clientes** - Ordenar comida/productos
2. **App de Repartidores** - Gestionar entregas
3. **App de Negocios** - Recibir y gestionar pedidos
4. **App de Administradores** - Panel de control completo

**Funcionalidades principales:**
- ✅ Exploración de restaurantes con filtros
- ✅ Carrito de compras y checkout
- ✅ Rastreo en tiempo real con GPS
- ✅ Pagos en línea y efectivo
- ✅ Sistema de calificaciones
- ✅ Notificaciones push
- ✅ Chat en tiempo real

---

### 3. 🌐 **prompt-web-delivery.md**
Prompt completo para crear la **plataforma web** responsiva.

**Stack Tecnológico:**
- Next.js 14 (App Router) + TypeScript
- Tailwind CSS + shadcn/ui
- Framer Motion (animaciones)
- Zustand (estado)
- React Hook Form + Zod
- Recharts (gráficas)
- Google Maps API

**Incluye 4 portales:**
1. **Portal de Clientes** - Landing page + exploración + pedidos
2. **Portal de Repartidores** - Dashboard de entregas
3. **Portal de Negocios** - Gestión de menú y pedidos
4. **Portal Admin** - Dashboard con analytics completo

**Características destacadas:**
- 🎨 Diseño moderno con animaciones fluidas
- 📱 Completamente responsive (mobile-first)
- ⚡ Performance optimizado (Lighthouse > 90)
- ♿ Accesibilidad WCAG 2.1 AA
- 🔍 SEO optimizado

---

### 4. 🛠️ **GUIA-INSTALACION-QUIUBOLE.md**
Guía paso a paso para configurar todo el entorno de desarrollo.

**Software necesario:**
- Node.js (✅ Obligatorio)
- Git (✅ Obligatorio)
- Visual Studio Code (✅ Obligatorio)
- Expo CLI / Android Studio (para móvil)
- PostgreSQL (base de datos)
- Docker (opcional)

**Incluye:**
- Links directos de descarga
- Instrucciones de instalación detalladas
- Configuración de variables de entorno
- Comandos para crear proyectos
- Extensiones recomendadas de VS Code
- Solución de problemas comunes

---

## 🚀 ¿Cómo empezar?

### Paso 1: Instalar Software
Abre `GUIA-INSTALACION-QUIUBOLE.md` y sigue las instrucciones para instalar:
- Node.js
- Git
- VS Code
- Y demás herramientas necesarias

### Paso 2: Crear Proyectos Base
Ejecuta los comandos de la guía para crear:

```bash
# App móvil
npx create-expo-app quiubole-app --template blank-typescript

# Plataforma web
npx create-next-app@latest quiubole-web --typescript --tailwind

# Backend (opcional)
nest new quiubole-backend
```

### Paso 3: Usar los Prompts
1. Abre `prompt-app-movil-delivery.md` o `prompt-web-delivery.md`
2. Copia el prompt completo (está al final del archivo)
3. Pégalo en tu IA favorita:
   - Claude
   - ChatGPT
   - Cursor
   - GitHub Copilot
4. ¡Empieza a desarrollar!

---

## 🎯 Funcionalidades del Sistema

### Para Clientes:
- Explorar restaurantes y negocios cercanos
- Buscar productos con filtros avanzados
- Agregar al carrito y personalizar productos
- Métodos de pago múltiples (tarjeta, efectivo, PayPal)
- Rastrear pedido en tiempo real en mapa
- Calificar restaurantes y repartidores
- Historial de pedidos y reordenar
- Cupones y promociones

### Para Repartidores:
- Activar/desactivar disponibilidad
- Recibir pedidos cercanos
- Navegación GPS integrada
- Confirmar recogida y entrega
- Historial de entregas y ganancias
- Chat con clientes y restaurantes

### Para Negocios/Restaurantes:
- Gestionar menú completo (CRUD)
- Recibir pedidos en tiempo real
- Aceptar/rechazar pedidos
- Notificar cuando el pedido está listo
- Ver estadísticas y reportes de ventas
- Gestionar horarios y disponibilidad

### Para Administradores:
- Dashboard con métricas en tiempo real
- Gestionar usuarios (clientes, repartidores, negocios)
- Monitorear todos los pedidos activos
- Reportes y analytics avanzados
- Configurar comisiones y promociones
- Sistema de soporte y tickets

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                    CLIENTES (Apps/Web)                      │
│  iOS App  │  Android App  │  Web Desktop  │  Web Mobile    │
└─────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      API REST + WebSockets                  │
│              (Node.js + Nest.js + TypeScript)               │
└─────────────────────────────────────────────────────────────┘
                              ▼
┌──────────────────┬──────────────────┬──────────────────────┐
│   PostgreSQL     │   Firebase       │   Redis Cache        │
│ (Base de datos)  │ (Tiempo real)    │ (Sesiones)          │
└──────────────────┴──────────────────┴──────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    SERVICIOS EXTERNOS                       │
│  Google Maps │ Stripe │ Cloudinary │ Twilio │ SendGrid    │
└─────────────────────────────────────────────────────────────┘
```

---

## 💡 Tecnologías Utilizadas

### Frontend Móvil:
- React Native
- TypeScript
- Expo
- React Navigation
- Redux Toolkit / Zustand
- React Native Paper
- React Native Reanimated

### Frontend Web:
- Next.js 14
- TypeScript
- Tailwind CSS
- shadcn/ui
- Framer Motion
- React Hook Form
- Recharts

### Backend:
- Node.js
- Nest.js
- TypeScript
- Prisma ORM
- PostgreSQL
- Socket.io
- JWT Authentication

### Servicios:
- Google Maps Platform
- Stripe / Conekta
- Firebase
- Cloudinary
- Twilio
- SendGrid

---

## 📱 Capturas de Pantalla (Mockups)

### App Móvil:
- Landing con onboarding
- Home con restaurantes destacados
- Menú de restaurante con productos
- Carrito de compras
- Rastreo en tiempo real con mapa
- Perfil de usuario

### Web:
- Landing page impactante
- Exploración de restaurantes
- Checkout fluido
- Dashboard de administrador
- Panel de repartidor
- Gestión de menú para negocios

---

## 🎨 Diseño

**Paleta de colores:**
- Naranja (#FF6B35) - Energía y apetito
- Rosa Mexicano (#EC4899) - Vibrante y llamativo
- Negro Azulado (#0F172A) - Profesionalismo

**Tipografía:**
- Títulos: Poppins Bold
- Cuerpo: Inter Regular
- Números: JetBrains Mono

**Estilo:**
- Moderno y minimalista
- Animaciones fluidas
- Micro-interacciones
- Glassmorphism
- Modo oscuro y claro

---

## 📊 Especificaciones Técnicas

### Performance:
- **App móvil:** 60 FPS, < 3s carga inicial
- **Web:** Lighthouse Score > 90, Core Web Vitals optimizados

### Compatibilidad:
- **iOS:** 13.0+
- **Android:** API 21+ (Android 5.0+)
- **Web:** Responsive en desktop, tablet, móvil

### Seguridad:
- HTTPS obligatorio
- Encriptación de datos sensibles
- JWT con refresh tokens
- Rate limiting
- Validación de inputs

---

## 🔮 Roadmap

### Fase 1: MVP (Mínimo Producto Viable)
- ✅ App de clientes básica
- ✅ App de repartidores
- ✅ Rastreo en tiempo real
- ✅ Pagos con tarjeta y efectivo

### Fase 2: Expansión
- Portal de negocios completo
- Portal de administradores
- Sistema de cupones avanzado
- Chat en tiempo real
- Notificaciones personalizadas

### Fase 3: Avanzado
- Machine Learning para recomendaciones
- Programa de lealtad
- Subscripciones premium
- Pedidos programados
- Órdenes grupales

---

## 📞 Soporte

Si tienes dudas sobre:
- Instalación de software
- Uso de los prompts
- Tecnologías específicas
- Problemas de configuración

Consulta la **GUIA-INSTALACION-QUIUBOLE.md** que incluye sección de troubleshooting.

---

## 📝 Licencia

Este proyecto es de código abierto. Úsalo libremente para tu emprendimiento.

---

## 🙏 Contribuciones

¡Las contribuciones son bienvenidas! Si mejoras algún prompt o agregas nueva funcionalidad, no dudes en compartirlo.

---

**¡Construye la próxima gran plataforma de delivery con Quiúbole!** 🚀🧡💗

---

## 🌟 Características Destacadas

- ✅ Documentación completa y detallada
- ✅ Prompts listos para usar con IA
- ✅ Stack tecnológico moderno y probado
- ✅ Diseño atractivo y profesional
- ✅ Escalable desde día 1
- ✅ Compatible con 3,000+ usuarios iniciales
- ✅ Performance optimizado
- ✅ Seguridad incorporada

---

**Versión:** 1.0.0
**Fecha:** Noviembre 2024
**Creado para:** Municipio local con expansión futura
**Hardware recomendado:** Legion Pro 5 Gen 10 o similar (32GB RAM, GPU RTX)
