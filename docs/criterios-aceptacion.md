# Criterios de aceptación — HU1, HU2, HU3, HU4 y HU5

## Objetivo

Establecer las condiciones de aceptación de las historias de usuario HU1 (autenticación), HU2 (grupos y alumnos) y HU3 (docentes y asignaciones) de CheckU.

## HU1. Autenticación

### CA-01. Inicio de sesión

* El sistema debe permitir que un usuario envíe sus credenciales para iniciar sesión.
* Las credenciales deben validarse antes de permitir el acceso.
* Si las credenciales son incorrectas, el sistema debe rechazar el inicio de sesión e informar que no fue posible autenticar al usuario.

### CA-02. Roles de usuario

* El inicio de sesión debe contemplar los roles de administrador, docente y alumno.
* Cuando la autenticación sea exitosa, el sistema debe identificar el rol correspondiente al usuario.
* El usuario debe acceder únicamente a las opciones permitidas para su rol.

### CA-03. Token de autenticación

* Cuando el inicio de sesión sea exitoso, el sistema debe proporcionar un token JWT válido.
* Las solicitudes que requieran autenticación deben poder validar el token recibido.
* Un token inválido debe ser rechazado.

### CA-04. Verificación de sesión

* El sistema debe permitir verificar la validez del token mediante el mecanismo de autenticación definido por la API.
* La verificación debe distinguir entre un token válido y uno inválido o expirado.

### CA-05. Respuestas de la API

* La API debe responder con un resultado que permita identificar si la autenticación fue exitosa.
* Los errores de autenticación deben comunicarse mediante respuestas HTTP apropiadas.
* Las respuestas no deben exponer contraseñas ni secretos de autenticación.

## HU2. Grupos y alumnos

### CA-06. Gestión de grupos

* El sistema debe permitir gestionar los grupos conforme a las operaciones definidas para HU2.
* La información de los grupos debe validarse antes de guardarse.
* El sistema debe comunicar cuando una operación sobre un grupo no pueda completarse.

### CA-07. Gestión de alumnos

* El sistema debe permitir gestionar la información de los alumnos conforme a las operaciones definidas para HU2.
* Los datos de los alumnos deben validarse antes de guardarse.
* El sistema debe comunicar cuando los datos proporcionados no sean válidos.

### CA-08. Relación entre grupos y alumnos

* El sistema debe permitir relacionar alumnos con los grupos correspondientes, de acuerdo con las reglas del proyecto.
* Las operaciones deben comprobar que los registros involucrados existan.
* El sistema debe evitar asociaciones duplicadas cuando las reglas del proyecto no las permitan.

### CA-09. Validación y duplicados

* El sistema debe validar los datos requeridos para las operaciones de grupos y alumnos.
* Cuando se detecte un registro duplicado según las reglas definidas por el proyecto, la operación debe rechazarse o manejarse de acuerdo con esas reglas.
* Los errores deben comunicarse mediante respuestas apropiadas de la API.

## HU3. Docentes y asignaciones

### CA-10. Gestión de docentes

* El sistema debe permitir gestionar la información de los docentes conforme a las operaciones definidas para HU3.
* Los datos proporcionados deben validarse antes de guardarse.
* El sistema debe comunicar cuando una operación sobre un docente no pueda completarse.

### CA-11. Asignaciones

* El sistema debe permitir gestionar las asignaciones de docentes conforme a las reglas definidas para HU3.
* Antes de registrar una asignación, el sistema debe validar la existencia de los registros relacionados.
* El sistema debe comunicar cuando una asignación no pueda realizarse por datos inválidos o referencias inexistentes.

### CA-12. Validación de operaciones

* Las operaciones de docentes y asignaciones deben respetar las validaciones definidas por el proyecto.
* El sistema debe responder apropiadamente cuando una solicitud contenga datos inválidos.
* Las respuestas de la API deben permitir identificar si la operación fue exitosa o si ocurrió un error.

## HU4. Sesión QR

### CA-13. Generación de sesión QR

- El sistema debe permitir generar una sesión QR para una clase.

- El QR debe contener o referenciar un token firmado que permita validar su autenticidad.

- Cada sesión debe contar con un token único.

### CA-14. Vigencia y cierre de sesión

- El sistema debe comprobar que la sesión QR se encuentre vigente antes de aceptarla.

- El sistema debe rechazar los QR correspondientes a sesiones expiradas o cerradas.

- El sistema debe permitir cerrar una sesión QR conforme a las reglas definidas por el proyecto.

### CA-15. Proyección del QR y PIN

- La interfaz debe permitir proyectar el QR y el PIN asociados a la sesión.

- Si ocurre un error que impida utilizar el QR, el sistema debe mostrar un mensaje genérico y permitir regenerarlo cuando corresponda.

- La información presentada debe corresponder a la sesión activa.

### CA-16. Firma y unicidad del token

- El sistema debe validar la firma del token antes de aceptar una sesión QR.

- El sistema debe rechazar tokens cuya firma no sea válida.

- El sistema debe evitar que se acepten tokens duplicados cuando las reglas de la sesión requieran unicidad.

## HU5. Validación QR y registro de asistencia

### CA-17. Validación del QR

- El sistema debe validar la autenticidad y vigencia del QR escaneado.

- El sistema debe rechazar QR inválidos, expirados o asociados a sesiones cerradas.

- Cuando la validación falle, debe comunicar el error sin exponer información sensible.

### CA-18. Registro de asistencia

- Cuando un QR válido sea aceptado, el sistema debe registrar la asistencia conforme a las reglas del proyecto.

- El registro debe relacionarse con la sesión y los datos correspondientes de la clase.

- El sistema debe evitar registros de asistencia duplicados para una misma sesión y alumno.

### CA-19. Confirmación de asistencia

- La aplicación móvil debe mostrar una confirmación cuando la asistencia se registre correctamente.

- La confirmación debe mostrar la materia, el grupo y la hora.

- La confirmación debe presentarse en menos de 5 segundos, conforme al requisito del proyecto.

### CA-20. Manejo de errores de asistencia

- El sistema debe informar cuando un QR sea inválido o haya expirado.

- Si ya existe un registro de asistencia para la misma sesión y alumno, el sistema debe evitar duplicarlo y comunicar el resultado.

- Los errores deben comunicarse mediante respuestas apropiadas de la API y mensajes comprensibles para el usuario.

## Condición de aceptación general

Las historias HU1, HU2, HU3, HU4 y HU5 se considerarán aceptadas cuando los criterios correspondientes hayan sido contrastados con los requisitos acordados por el equipo y las pruebas correspondientes demuestren su cumplimiento.

