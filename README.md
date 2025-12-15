# Gestor de Tareas 🗂️

**Descripción:**  
Este proyecto es un **Gestor de Proyectos y Tareas** desarrollado con **Django**, **Strawberry GraphQL** y **SQL**.  
El objetivo principal es demostrar dominio profesional sobre:

- Autenticación con **access y refresh tokens**
- Hash de contraseñas con Django
- Relaciones SQL:
  - **1 a 1** → Usuario – Perfil
  - **1 a muchos** → Usuario – Proyectos
  - **1 a muchos** → Proyecto – Tareas
  - **Muchos a muchos normalizado** → Usuarios asignados a proyectos con roles
- GraphQL **code-first** usando Strawberry
- Roles y permisos personalizados
- Documentación automática con **Strawberry GraphiQL**
- Pruebas de queries/mutations con **Altair GraphQL Client**

---

## 🛠️ Tecnologías Usadas

- **Python 3**
- **Django**
- **Strawberry (GraphQL)**
- **SQLite / PostgreSQL**
- **PyJWT**
- **Django ORM**

---

## 📦 Instalación y Uso

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/GustavoGutierrez21/PYTHON-gestorTareas
   ```

2. Entrar en la carpeta del proyecto:

   ```bash
   cd PYTHON-gestorTareas
   ```

3. Crear un entorno virtual:

   ```bash
   python -m venv venv
   ```

4. Activarlo:

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

6. Aplicar migraciones de la base de datos:

   ```bash
   python manage.py migrate
   ```

7. Ejecutar el servidor:

   ```bash
   python manage.py runserver
   ```

---

## 📍 Playground principal (Strawberry GraphiQL)

Disponible por defecto en:

```
http://localhost:8000/graphql/
```

Incluye:

- Autocompletado
- Docs del schema
- Historial de queries

---

# 🧪 Uso de Altair GraphQL Client (Recomendado)

Altair es un cliente moderno para hacer queries y mutations a tu API GraphQL.

---

## 🔧 Instalación de Altair

### ✔ Extensión del Navegador (Recomendada)

Chrome / Edge / Brave:

```
https://chromewebstore.google.com/detail/altair-graphql-client/iflndnncoankcfdgplajneolgaankcjg
```

Firefox:

```
https://addons.mozilla.org/en-US/firefox/addon/altair-graphql-client/
```

### ✔ Aplicación de escritorio (opcional)

Descargar desde:

```
https://altairgraphql.dev/
```

---

## 🚀 Usar Altair con tu proyecto Django

1. Abrir Altair
2. En la barra superior, pegar tu endpoint:
   ```
   http://localhost:8000/graphql/
   ```
3. Dar clic en **Set URL**
4. Ya puedes ejecutar queries y mutations

Ejemplo:

```graphql
query {
  hello
}
```

---

## ✨ Características del Proyecto

- CRUD completo de proyectos y tareas
- Usuarios con roles por proyecto
- JWT (access + refresh)
- Hash de contraseñas con Django
- Relaciones SQL:
  - 1:1 Perfil
  - 1:N Proyectos
  - 1:N Tareas
  - N:M Miembros con roles
- GraphQL con Strawberry (Code-first)
- Documentación automática con GraphiQL
- Probado en Altair

---
