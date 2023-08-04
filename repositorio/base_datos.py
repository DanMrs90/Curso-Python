import sqlite3 
#se creara una conexion a la base de datos, si no existe se creara
conn=sqlite3.connect("prueba.db")

#se crea un cursor para interactuar con la  base de datos
cursor=conn.cursor()

#crear un tabla llamada usuarios con tres columnas:id,nombre,edad

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT not null,
               edad INTEGER 
)''')

#guardar los cambios y cerrar conexion
conn.commit()
conn.close()
conn=sqlite3.connect("prueba.db")
cursor=conn.cursor()
cursor.execute("insert into usuarios(nombre,edad) values(?,?)",("Juan",21))
conn.commit()
conn.close()

from fastapi import FastAPI
from pydantic import BaseModel