# 🛡️ ServerGuard CLI

**ServerGuard CLI** es una herramienta profesional de línea de comandos (CLI) para la **gestión, auditoría y monitoreo de servidores**, diseñada para administradores de sistemas, desarrolladores y perfiles DevOps.

Inspirada en herramientas como `git`, `docker` o `kubectl`, ServerGuard permite **entender el estado de un servidor y su seguridad directamente desde la terminal**, de forma clara, estructurada y multiplataforma.

---

## 🚀 Características principales

* 📊 Monitoreo del sistema (CPU, memoria, disco, uptime)
* ⚙️ Gestión y estado de servicios
* 📜 Visualización y búsqueda de logs
* 👥 Gestión de usuarios y sesiones activas
* 🔐 Auditorías de seguridad y cumplimiento
* 🧾 Generación de reportes (daily / weekly / monthly)
* 🎨 Salida profesional con colores y símbolos
* 🌍 Compatible con **Windows y Linux**

---

## 📦 Requisitos

* Python **3.8+**
* Terminal compatible con UTF-8 (recomendado)

> No requiere librerías externas: usa solo la librería estándar de Python.

---

## 🔧 Instalación

### 1️⃣ Clonar o descargar el repositorio

```bash
git clone https://github.com/tuusuario/serverguard-cli.git
cd serverguard-cli
```

### 2️⃣ Guardar el archivo principal

El script principal es:

```bash
serverguard.py
```

### 3️⃣ Permisos de ejecución (Linux / macOS)

```bash
chmod +x serverguard.py
```

### 4️⃣ Ejecutar

```bash
python serverguard.py --help
```

---

## ▶️ Uso básico

ServerGuard sigue una estructura de comandos jerárquica:

```bash
serverguard <comando> <subcomando> [opciones]
```

### Ejemplos rápidos

```bash
serverguard system status
serverguard logs tail --lines 20
serverguard users list
serverguard audit scan
serverguard report generate daily
```

---

## 🧠 Comandos disponibles

### 🖥️ `system` – Estado del sistema

```bash
serverguard system status
serverguard system services
serverguard system resources
```

Incluye:

* Uso de CPU
* Memoria RAM
* Discos
* Servicios activos
* Uptime

---

### 📜 `logs` – Gestión de logs

```bash
serverguard logs tail --lines 50
serverguard logs tail --service nginx
serverguard logs search ERROR --hours 24
```

Funciones:

* Visualizar logs recientes
* Filtrar por servicio
* Buscar errores o patrones

---

### 👥 `users` – Usuarios y sesiones

```bash
serverguard users list
serverguard users sessions
```

Muestra:

* Usuarios del sistema
* UID y grupos
* Último acceso
* Sesiones activas

---

### 🔐 `audit` – Auditoría y cumplimiento

```bash
serverguard audit scan
serverguard audit compliance
```

Incluye:

* Reglas básicas de seguridad
* Estado del firewall
* Políticas de contraseñas
* Cifrado y permisos

---

### 🧾 `report` – Generación de reportes

```bash
serverguard report generate daily
serverguard report generate weekly --format html
serverguard report generate monthly --format json
```

Opciones:

* Tipo: `daily`, `weekly`, `monthly`
* Formato: `pdf`, `html`, `json`
* Periodo configurable

---

## 🎨 Opciones globales

```bash
--no-color     Desactiva salida con colores
--version      Muestra la versión
--help         Ayuda general
```

---

## 🧱 Arquitectura del proyecto

Actualmente el proyecto está diseñado como **script único**, pero preparado para escalar a arquitectura modular:

```text
serverguard.py
│
├── CLI & routing
├── System module
├── Logs module
├── Users module
├── Audit module
└── Report module
```

---

## 🔒 Seguridad

* No ejecuta cambios destructivos
* Ideal para entornos de auditoría
* Preparado para integración futura con:

  * Roles
  * Autenticación
  * Logs persistentes

---

## 🛣️ Roadmap

* [x] CLI profesional estilo enterprise
* [x] System / Logs / Users / Audit / Report
* [ ] Persistencia real de datos
* [ ] Integración con `psutil`
* [ ] Modo daemon
* [ ] Exportación real de reportes
* [ ] Instalación como comando global

---

## 💼 Enfoque profesional

Este proyecto demuestra habilidades en:

* Python avanzado
* Diseño de herramientas CLI
* Arquitectura de software
* Sistemas operativos
* Auditoría y monitoreo

Ideal para **portafolio, CV técnico y proyectos DevOps**.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

---

## 🤝 Contribuciones

Las contribuciones, ideas y mejoras son bienvenidas.

```bash
git checkout -b feature/nueva-funcionalidad
git commit -m "add new feature"
git push origin feature/nueva-funcionalidad
```

---

## 📌 Autor

Desarrollado por **Alexander Josué Delgado Rodríguez**
Enfoque en automatización, sistemas y desarrollo de software.

---

> *ServerGuard CLI — Control total del servidor, directamente desde la terminal.*
