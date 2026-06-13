from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Transaccion(BaseModel):
    id: int
    valor_unitario: float
    cantidad: int
    factura_id: int

lista_transacciones = []

@router.get("/transacciones")
def listar_transacciones():
    return {"Transacciones": lista_transacciones}

@router.get("/transacciones/{id}")
def obtener_transaccion_por_id(id: int):
    for transaccion in lista_transacciones:
        if int(transaccion.id) == int(id):
            return {"Transaccion": transaccion}
    raise HTTPException(status_code=404, detail="Transacción no encontrada")

@router.post("/transacciones")
def crear_transaccion(datos_transaccion: Transaccion):
    lista_transacciones.append(datos_transaccion)
    return {"mensaje": "Se creó la transacción con éxito"}

@router.put("/transacciones/{id}")
def editar_transaccion(id: int, datos_transaccion: Transaccion):
    posicion = 0
    for transaccion in lista_transacciones:
        if int(transaccion.id) == int(id):
            lista_transacciones[posicion] = datos_transaccion
            return {"mensaje": "Transacción actualizada correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Transacción no encontrada")

@router.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):
    posicion = 0
    for transaccion in lista_transacciones:
        if int(transaccion.id) == int(id):
            lista_transacciones.pop(posicion)
            return {"mensaje": "Transacción eliminada correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Transacción no encontrada")