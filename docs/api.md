# CheckU API – Contrato de Autenticación (HU1)

Documento de revisión del contrato de la API correspondiente a la Historia de Usuario 1 (Autenticación y gestión de usuarios).

Base URL: `http://localhost:5000`

---

## 1. POST /api/auth/login

**Descripción:** Login unificado para Administrador, Profesor y Alumno.

**Rol requerido:** Ninguno (público)

**Body (JSON):**
| Parámetro     | Tipo   | Obligatorio | Descripción                                      |
|---------------|--------|-------------|--------------------------------------------------|
| identificador | string | Sí          | Matrícula, usuario o email                       |
| password      | string | Sí*         | Contraseña (*obligatoria para admin y profesor)  |
| origen        | string | No          | `"web"` o `"movil"` (default: `"web"`)           |

**Códigos de respuesta:**

| Código | Significado                                      |
|--------|--------------------------------------------------|
| 200    | Login exitoso. Devuelve `access_token` y `role`  |
| 400    | Falta identificador o contraseña                 |
| 401    | Credenciales incorrectas o usuario no encontrado |
| 403    | Alumno intentando entrar desde origen `"web"`    |

---

## 2. GET /api/auth/verify

**Descripción:** Verifica si el token JWT es válido y devuelve el rol y claims.

**Rol requerido:** Cualquier usuario autenticado (JWT)

**Headers:**

**Códigos de respuesta:**

| Código | Significado                                      |
|--------|--------------------------------------------------|
| 200    | Token válido. Devuelve `valid: true`, `role`...  |
| 401    | Token faltante, inválido o expirado              |
| 403    | Alumno intentando verificar desde origen web     |

---

## 3. GET /api/auth/me

**Descripción:** Devuelve los datos del usuario autenticado según su rol.

**Rol requerido:** Cualquier usuario autenticado (JWT)

**Headers:**


**Códigos de respuesta:**

| Código | Significado                          |
|--------|--------------------------------------|
| 200    | Datos del usuario                    |
| 400    | Rol no reconocido                    |
| 401    | Token inválido o expirado            |
| 404    | Usuario no encontrado en la base     |

---

## 4. Endpoints adicionales de autenticación (legacy / específicos)

| Método | Ruta                      | Descripción                     | Códigos principales     |
|--------|---------------------------|---------------------------------|-------------------------|
| POST   | /api/auth/profesor/login  | Login específico de profesor    | 200, 400, 401           |
| POST   | /api/auth/admin/login     | Login específico de admin       | 200, 400, 401           |
| POST   | /api/auth/alumno/login    | Login específico de alumno      | 200, 400, 404           |

---

## Notas importantes (HU1)

- Los tokens JWT tienen una expiración configurada en `JWT_EXPIRATION_HOURS` (por defecto 24 horas).
- Los alumnos **no** pueden acceder al portal web (`origen: "web"` → 403).
- Los códigos de error estandarizados incluyen: `TOKEN_EXPIRED`, `INVALID_TOKEN`, `UNAUTHORIZED`, `ALUMNO_WEB_RESTRICTED`.