from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = ("Mi super API")
app.version = "V1.0.0"

@app.get("/", tags=['home'])

def message():
    return HTMLResponse(
        content = "<h1>¡Hola Mundo!</h1>"
    )

