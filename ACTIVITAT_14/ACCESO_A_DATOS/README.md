#  Proyecto Login con Django y PostgreSQL

## Tecnologías utilizadas

- Download Python 3.13.3
- Django 4.1
- PostgreSQL 13
- Docker y Docker Compose
- Pycharm Comunity Edition 2024.3.5


## Estructura del proyecto

![img.png](Capturas/img.png)


## Funcionalidades

###  Login sin sesión
- Vista que recibe email y password.
- Verifica en la base de datos sin guardar estado.
- Si las credenciales son válidas, redirige a una página de inicio.
- Si no, muestra un mensaje de error.

###  Login con sesión
- Igual al login anterior pero almacena la `usuario_id` en `request.session`.
- Permite mantener la sesión iniciada hasta hacer logout.
- Redirige al login si intenta acceder sin estar autenticado.

###  Logout
- Borra la sesión activa y redirige al formulario de login con sesión.

###  Página de inicio
- Muestra mensaje de bienvenida con el nombre del usuario y un botón de cerrar sesión.


## Capturas de pantalla

### Formulario de Login

![img.png](Capturas/img.png)

Código:
```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Entrar</button>
</form>
```

### Página de Inicio con sesión activa

![img_1.png](Capturas/img_1.png)

Código:
```html
<h1>Benvingut/da {{ usuario.nombre }}</h1>
<p>Ciutat: {{ usuario.ciudad }}</p>
<a href="{% url 'logout' %}">Tancar sessió</a>
```

---

## Base de datos PostgreSQL

![img_2.png](Capturas/img_2.png)

![img_3.png](Capturas/img_3.png)

- Conectada mediante `docker-compose.yml`.
- Modelo `Usuario` con campos: `nombre`, `email`, `password`, `ciudad`.
- Campo `email` con `unique=True`.


## Pruebas realizadas

- Login sin sesión ( muestra error).
![img_4.png](Capturas/img_4.png)
- Login con sesión (mantiene sesión abierta tras recargar).
![img_10.png](Capturas/img_10.png)
- Logout (cierra correctamente la sesión).
![img_6.png](Capturas/img_6.png)
![img_7.png](Capturas/img_7.png)
- Acceso denegado a `/inicio/` si no hay sesión.
![img_8.png](Capturas/img_8.png)
![img_9.png](Capturas/img_9.png)
![img_10.png](Capturas/img_10.png)
