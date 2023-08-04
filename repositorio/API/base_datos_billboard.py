import sqlite3 
from fastapi import FastAPI
from pydantic import BaseModel
conn=sqlite3.connect("billboard.db")
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS datos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               artista TEXT NOT NULL,
               position INTEGER 
)''')
conn.commit()
conn.close()


class Datos(BaseModel):
    titulo:str
    artista:str
    posicion:str


app=FastAPI()

@app.post("/agregar/")
async def agregar_datos(datos:Datos):
    conn=sqlite3.connect("billboard.db")
    cursor=conn.cursor()
    cursor.execute("INSER INTO datos(titulo,artista,posicion) values (?,?,?)",)
    conn.commit()
    conn.close()
    return {"mensaje":"Datos agregados correctamente"}