from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Importamos los routers de los otros archivos
from facturas import router as router_facturas
from transacciones import router as router_transacciones

app = FastAPI()

# Incluimos las rutas de los otros archivos en la aplicación principal
app.include_router(router_facturas)
app.include_router(router_transacciones)

class Cliente(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None

lista_clientes = []

@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}

@app.get("/clientes/{id}")
def obtener_cliente_por_id(id: int):
    for cliente in lista_clientes:
        if int(cliente.id) == int(id):
            return {"Cliente": cliente}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return {"mensaje": "Se creó el cliente con éxito"}

@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_cliente: Cliente):
    posicion = 0
    for cliente in lista_clientes:
        if int(cliente.id) == int(id):
            lista_clientes[posicion] = datos_cliente
            return {"mensaje": "Cliente actualizado correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    posicion = 0
    for cliente in lista_clientes:
        if int(cliente.id) == int(id):
            lista_clientes.pop(posicion)
            return {"mensaje": "Cliente eliminado correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Cliente no encontrado")