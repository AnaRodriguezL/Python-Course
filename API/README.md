# HTTP Methods in the API 🌐

HTTP, or Hypertext Transfer Protocol, is a system that defines how messages are sent and received over the web. In the API to be built, HTTP will be used to communicate with the server and perform different actions on the data, such as creating, retrieving, modifying, or deleting information. 🌐

## Basic HTTP Methods

There are several HTTP methods, but we will focus on the most important ones for building the API:

- **POST:** Used to create a new resource. For example, adding a new movie to the database. 📝
```python
@app.post()
```
- **GET:** Used to retrieve information. With it, you can obtain the list of movies or details of a specific movie. 📥
```python
@app.get()
```
- **PUT:** Used to modify an existing resource. If you need to change the information of a movie, this method will be used. 🔄
```python
@app.put()
```
- **DELETE:** As the name suggests, used to delete a resource. If you want to remove a movie from the database. ❌
```python
@app.delete()
```

## The Movies API

Throughout the course, an API will be built that will provide information about movies. Here are some things that will be done:

- **Fetching all movies:** Using the GET method, data from all available movies will be requested. 🎬
- **Filtering movies:** Movies can be searched by their ID or category, using GET along with specific parameters. 🔍
- **Recording movies:** To add new movies to the database, the POST method is used. 📝
- **Modification and deletion:** The API will be completed with the ability to modify (with PUT) and delete movies (with DELETE). 🔄❌

This section of the API will also deal with the following FastAPI-specific concepts:

- **Request:** The request sent to the server by a client, which includes information about the HTTP method, headers, and body of the request. 📤
```http
GET /movies HTTP/1.1
Host: api.example.com
Content-Type: application/json
```

- **Response:** The response returned by the server to the client after processing the request, which includes the HTTP status code, headers, and body of the response. 📥
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "title": "Titanic",
  "year": 1997,
  "genre": "Romance/Drama"
}
```

- **Body:** The content of the request or response, which can be any type of data, such as text, JSON, or binary. 📦
```http
{
  "title": "Titanic",
  "year": 1997,
  "genre": "Romance/Drama"
}
```

- **Headers:** The headers of the request or response, which contain additional information about the request or response, such as the content type, body length, etc. 📑
```http
Content-Type: application/json
Content-Length: 67
```
