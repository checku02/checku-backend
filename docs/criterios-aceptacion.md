\# Criterios de aceptación — HU1: Autenticación



\## Objetivo



Establecer las condiciones que debe cumplir la historia de usuario HU1 relacionada con el inicio de sesión y la autenticación en CheckU.



\## Criterios de aceptación



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



\## Condición de aceptación



La HU1 se considerará aceptada cuando los criterios anteriores hayan sido contrastados con los requisitos acordados por el equipo y las pruebas correspondientes demuestren su cumplimiento.

