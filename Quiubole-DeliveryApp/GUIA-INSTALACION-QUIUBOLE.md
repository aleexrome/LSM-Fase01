# 🛠️ GUÍA COMPLETA DE INSTALACIÓN Y CONFIGURACIÓN - QUIÚBOLE!

## 💻 ESPECIFICACIONES TÉCNICAS

### Tu Hardware (Legion Pro 5 Gen 10):
✅ **EXCELENTE** - Tu computadora es más que suficiente para este proyecto:
- **GPU RTX 5070:** Perfecta para cualquier tarea de desarrollo
- **1TB de almacenamiento:** Suficiente espacio (el proyecto ocupará ~5-10GB)
- **32GB RAM:** Ideal para correr múltiples emuladores y servicios
- **Procesador:** Legion Pro 5 Gen 10 tiene procesadores de alta gama

**Conclusión:** Tu hardware puede manejar sin problemas:
- Múltiples emuladores de Android/iOS corriendo simultáneamente
- IDE pesados (VS Code, Android Studio)
- Backend en desarrollo (Node.js, PostgreSQL)
- Docker containers
- Y mucho más

---

## 📋 ÍNDICE DE INSTALACIÓN

1. [Software Base (Obligatorio)](#1-software-base-obligatorio)
2. [Desarrollo Móvil](#2-desarrollo-móvil)
3. [Desarrollo Web](#3-desarrollo-web)
4. [Backend y Base de Datos](#4-backend-y-base-de-datos)
5. [Herramientas Adicionales](#5-herramientas-adicionales)
6. [Configuración Inicial](#6-configuración-inicial)
7. [Verificación de Instalación](#7-verificación-de-instalación)

---

## 1. SOFTWARE BASE (OBLIGATORIO)

### 🟢 1.1 Node.js (JavaScript Runtime)
**¿Qué es?** Motor que ejecuta JavaScript fuera del navegador.

**Descarga:** https://nodejs.org/
- Descargar versión **LTS (Long Term Support)** - Actualmente 20.x o 22.x
- Ejecutar instalador
- Dejar opciones por defecto
- ✅ Marcar "Automatically install necessary tools" si pregunta

**Verificar instalación:**
```bash
node --version   # Debe mostrar v20.x.x o v22.x.x
npm --version    # Debe mostrar 10.x.x o superior
```

---

### 🟢 1.2 Git (Control de Versiones)
**¿Qué es?** Sistema para controlar versiones del código.

**Descarga:** https://git-scm.com/downloads
- Descargar para Windows
- Instalar con opciones por defecto
- En "Choosing the default editor": seleccionar VS Code (si ya lo instalaste)

**Verificar:**
```bash
git --version   # Debe mostrar git version 2.x.x
```

---

### 🟢 1.3 Visual Studio Code (Editor de Código)
**¿Qué es?** El mejor editor de código para JavaScript/TypeScript.

**Descarga:** https://code.visualstudio.com/
- Descargar e instalar
- ✅ Marcar "Add to PATH"
- ✅ Marcar "Register Code as an editor for supported file types"

**Extensiones OBLIGATORIAS** (instalar desde VS Code):
1. **ES7+ React/Redux/React-Native snippets** (dsznajder)
2. **Prettier - Code formatter** (esbenp)
3. **ESLint** (dbaeumer)
4. **Auto Rename Tag** (formulahendry)
5. **Tailwind CSS IntelliSense** (bradlc)
6. **GitLens** (eamodio)
7. **Thunder Client** (rangav) - Para probar APIs

**Extensiones RECOMENDADAS:**
- Material Icon Theme (PKief)
- Error Lens (usernamehw)
- Console Ninja (WallabyJs)
- Better Comments (aaron-bond)

---

## 2. DESARROLLO MÓVIL

### 🟢 2.1 OPCIÓN A: Expo (Recomendado para empezar rápido)

**¿Qué es?** Plataforma que simplifica el desarrollo con React Native.

**Instalación:**
```bash
npm install -g expo-cli
```

**Verificar:**
```bash
expo --version
```

**App en tu celular:**
- **Android:** Descargar "Expo Go" desde Google Play
- **iOS:** Descargar "Expo Go" desde App Store

**¡Con esto ya puedes desarrollar apps móviles!** 🎉

---

### 🟢 2.2 OPCIÓN B: React Native CLI (Más control, más complejo)

Solo si quieres configuración avanzada y personalización total.

#### Para Android:

**A. Java Development Kit (JDK):**
- Descargar JDK 17 (LTS): https://adoptium.net/
- Instalar
- Agregar a variables de entorno:
  ```
  JAVA_HOME = C:\Program Files\Eclipse Adoptium\jdk-17.x.x
  PATH += %JAVA_HOME%\bin
  ```

**B. Android Studio:**
- Descargar: https://developer.android.com/studio
- Instalar con las opciones por defecto
- Al abrir por primera vez:
  - ✅ Android SDK
  - ✅ Android SDK Platform
  - ✅ Android Virtual Device

**Configurar Android SDK:**
1. Abrir Android Studio
2. More Actions > SDK Manager
3. SDK Platforms tab:
   - ✅ Android 13.0 (Tiramisu) - API 33
   - ✅ Android 12.0 (S) - API 31
4. SDK Tools tab:
   - ✅ Android SDK Build-Tools
   - ✅ Android Emulator
   - ✅ Android SDK Platform-Tools
5. Click "Apply" y "OK"

**Variables de entorno:**
```
ANDROID_HOME = C:\Users\TU_USUARIO\AppData\Local\Android\Sdk
PATH += %ANDROID_HOME%\platform-tools
PATH += %ANDROID_HOME%\emulator
PATH += %ANDROID_HOME%\tools
PATH += %ANDROID_HOME%\tools\bin
```

**Verificar:**
```bash
adb --version
```

#### Para iOS (Solo si tienes Mac):
- Xcode desde App Store
- Command Line Tools: `xcode-select --install`
- CocoaPods: `sudo gem install cocoapods`

---

## 3. DESARROLLO WEB

### 🟢 3.1 Herramientas ya cubiertas:
- ✅ Node.js (ya instalado)
- ✅ VS Code (ya instalado)

### 🟢 3.2 Navegadores para Testing:

**Principales:**
- Google Chrome (https://www.google.com/chrome/)
- Firefox Developer Edition (https://www.mozilla.org/firefox/developer/)
- Microsoft Edge (preinstalado en Windows)

**Extensiones de Chrome útiles:**
- React Developer Tools
- Redux DevTools
- Lighthouse
- WhatFont
- ColorZilla

---

## 4. BACKEND Y BASE DE DATOS

### 🟢 4.1 PostgreSQL (Base de Datos Principal)

**Descarga:** https://www.postgresql.org/download/windows/
- Descargar instalador
- Durante instalación:
  - Puerto: **5432** (default)
  - Contraseña: Elige una y **¡GUÁRDALA!**
  - Locale: default
- ✅ Instalar Stack Builder components (opcional)

**Cliente GUI (para ver la BD visualmente):**
- **pgAdmin** (viene con PostgreSQL) - Ya instalado
- O **DBeaver** (https://dbeaver.io/) - Más moderno

**Verificar:**
- Abrir pgAdmin
- Conectar a localhost
- Debe conectarse sin problemas

---

### 🟢 4.2 Docker (Opcional pero muy útil)

**¿Qué es?** Permite correr servicios (base de datos, Redis, etc.) en contenedores.

**Descarga:** https://www.docker.com/products/docker-desktop/
- Descargar Docker Desktop for Windows
- Instalar
- Requiere WSL 2 (se instala automáticamente)
- Reiniciar PC después de instalar

**Verificar:**
```bash
docker --version
docker-compose --version
```

**Ventaja:** Puedes levantar PostgreSQL, Redis, y otros servicios sin instalarlos directamente.

---

### 🟢 4.3 Postman / Thunder Client (Testing de APIs)

**Thunder Client** (ya en extensiones de VS Code)
O
**Postman:** https://www.postman.com/downloads/
- Descargar e instalar
- Crear cuenta gratis

---

## 5. HERRAMIENTAS ADICIONALES

### 🟢 5.1 Terminal Mejorada (Opcional pero recomendado)

**Windows Terminal:**
- Descargar desde Microsoft Store
- O desde https://github.com/microsoft/terminal

**PowerShell 7:**
- https://github.com/PowerShell/PowerShell/releases
- Mejor que PowerShell 5 que viene con Windows

---

### 🟢 5.2 Cloudinary (Manejo de Imágenes)

**No requiere instalación local:**
1. Ir a https://cloudinary.com/
2. Crear cuenta gratuita
3. Copiar:
   - Cloud name
   - API Key
   - API Secret
4. Guardar en archivo `.env`

---

### 🟢 5.3 Firebase (Backend as a Service)

**No requiere instalación local:**
1. Ir a https://firebase.google.com/
2. Crear cuenta con Google
3. Crear nuevo proyecto
4. Habilitar:
   - Authentication
   - Realtime Database
   - Cloud Messaging (para push notifications)
5. Copiar configuración (Firebase SDK)

**Instalación en proyecto:**
```bash
npm install firebase
```

---

### 🟢 5.4 Stripe (Pagos)

**Cuenta de prueba:**
1. Ir a https://stripe.com/
2. Crear cuenta
3. Activar modo "Test mode"
4. Copiar:
   - Publishable key
   - Secret key
5. Guardar en `.env`

**NO uses claves reales hasta producción.**

---

### 🟢 5.5 Google Maps API

1. Ir a https://console.cloud.google.com/
2. Crear proyecto nuevo: "Quiubole"
3. Habilitar APIs:
   - Maps JavaScript API
   - Geocoding API
   - Directions API
   - Places API
4. Crear credenciales:
   - Tipo: API Key
   - Restricciones: IP (para backend) o HTTP referrers (para frontend)
5. Copiar API Key
6. Guardar en `.env`

**Nota:** Google da $200 USD de crédito gratis mensual.

---

## 6. CONFIGURACIÓN INICIAL

### 🟢 6.1 Configurar Git (Primera vez)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

---

### 🟢 6.2 Crear Proyecto React Native con Expo

```bash
# Crear carpeta para tus proyectos
mkdir C:\Proyectos
cd C:\Proyectos

# Crear proyecto de app móvil
npx create-expo-app quiubole-app --template blank-typescript

# Entrar al proyecto
cd quiubole-app

# Instalar dependencias principales
npm install @react-navigation/native @react-navigation/native-stack
npm install react-native-screens react-native-safe-area-context
npm install @react-native-async-storage/async-storage
npm install axios
npm install zustand
npm install react-hook-form
npm install @hookform/resolvers zod

# Dependencias de UI
npm install react-native-paper
npm install react-native-reanimated
npm install react-native-gesture-handler

# Mapas
npm install react-native-maps

# Iniciar proyecto
npm start
```

---

### 🟢 6.3 Crear Proyecto Next.js para Web

```bash
cd C:\Proyectos

# Crear proyecto web
npx create-next-app@latest quiubole-web --typescript --tailwind --app

# Responder las preguntas:
# ✓ Would you like to use ESLint? Yes
# ✓ Would you like to use Tailwind CSS? Yes
# ✓ Would you like to use `src/` directory? No
# ✓ Would you like to use App Router? Yes
# ✓ Would you like to customize the default import alias? No

cd quiubole-web

# Instalar dependencias
npm install zustand
npm install axios
npm install react-hook-form @hookform/resolvers zod
npm install framer-motion
npm install @tanstack/react-table
npm install recharts
npm install react-hot-toast
npm install lucide-react

# shadcn/ui
npx shadcn-ui@latest init
# Responder:
# Style: Default
# Base color: Slate
# CSS variables: Yes

# Instalar componentes de shadcn/ui
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
npx shadcn-ui@latest add input
npx shadcn-ui@latest add form
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
npx shadcn-ui@latest add tabs
npx shadcn-ui@latest add table

# Iniciar proyecto
npm run dev
```

Abrir http://localhost:3000 en el navegador.

---

### 🟢 6.4 Crear Backend con Nest.js

```bash
cd C:\Proyectos

# Instalar Nest CLI
npm install -g @nestjs/cli

# Crear proyecto backend
nest new quiubole-backend

# Elegir npm como package manager

cd quiubole-backend

# Instalar dependencias
npm install @nestjs/typeorm typeorm pg
npm install @nestjs/config
npm install @nestjs/jwt @nestjs/passport passport passport-jwt
npm install bcrypt
npm install class-validator class-transformer
npm install @nestjs/websockets @nestjs/platform-socket.io

# Tipos de TypeScript
npm install -D @types/bcrypt @types/passport-jwt

# Iniciar servidor
npm run start:dev
```

---

### 🟢 6.5 Archivo .env (Variables de Entorno)

Crear archivo `.env` en cada proyecto:

**Backend (.env):**
```env
# Base de datos
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=postgres
DATABASE_PASSWORD=tu_password_aqui
DATABASE_NAME=quiubole_db

# JWT
JWT_SECRET=tu_secret_super_seguro_aqui_cambiar_en_produccion
JWT_EXPIRES_IN=7d

# Stripe
STRIPE_SECRET_KEY=sk_test_tu_key_aqui
STRIPE_PUBLISHABLE_KEY=pk_test_tu_key_aqui

# Cloudinary
CLOUDINARY_CLOUD_NAME=tu_cloud_name
CLOUDINARY_API_KEY=tu_api_key
CLOUDINARY_API_SECRET=tu_api_secret

# Google Maps
GOOGLE_MAPS_API_KEY=tu_google_maps_key

# Firebase
FIREBASE_API_KEY=tu_firebase_key
FIREBASE_AUTH_DOMAIN=tu-proyecto.firebaseapp.com
FIREBASE_PROJECT_ID=tu-proyecto
FIREBASE_STORAGE_BUCKET=tu-proyecto.appspot.com
FIREBASE_MESSAGING_SENDER_ID=123456789
FIREBASE_APP_ID=1:123456789:web:abcdef

# Otros
PORT=3001
NODE_ENV=development
```

**Frontend Web (.env.local):**
```env
NEXT_PUBLIC_API_URL=http://localhost:3001
NEXT_PUBLIC_GOOGLE_MAPS_API_KEY=tu_key_aqui
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_tu_key_aqui
```

**App Móvil (.env):**
```env
API_URL=http://localhost:3001
GOOGLE_MAPS_API_KEY=tu_key_aqui
STRIPE_PUBLISHABLE_KEY=pk_test_tu_key_aqui
```

---

## 7. VERIFICACIÓN DE INSTALACIÓN

### ✅ Checklist completo:

Ejecuta estos comandos uno por uno y verifica que todos funcionen:

```bash
# Node.js y npm
node --version
npm --version

# Git
git --version

# Expo (si instalaste)
expo --version

# Android (si instalaste React Native CLI)
adb --version

# Docker (si instalaste)
docker --version

# Nest CLI
nest --version
```

**Todos deben devolver una versión. Si alguno da error, reinstalar.**

---

## 🎨 CONFIGURACIÓN DE COLORES (Opción 3 - Vibrante)

### Tailwind Config (quiubole-web/tailwind.config.ts):

```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: 'class',
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Opción 3 - Vibrante
        primary: {
          DEFAULT: '#8B5CF6', // Morado
          50: '#F5F3FF',
          100: '#EDE9FE',
          200: '#DDD6FE',
          300: '#C4B5FD',
          400: '#A78BFA',
          500: '#8B5CF6',
          600: '#7C3AED',
          700: '#6D28D9',
          800: '#5B21B6',
          900: '#4C1D95',
        },
        secondary: {
          DEFAULT: '#EC4899', // Rosa
          50: '#FDF2F8',
          100: '#FCE7F3',
          200: '#FBCFE8',
          300: '#F9A8D4',
          400: '#F472B6',
          500: '#EC4899',
          600: '#DB2777',
          700: '#BE185D',
          800: '#9F1239',
          900: '#831843',
        },
        accent: {
          DEFAULT: '#0F172A', // Negro azulado
          50: '#F8FAFC',
          100: '#F1F5F9',
          200: '#E2E8F0',
          300: '#CBD5E1',
          400: '#94A3B8',
          500: '#64748B',
          600: '#475569',
          700: '#334155',
          800: '#1E293B',
          900: '#0F172A',
        },
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Poppins', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
export default config
```

### React Native Theme (quiubole-app/src/theme/colors.ts):

```typescript
export const colors = {
  primary: '#8B5CF6', // Morado
  primaryLight: '#A78BFA',
  primaryDark: '#7C3AED',

  secondary: '#EC4899', // Rosa
  secondaryLight: '#F472B6',
  secondaryDark: '#DB2777',

  accent: '#0F172A', // Negro azulado

  background: '#FFFFFF',
  backgroundSecondary: '#F8FAFC',

  text: '#1F2937',
  textLight: '#6B7280',
  textDark: '#111827',

  border: '#E5E7EB',

  success: '#10B981',
  warning: '#F59E0B',
  error: '#EF4444',
  info: '#3B82F6',

  // Gradientes
  gradientPrimary: ['#8B5CF6', '#EC4899'],
  gradientSecondary: ['#EC4899', '#F472B6'],
}
```

---

## 📚 RECURSOS DE APRENDIZAJE

### Documentación Oficial:
- **React Native:** https://reactnative.dev/docs/getting-started
- **Expo:** https://docs.expo.dev/
- **Next.js:** https://nextjs.org/docs
- **Nest.js:** https://docs.nestjs.com/
- **Tailwind CSS:** https://tailwindcss.com/docs
- **TypeScript:** https://www.typescriptlang.org/docs/

### Tutoriales Recomendados:
- **React Native:** "The Net Ninja" en YouTube
- **Next.js:** Documentación oficial + "Vercel" YouTube channel
- **Node.js/Nest.js:** "Traversy Media" en YouTube
- **TypeScript:** "Matt Pocock" en YouTube

---

## 🆘 SOLUCIÓN DE PROBLEMAS COMUNES

### Error: "npm no se reconoce como comando"
**Solución:** Reiniciar la terminal o PC después de instalar Node.js

### Error: "adb no se reconoce como comando"
**Solución:** Verificar que las variables de entorno ANDROID_HOME estén correctas

### Error: "Cannot find module..."
**Solución:**
```bash
rm -rf node_modules
npm install
```

### Error: "Port 3000 is already in use"
**Solución:** Matar proceso en ese puerto:
```bash
# Windows
netstat -ano | findstr :3000
taskkill /PID <PID_NUMBER> /F

# O cambiar puerto
npm run dev -- -p 3001
```

### Emulador Android muy lento
**Solución:**
1. Habilitar Virtualization en BIOS
2. Usar Expo Go en celular físico (más rápido)

---

## 🚀 SIGUIENTE PASO

**¡YA TIENES TODO LISTO!** Ahora puedes:

1. **Para App Móvil:** Abre `prompt-app-movil-delivery.md` y copia el prompt final
2. **Para Web:** Abre `prompt-web-delivery.md` y copia el prompt final
3. Pega el prompt en Claude, ChatGPT, o cualquier IA de código
4. ¡Empieza a construir Quiúbole!

---

## 📞 COMANDOS ÚTILES DE REFERENCIA RÁPIDA

### App Móvil (Expo):
```bash
cd quiubole-app
npm start          # Iniciar servidor de desarrollo
npm run android    # Correr en Android
npm run ios        # Correr en iOS (solo Mac)
```

### Web (Next.js):
```bash
cd quiubole-web
npm run dev        # Modo desarrollo
npm run build      # Build de producción
npm run start      # Iniciar servidor de producción
npm run lint       # Linter
```

### Backend (Nest.js):
```bash
cd quiubole-backend
npm run start:dev  # Modo desarrollo (hot reload)
npm run start      # Iniciar servidor
npm run build      # Build de producción
```

---

**¡Estás listo para crear Quiúbole!** 🎉🚀

Si tienes algún error durante la instalación, copia el error y pregúntame.
