from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse


genres_router = APIRouter()

@genres_router.get('/genres_hello', tags=['genres'], status_code=200)
def get_genres_hello():
    """function to check the route"""
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')

@genres_router.get('/genres', tags = ['genres'], status_code=200)
def get_genres():
    #funcion que trae todos los generos que esta en servicios
    return JSONResponse(content={'message':'estos son los generos'})

@genres_router.post('/genres', tags=['genres'], status_code=201)
def create_genres():
    #llamar una funcion que va a estar en el servicios 
    return JSONResponse(content={"message":"genre created successfully"})

#creamos un get que trae un solo genero por id 

# para el genres delete debemos verificar que el id existe y despues ese genero lo eliminamos


