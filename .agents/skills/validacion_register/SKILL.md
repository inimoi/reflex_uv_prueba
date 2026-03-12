---
name: validacion register
version: 1.1.0
author: Inigo
description: Verificar que los endpoint del register esten correctamente implementados y cumplan las reglas de negocio.
---

Este skill define las validaciones críticas que deben cumplirse para el registro de nuevos usuarios:

### Reglas de Validación
1. **Email Único**: El correo electrónico no debe existir previamente en el sistema (gestionado por Supabase).
2. **Email Formato**: Debe ser un correo electrónico válido (tipo `EmailStr`).
3. **Password Robusta**:
   - Longitud mínima de **8 caracteres**.
   - Debe contener al menos **un número**.
   - Debe contener al menos **una letra mayúscula**.
4. **Nombre de Usuario**:
   - Longitud mínima de **5 caracteres**.

### Verificación Automática
Para verificar estas reglas, puedes ejecutar el script de validación incluido en este skill.
