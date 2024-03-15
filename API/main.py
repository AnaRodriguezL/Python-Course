from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = ("Mi super API")
app.version = "V1.0.0"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': 'Simios azules extraterrestres que pelean con el poder de la naturaleza',
        'year': 2009,
        'rating': 9.1,
        'category': 'fiction'
    },
    {
        'id': 2,
        'title': 'Pirates of the Caribe 1',
        'overview': 'Película que trata sobre piratas',
        'year': 2003,
        'rating': 7.2,
        'category': 'pirates'
    },
     {
        'id': 3,
        'title': 'Piratas del caribe: el cofre de la muerte',
        'overview': 'Película que trata sobre piratas',
        'year': 2006,
        'rating': 6.4,
        'category': 'pirates'
    }
]

@app.get("/", tags=['home'])

def message():
    return HTMLResponse(
        content = "<h1>¡Hola Mundo!</h1>"
    )

# Consumiendo la información con respecto a una ruta en especifico
@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

# Definiendo parámetros dentro de la ruta
@app.get('/movies/{id}', tags=['movies'])
def get_movies(id: int):
    for movie in movies:
        # Si encuentra la película con el id lo retorna
        if movie['id'] == id:
            return movie
    # Si no, retorna una lista vacía
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str):
    movies_filter = []
    for movie in movies:
        if movie['category'] == category:
            movies_filter.append(movie)
    return movies_filter

# Añadir datos al diccionario de 'movies'
@app.post('/movies', tags=['movies'])
def post_movies(id: int, title: str, overview: str, year: int, rating: int, category: str):
    return {"id": id, "title": title, "overview": overview, "year": year, "rating": rating, "category": category}