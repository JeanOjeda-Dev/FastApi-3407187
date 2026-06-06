from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()



class Cliente(BaseModel):
    id: int
    nombre: str
    descripcion: str | None = None

class Factura(BaseModel):
    id: int
    fecha: str
    valor_total: float
    cliente: str  # Guardamos el nombre del cliente o su ID como texto

class Transaccion(BaseModel):
    id: int
    vr_unitario: float
    cantidad: int
    factura_id: int



lista_clientes = []
lista_facturas = []
lista_transacciones = []




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



@app.get("/facturas")
def listar_facturas():
    return {"Facturas": lista_facturas}

@app.get("/facturas/{id}")
def obtener_factura_por_id(id: int):
    for factura in lista_facturas:
        if int(factura.id) == int(id):
            return {"Factura": factura}
    raise HTTPException(status_code=404, detail="Factura no encontrada")

@app.post("/facturas")
def crear_factura(datos_factura: Factura):
    lista_facturas.append(datos_factura)
    return {"mensaje": "Se creó la factura con éxito"}

@app.put("/facturas/{id}")
def editar_factura(id: int, datos_factura: Factura):
    posicion = 0
    for factura in lista_facturas:
        if int(factura.id) == int(id):
            lista_facturas[posicion] = datos_factura
            return {"mensaje": "Factura actualizada correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Factura no encontrada")

@app.delete("/facturas/{id}")
def eliminar_factura(id: int):
    posicion = 0
    for factura in lista_facturas:
        if int(factura.id) == int(id):
            lista_facturas.pop(posicion)
            return {"mensaje": "Factura eliminada correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Factura no encontrada")




@app.get("/transacciones")
def listar_transacciones():
    return {"Transacciones": lista_transacciones}

@app.get("/transacciones/{id}")
def obtener_transaccion_por_id(id: int):
    for transaccion in lista_transacciones:
        if int(transaccion.id) == int(id):
            return {"Transaccion": transaccion}
    raise HTTPException(status_code=404, detail="Transacción no encontrada")

@app.post("/transacciones")
def crear_transaccion(datos_transaccion: Transaccion):
    lista_transacciones.append(datos_transaccion)
    return {"mensaje": "Se creó la transacción con éxito"}

@app.put("/transacciones/{id}")
def editar_transaccion(id: int, datos_transaccion: Transaccion):
    posicion = 0
    for transaccion in lista_transacciones:
        if int(transaccion.id) == int(id):
            lista_transacciones[posicion] = datos_transaccion
            return {"mensaje": "Transacción actualizada correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Transacción no encontrada")

@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):
    posicion = 0
    for transaccion in lista_transacciones:
        if int(transaccion.id) == int(id):
            lista_transacciones[posicion] = transaccion
            lista_transacciones.pop(posicion)
            return {"mensaje": "Transacción eliminada correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Transacción no encontrada")