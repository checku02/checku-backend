\# Criterios de aceptación — HU1, HU2 y HU3



\## Objetivo



Establecer las condiciones de aceptación de las historias de usuario HU1 (autenticación), HU2 (grupos y alumnos) y HU3 (docentes y asignaciones) de CheckU.



\## HU1. Autenticación



\### CA-01. Inicio de sesión



\- El sistema debe permitir que un usuario envíe sus credenciales para iniciar sesión.

\- Las credenciales deben validarse antes de permitir el acceso.

\- Si las credenciales son incorrectas, el sistema debe rechazar el inicio de sesión e informar que no fue posible autenticar al usuario.



\### CA-02. Roles de usuario



\- El inicio de sesión debe contemplar los roles de administrador, docente y alumno.

\- Cuando la autenticación sea exitosa, el sistema debe identificar el rol correspondiente al usuario.

\- El usuario debe acceder únicamente a las opciones permitidas para su rol.



\### CA-03. Token de autenticación



\- Cuando el inicio de sesión sea exitoso, el sistema debe proporcionar un token JWT válido.

\- Las solicitudes que requieran autenticación deben poder validar el token recibido.

\- Un token inválido debe ser rechazado.



\### CA-04. Verificación de sesión



\- El sistema debe permitir verificar la validez del token mediante el mecanismo de autenticación definido por la API.

\- La verificación debe distinguir entre un token válido y uno inválido o expirado.



\### CA-05. Respuestas de la API



\- La API debe responder con un resultado que permita identificar si la autenticación fue exitosa.

\- Los errores de autenticación deben comunicarse mediante respuestas HTTP apropiadas.

\- Las respuestas no deben exponer contraseñas ni secretos de autenticación.



\## HU2. Grupos y alumnos



\### CA-06. Gestión de grupos



\- El sistema debe permitir gestionar los grupos conforme a las operaciones definidas para HU2.

\- La información de los grupos debe validarse antes de guardarse.

\- El sistema debe comunicar cuando una operación sobre un grupo no pueda completarse.



\### CA-07. Gestión de alumnos



\- El sistema debe permitir gestionar la información de los alumnos conforme a las operaciones definidas para HU2.

\- Los datos de los alumnos deben validarse antes de guardarse.

\- El sistema debe comunicar cuando los datos proporcionados no sean válidos.



\### CA-08. Relación entre grupos y alumnos



\- El sistema debe permitir relacionar alumnos con los grupos correspondientes, de acuerdo con las reglas del proyecto.

\- Las operaciones deben comprobar que los registros involucrados existan.

\- El sistema debe evitar asociaciones duplicadas cuando las reglas del proyecto no las permitan.



\### CA-09. Validación y duplicados



\- El sistema debe validar los datos requeridos para las operaciones de grupos y alumnos.

\- Cuando se detecte un registro duplicado según las reglas definidas por el proyecto, la operación debe rechazarse o manejarse de acuerdo con esas reglas.

\- Los errores deben comunicarse mediante respuestas apropiadas de la API.



\## HU3. Docentes y asignaciones



\### CA-10. Gestión de docentes



\- El sistema debe permitir gestionar la información de los docentes conforme a las operaciones definidas para HU3.

\- Los datos proporcionados deben validarse antes de guardarse.

\- El sistema debe comunicar cuando una operación sobre un docente no pueda completarse.



\### CA-11. Asignaciones



\- El sistema debe permitir gestionar las asignaciones de docentes conforme a las reglas definidas para HU3.

\- Antes de registrar una asignación, el sistema debe validar la existencia de los registros relacionados.

\- El sistema debe comunicar cuando una asignación no pueda realizarse por datos inválidos o referencias inexistentes.



\### CA-12. Validación de operaciones



\- Las operaciones de docentes y asignaciones deben respetar las validaciones definidas por el proyecto.

\- El sistema debe responder apropiadamente cuando una solicitud contenga datos inválidos.

\- Las respuestas de la API deben permitir identificar si la operación fue exitosa o si ocurrió un error.



\## Condición de aceptación



Las historias HU1, HU2 y HU3 se considerarán aceptadas cuando los criterios correspondientes hayan sido contrastados con los requisitos acordados por el equipo y las pruebas correspondientes demuestren su cumplimiento.

