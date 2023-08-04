from  fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()


class Libro(BaseModel):
    titulo:str
    autor:str
    paginas:int
    editorial:Optional[str]

@app.get("/")
async def raiz():
    return {"Hola":"Mundo"}

@app.get("/libros/{id}")
async def mostrar_libros(id:int):
    return{"data":id}

@app.post("/libros/")
async def insertar_libro(libro:Libro):
    return{f"El libro {libro.titulo} se ha insertado correctamente"}


@app.get("/items/{item_id}/{m}")
def read_item(item_id,m:str=None):
    return {"Item id":item_id,"m":m}