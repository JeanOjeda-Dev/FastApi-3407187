from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista_clientes = []

#datos de clientes
class Cliente(BaseModel):
    id : int
    nombre : str
    descripcion : str | None = None

# RUTA PARA LEER (GET) - Devuelve todos los clientes registrados en la lista
@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}


    
#Busca un cliente por su posición (índice) en la lista
@app.get("/clientes/{id}")
def listar_cliente(id: int):
    return {"Cliente": lista_clientes[id]}


#Recibe los datos de un nuevo cliente y los guarda en la lista
@app.post("/clientes")
def crear_clientes(datos_cliente : Cliente):
    lista_clientes.append(datos_cliente)
    return {"mensaje": "Se creo el cliente"}




#Reemplaza los datos de un cliente en una posición específica
@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_cliente : Cliente):
    lista_clientes[id] = datos_cliente
    return {"mensaje": "Se edito el cliente"}



#Borra un cliente de la lista usando su posición
@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    lista_clientes.pop(id)
    return {"mensaje": "Se elimino el cliente"}