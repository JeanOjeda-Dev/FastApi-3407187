from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

lista_clientes = []

# Modelo de datos de clientes
class Cliente(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None

# GET - Listar todos los clientes
@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}

# GET - Listar un solo cliente por ID
@app.get("/clientes/{id}")
def listar_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return {"Cliente": cliente}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# POST - Crear cliente
@app.post("/clientes")
def crear_clientes(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return {"mensaje": "Se creó el cliente"}

# PUT - Editar cliente
@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_cliente: Cliente):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            lista_clientes[i] = datos_cliente
            return {"mensaje": "Cliente actualizado correctamente"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# DELETE - Eliminar cliente
@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            lista_clientes.pop(i)
            return {"mensaje": "Cliente eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")