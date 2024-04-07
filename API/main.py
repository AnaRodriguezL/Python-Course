from fastapi.responses import HTMLResponse
from fastapi import FastAPI

from config.database import engine, Base
from routers.movie import movie_router
from routers.auth import auth_router

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(movie_router)
app.include_router(auth_router)
app.title = "La super API" 
app.version = "2.0.0"

@app.get("/", tags=['home'])
def message() -> HTMLResponse:
    """
    Render the welcome message in the home page.

    Returns:
        HTMLResponse: A welcome message in HTML format.
    """
    return HTMLResponse(content="<h1> Bienvenido a mi API </h1>")
