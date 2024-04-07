from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Path, Query, Depends

from schemas.movie import Movie
from config.database import Session
from services.movie import MovieService
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie as MovieModel

movie_router = APIRouter()

@movie_router.get("/movies", tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    """
    Return all movies from database

    Returns
    -------
    list
        A list of all movies
    """
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get("/movies/{id}", tags=['movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=2000, description="Movie's id")):
    """
    Get a movie from database by its id

    Parameters
    ----------
    id : int
        Movie's id

    Returns
    -------
    Movie
        A movie with the given id or None if it doesn't exist
    """
    db = Session()
    result = MovieService(db).get_movie(id)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Movie not found"}, status_code=404)
    return result


@movie_router.get("/movies/", tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=3, max_length=15)) -> List[Movie]:
    """
    Return all movies from a specific category

    Parameters
    ----------
    category : str
        Movie's category

    Returns
    -------
    list
        A list of movies of the given category
    """
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Movies not found"}, status_code=404)
    return result


@movie_router.post("/movies", tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    """
    Create a new movie in the database

    Parameters
    ----------
    movie : Movie
        A movie to be added to the database

    Returns
    -------
    dict
        A dictionary with a message indicating that the movie was created

    """
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "Movie created successfully"}, status_code=201)

@movie_router.put("/movies/{id}", tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    """
    Update a movie in the database

    Parameters
    ----------
    id : int
        Movie's id
    movie : Movie
        Movie's attributes to be updated

    Returns
    -------
    dict
        A dictionary with a message indicating that the movie was updated
    """
    db = Session()
    movie_to_update = MovieService(db).get_movie(id)
    if not movie_to_update:
        response = JSONResponse(content={"message": "Movie not found"}, status_code=404)
    else:
        MovieService(db).update_movie(movie_to_update, movie)
        response = JSONResponse(content={"message": "Movie updated successfully"}, status_code=200)
    return response

@movie_router.delete("/movies/{id}", tags=['movies'], response_model=dict, dependencies=[Depends(JWTBearer())])
def delete_movie(id: int) -> dict:
    """
    Delete a movie from the database

    Parameters
    ----------
    id : int
        Movie's id

    Returns
    -------
    dict
        A dictionary with a message indicating that the movie was deleted
    """
    db = Session()
    movie = MovieService(db).get_movie(id)
    if not movie:
        # If the movie doesn't exist
        response = JSONResponse(content={"message": "Movie not found"}, status_code=404)
    else:
        # If the movie exists
        MovieService(db).delete_movie(movie)
        response = JSONResponse(content={"message": "Movie deleted successfully"})
    return response
