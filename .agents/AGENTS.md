# 🤖 AGENTS.md: Project Coordination Template

Este archivo sirve como hoja de ruta y punto de coordinación para los agentes (IA y humanos) que trabajan en el proyecto **reflex_uv**.

---

## 🎯 Objetivo Actual
> Describe aquí el hito principal en el que se está trabajando.
*Ejemplo: Implementar el sistema de navegación y la página de inicio con el nuevo sistema de estilos.*

---

## 📋 Lista de Tareas (Backlog)

### 🔴 Prioridad Alta
- [x] **Configuración Base**: Sistema de diseño (`colors.py`, `fonts.py`, `size.py`) integrado en `styles.py`.
- [x] **Footer Premium**: Rediseñado completamente con estética moderna y responsiva.
- [x] **Navbar Premium**: Rediseñado con glassmorphism para coincidir con el Footer.
- [x] **Validación de API**: Implementada validación robusta con Pydantic en registro y login, con manejo de errores y feedback visual (Toasts).

### 🟡 Prioridad Media
- [ ] **Diseño Responsivo**: Asegurar que los componentes se adapten a móviles.
- [ ] **Animaciones**: Añadir micro-interacciones usando Framer Motion (si aplica) o CSS Transitions.

### 🟢 Backlog / Futuro
- [ ] Integración con Base de Datos.
- [ ] Sistema de Autenticación.

---

## 🎨 Sistema de Diseño
Este proyecto utiliza un sistema de diseño centralizado en la carpeta `reflex_uv/styles/`.
- **Colores**: [colors.py](file:///home/inigo/Documentos/Reflex/reflex_uv/reflex_uv/styles/colors.py)
- **Espaciado**: [spacing.py](file:///home/inigo/Documentos/Reflex/reflex_uv/reflex_uv/styles/spacing.py)
- **Tamaños**: [size.py](file:///home/inigo/Documentos/Reflex/reflex_uv/reflex_uv/styles/size.py)
- **Estilos Globales**: [styles.py](file:///home/inigo/Documentos/Reflex/reflex_uv/reflex_uv/styles/styles.py)

**Regla de Oro**: NO uses valores "hardcoded" (ej. `#FFFFFF` o `padding="10px"`). Usa siempre las variables definidas en el sistema de diseño.

---

## 🛠️ Stack Tecnológico
- **Framework**: [Reflex](https://reflex.dev/) (Python)
- **Gestor de Paquetes**: `uv`
- **Estilos**: Tailwind CSS V4 (Plugin configurado en `rxconfig.py`)
- **Arquitectura**: Componentes modulares.

---

## 📜 Reglas para Agentes (AI Guidelines)
1. **Verificación**: Antes de dar por terminada una tarea, ejecuta `reflex run` (en segundo plano) para verificar que no haya errores de compilación.
2. **Estilo de Código**: Sigue PEP 8. Usa nombres descriptivos para los componentes.
3. **Documentación**: Si creas un componente nuevo, añade un breve comentario de qué hace y qué props acepta.
4. **Actualización**: Mantén este archivo `AGENTS.md` actualizado con el progreso.

---

## ✅ Registro de Cambios (Log)
- **2026-03-12**: Verificación exitosa de la app con el nuevo diseño premium y corrección de la lógica de renderizado condicional en la Navbar. (Agente: Antigravity)
- **2026-03-12**: Rediseño premium de Navbar y Footer con sistema de diseño centralizado. (Agente: Antigravity)
- **2026-03-12**: Estandarización de la estructura de skills (`SKILLS.md` -> `SKILL.md`) y organización de carpeta `.agents/`. (Agente: Antigravity)
