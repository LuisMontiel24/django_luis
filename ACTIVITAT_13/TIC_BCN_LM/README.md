












# 📘 Proyecto Django: Gestión de Personas (Alumnos y Profesores)

Este proyecto permite gestionar un listado de personas clasificadas por roles: **alumnos** y **profesores**. Incluye creación, edición, visualización y eliminación desde un panel web y el panel de administración de Django.


## 📸 `models.py` – Modelo de Persona

Define el esqueleto del HTML (<doctype>, <head>, <body>) e incluye una cabecera común a todas las páginas usando {% include 'centre/header.html' %}. Tiene un bloque {% block content %} para que otras plantillas puedan heredar de él y colocar su contenido específico.

![Captura del modelo Persona](/Fotos/models.py.png)


## 📸 `forms.py` – Formulario de Persona

PersonaForm extiende de ModelForm y se vincula con el modelo Persona.
Se usan widgets para personalizar el diseño de los campos con clases de Bootstrap.
Se establecen etiquetas (labels) en catalán para los campos del formulario.

![Captura del modelo Persona](/Fotos/forms.py.png)


## 📸 `admin.py` – Registro del modelo en el panel de administración

Se registra el modelo Persona en el panel de administración con una clase personalizada.
list_display define qué campos mostrar en el listado.
list_filter permite filtrar por rol y si es tutor.
search_fields permite búsqueda rápida por nombre, apellido y correo.
fieldsets agrupa los campos en secciones: personales y académicos.

![Captura del modelo Persona](/Fotos/admin.py.png)


## 📸 `views.py` –Vistas (lógica del backend)

render, redirect: para mostrar HTML o redirigir.
get_object_or_404: lanza error si no se encuentra el objeto.
reverse: construye URLs dinámicas.
messages: sistema de mensajes flash.
never_cache: evita caché del navegador.
transaction: asegura atomicidad en BD.
time: para mostrar hora de última actualización.

![Captura del modelo Persona](/Fotos/views.py1.png)

![Captura del modelo Persona](/Fotos/views.py.png)



## Estructura de las Vistas HTML

## 📸 `base.html` 

Este archivo es la plantilla base de todo el proyecto. Define el esqueleto del HTML (doctype, <head>, <body>) e incluye una cabecera común a todas las páginas usando {% include 'centre/header.html' %}. Tiene un bloque {% block content %} para que otras plantillas puedan heredar de él y colocar su contenido específico.

## 📸 `header.html` 

Contiene la cabecera de la web que se visualiza en todas las vistas. Incluye el nombre de la institución y enlaces de navegación al listado de alumnat y professorat.


## Apartado Professorat

## 📸 `teacher_list.html` 

Página principal que muestra el listado de profesorado.
Incluye un botón para "Afegir Professor".
Se presenta una tabla con columnas como ID, nombre, apellido, curso y si es tutor.
Añade opciones de acción como "Editar" y "Eliminar".
Si no hay profesores registrados, se muestra un mensaje indicativo.

![Captura del modelo Persona](/Fotos/teacher_list.html.png)

## 📸 `teacher_detail.html` 

Muestra el detalle de todos los profesores (puede haber confusión con el nombre, ya que normalmente *_detail.html sería para uno solo).

Permite ver un resumen tabular de los datos de cada profesor y ofrece los botones de edición y eliminación.

![Captura del modelo Persona](/Fotos/teacher_detail.html.png)

## 📸 `teachers.html` 

Muy similar a teacher_detail.html, pero más simple.
Lista profesores con atributos como nombre, edad, curso, etc.
Botón de acción "INFO" que redirige a teacher_detail.

![Captura del modelo Persona](/Fotos/teachers.html1.png)


## Apartado Alumnat

## 📸 `student_list.html` 

Página principal del alumnado.
Contiene un botón "Afegir Alumne".
Muestra una tabla con nombre, apellido, curso y acciones como "Editar" o "Eliminar".
Si no hay alumnos, se muestra un mensaje informativo.

![Captura del modelo Persona](/Fotos/student_list.html.png)

## 📸 `student_detail.html` 

Muestra información detallada de un alumno específico.
Incluye nombre, apellidos, correo, curso y módulos.
Botón para volver al listado general.

![Captura del modelo Persona](/Fotos/student_detail.html.png)

## 📸 `students.html` 

Alternativa más simple a student_list.html.
Solo muestra nombre, apellido y rol del alumno.
Opción de ver más detalles con el botón "INFO".

![Captura del modelo Persona](/Fotos/students.html.png)



## Formularios y Eliminación

## 📸 `persona_form.html` 

Usado tanto para añadir como editar personas (alumnos o profesores).
Detecta automáticamente si se trata de un profesor para mostrar el campo "tutor".
Incluye validaciones y mensajes de error con diseño amigable.
Contiene estilos para botones "Guardar" y "Cancel·lar".persona_confirm_delete.html

![Captura del modelo Persona](/Fotos/persona_form.html.png)

## 📸 `persona_confirm_delete.html` 

Plantilla para confirmar la eliminación de un alumno o profesor.
Incluye botón de confirmación y opción para cancelar.

![Captura del modelo Persona](/Fotos/persona_confirm_delete.html.png)