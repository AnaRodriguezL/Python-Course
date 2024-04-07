from schemas.movie import Movie
from models.movie import Movie as MovieModel

class MovieService():
    """
    Movie Service constructor

    Parameters
    ----------
    db : sqlalchemy.orm.Session
        Database session
    """
    def __init__(self, db):
        """
        Initialize Movie Service class

        Parameters
        ----------
        db : sqlalchemy.orm.Session
            Database session
        """
        self.db = db

    def get_movies(self):
        """
        Return all movies from database

        Returns
        -------
        list
            A list of all movies
        """
        return self.db.query(MovieModel).all()

    # Get a movie from database by its id
    #
    # Parameters
    # ----------
    # id : int
    #     Movie's id
    #
    # Returns
    # -------
    # MovieModel
    #     A movie with the given id or None if it doesn't exist
    def get_movie(self, id: int):
        """
        Get a movie from database by its id

        Parameters
        ----------
        id : int
            Movie's id

        Returns
        -------
        MovieModel
            A movie with the given id or None if it doesn't exist
        """
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()
    
    def get_movies_by_category(self, category: str) -> List[MovieModel]:
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
        return self.db.query(MovieModel).filter(MovieModel.category == category).all()
    
    # Add a new movie to database
    #
    # Parameters
    # ----------
    # movie : Movie
    #     Movie's attributes
    #
    # Returns
    # -------
    # None
    def create_movie(self, movie:Movie):
        """
        Add a new movie to database

        Parameters
        ----------
        movie : Movie
            Movie's attributes
        """
        new_movie = MovieModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()

    # Update a movie from database
    #
    # Parameters
    # ----------
    # movie : MovieModel
    #     Movie to update
    # data : Movie
    #     New values for the movie
    #
    # Returns
    # -------
    # None
    def update_movie(self, movie: MovieModel, data: Movie):
        """
        Update a movie from database

        Parameters
        ----------
        movie : MovieModel
            Movie to update
        data : Movie
            New values for the movie
        """
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()

    # Delete a movie from database
    #
    # Parameters
    # ----------
    # movie : MovieModel
    #     Movie to delete
    #
    # Returns
    # -------
    # None
    def delete_movie(self, movie: MovieModel):
        """
        Delete a movie from database

        Parameters
        ----------
        movie : MovieModel
            Movie to delete
        """
        self.db.delete(movie)
        self.db.commit()
