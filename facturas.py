from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Factura(BaseModel):
    id: int
    fecha: str
    valor_total: float
    cliente: str  # Guardamos el nombre del cliente o su ID como texto

lista_facturas = []

@router.get("/facturas")
def listar_facturas():
    return {"Facturas": lista_facturas}

@router.get("/facturas/{id}")
def obtener_factura_por_id(id: int):
    for factura in lista_facturas:
        if int(factura.id) == int(id):
            return {"Factura": factura}
    raise HTTPException(status_code=404, detail="Factura no encontrada")

@router.post("/facturas")
def crear_factura(datos_factura: Factura):
    lista_facturas.append(datos_factura)
    return {"mensaje": "Se creó la factura con éxito"}

@router.put("/facturas/{id}")
def editar_factura(id: int, datos_factura: Factura):
    posicion = 0
    for factura in lista_facturas:
        if int(factura.id) == int(id):
            lista_facturas[posicion] = datos_factura
            return {"mensaje": "Factura actualizada correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Factura no encontrada")

@router.delete("/facturas/{id}")
def eliminar_factura(id: int):
    posicion = 0
    for factura in lista_facturas:
        if int(factura.id) == int(id):
            lista_facturas.pop(posicion)
            return {"mensaje": "Factura eliminada correctamente"}
        posicion = posicion + 1
    raise HTTPException(status_code=404, detail="Factura no encontrada")