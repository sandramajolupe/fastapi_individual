from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine,Base

from middlewares.error_handler import Errorhandler

from routers.product import product_router
from routers.supplier import supplier_router
from routers.supplies import supplies_router


app = FastAPI()
app.title = "My inventory project FastAPI"
app.version = "0.0.1"

app.add_middleware(Errorhandler)
app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(supplies_router)


Base.metadata.create_all(bind=engine)


@app.get('/',tags=['home'],status_code=200)
def message():
    return HTMLResponse('<h1>Hello developers</h1>')

@app.get('/hola',tags=['home'])
def hola():
    return HTMLResponse('<h1>Hola people</h1>')