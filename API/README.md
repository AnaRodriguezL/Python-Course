# Métodos HTTP en la API

## ¿Qué es HTTP?

HTTP, o Protocolo de Transferencia de Hipertexto, es un sistema que define cómo se envían y reciben mensajes a través de la web. En la API que se construirá, se utilizará HTTP para comunicarse con el servidor y realizar diferentes acciones sobre los datos, como crear, obtener, modificar o eliminar información. 🌐

## Métodos HTTP Básicos

Existen varios métodos HTTP, pero nos centraremos en los más importantes para construir la API:

- **POST:** Se usa para crear un nuevo recurso. Por ejemplo, agregar una nueva película a la base de datos. 📝
```python
@app.post()
```
- **GET:** Se usa para consultar información. Con él, se puede obtener la lista de películas o detalles de una película específica. 📥
```python
@app.get()
```
- **PUT:** Se usa para modificar un recurso existente. Si se necesita cambiar la información de una película, se usará este método. 🔄
```python
@app.put()
```
- **DELETE:** Como su nombre lo indica, se usa para eliminar un recurso. Si se quiere quitar una película de la base de datos. ❌
```python
@app.delete()
```

## La API de Películas

A lo largo del curso, se construirá una API que proporcionará información sobre películas. Aquí hay algunas cosas que se harán:

- **Consulta de todas las películas:** Utilizando el método GET, se solicitarán datos de todas las películas disponibles. 🎬
- **Filtro de películas:** Se podrá buscar películas por su ID o categoría, usando GET junto con parámetros específicos. 🔍
- **Registro de películas:** Para añadir nuevas películas a la base de datos, se usa el método POST. 📝
- **Modificación y eliminación:** Se completará la API con la capacidad de modificar (con PUT) y eliminar películas (con DELETE). 🔄❌

Esta sección de la API también tratará con los siguientes conceptos específicos de FastAPI:

- **Request:** La solicitud enviada al servidor por un cliente, que incluye información sobre el método HTTP, los encabezados y el cuerpo de la solicitud. 📤
```http
GET /movies HTTP/1.1
Host: api.example.com
Content-Type: application/json
```

- **Response:** La respuesta devuelta por el servidor al cliente después de procesar la solicitud, que incluye el código de estado HTTP, los encabezados y el cuerpo de la respuesta. 📥
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "title": "Titanic",
  "year": 1997,
  "genre": "Romance/Drama"
}
```

- **Body:** El contenido de la solicitud o respuesta, que puede ser cualquier tipo de datos, como texto, JSON o binario. 📦
```http
{
  "title": "Titanic",
  "year": 1997,
  "genre": "Romance/Drama"
}
```

- **Headers:** Los encabezados de la solicitud o respuesta, que contienen información adicional sobre la solicitud o respuesta, como el tipo de contenido, la longitud del cuerpo, etc. 📑
```http
Content-Type: application/json
Content-Length: 67
```
