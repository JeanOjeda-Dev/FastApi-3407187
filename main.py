from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 1. DEFINIMOS EL MODELO DE DATOS
class Cliente(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None

# 2. NUESTRA BASE DE DATOS SIMULADA (EMPIEZA VACÍA)
lista_clientes = []


# 3. RUTA PARA VER TODOS LOS CLIENTES (GET)
@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}


# 4. RUTA PARA BUSCAR UN SOLO CLIENTE POR ID (GET)
@app.get("/clientes/{id}")
def obtener_cliente_por_id(id: int):
    for cliente in lista_clientes:
        # Forzamos a que se comparen como enteros puros
        if int(cliente.id) == int(id):
            return {"Cliente": cliente}
            
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# 5. RUTA PARA CREAR UN NUEVO CLIENTE (POST)
@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return {"mensaje": "Se creó el cliente con éxito"}


# 6. RUTA PARA EDITAR UN CLIENTE (PUT)
@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_cliente: Cliente):
    posicion = 0
    for cliente in lista_clientes:
        if int(cliente.id) == int(id):
            lista_clientes[posicion] = datos_cliente
            return {"mensaje": "Cliente actualizado correctamente"}
        posicion = posicion + 1
        
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# 7. RUTA PARA ELIMINAR UN CLIENTE (DELETE)
@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    posicion = 0
    for cliente in lista_clientes:
        if int(cliente.id) == int(id):
            lista_clientes.pop(posicion)
            return {"mensaje": "Cliente eliminado correctamente"}
        posicion = posicion + 1
        
    raise HTTPException(status_code=404, detail="Cliente no encontrado")