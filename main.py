
from fastapi import FastAPI, HTTPException


from pydantic import BaseModel

app = FastAPI()



class Cliente(BaseModel):

    id: int
    nombre: str
    descripcion: str | None = None


# Modelo para representar una factura
class Factura(BaseModel):

    id: int
    fecha: str
    valor_total: float
    cliente: str


# Modelo para representar una transacción
class Transaccion(BaseModel):

    id: int
    vr_unitario: float
    cantidad: int
    factura_id: int


lista_clientes = []
lista_facturas = []
lista_transacciones = []


# Endpoint GET para obtener todos los clientes
@app.get("/clientes")
def listar_clientes():
    return {"Clientes": lista_clientes}


# Endpoint GET para buscar un cliente por ID
@app.get("/clientes/{id}")
def obtener_cliente_por_id(id: int):
    for cliente in lista_clientes:
        if int(cliente.id) == int(id):

            # Retorna el cliente encontrado
            return {"Cliente": cliente}

    # Si no encuentra el cliente, genera un error 404
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# Endpoint POST para crear un cliente
@app.post("/clientes")
def crear_cliente(datos_cliente: Cliente):

    # Agrega el cliente a la lista
    lista_clientes.append(datos_cliente)

    # Retorna mensaje de éxito
    return {"mensaje": "Se creó el cliente con éxito"}


# Endpoint PUT para actualizar un cliente existente
@app.put("/clientes/{id}")
def editar_cliente(id: int, datos_cliente: Cliente):

    # Variable para almacenar la posición del cliente
    posicion = 0

    # Recorre todos los clientes
    for cliente in lista_clientes:

        # Verifica si el ID coincide
        if int(cliente.id) == int(id):

            # Reemplaza el cliente por los nuevos datos
            lista_clientes[posicion] = datos_cliente

            # Retorna mensaje de éxito
            return {"mensaje": "Cliente actualizado correctamente"}

        # Avanza a la siguiente posición
        posicion = posicion + 1

    # Error si no existe el cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# Endpoint DELETE para eliminar un cliente
@app.delete("/clientes/{id}")
def eliminar_cliente(id: int):

    # Inicializa la posición
    posicion = 0

    # Recorre la lista de clientes
    for cliente in lista_clientes:

        # Busca coincidencia de ID
        if int(cliente.id) == int(id):

            # Elimina el cliente encontrado
            lista_clientes.pop(posicion)

            # Retorna mensaje de éxito
            return {"mensaje": "Cliente eliminado correctamente"}

        # Incrementa la posición
        posicion = posicion + 1

    # Error si no existe el cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# Endpoint GET para listar todas las facturas
@app.get("/facturas")
def listar_facturas():

    # Retorna la lista de facturas
    return {"Facturas": lista_facturas}


# Endpoint GET para obtener una factura por ID
@app.get("/facturas/{id}")
def obtener_factura_por_id(id: int):

    # Recorre las facturas almacenadas
    for factura in lista_facturas:

        # Verifica si coincide el ID
        if int(factura.id) == int(id):

            # Retorna la factura encontrada
            return {"Factura": factura}

    # Error si no se encuentra
    raise HTTPException(status_code=404, detail="Factura no encontrada")


# Endpoint POST para crear una factura
@app.post("/facturas")
def crear_factura(datos_factura: Factura):

    # Agrega la factura a la lista
    lista_facturas.append(datos_factura)

    # Retorna mensaje de éxito
    return {"mensaje": "Se creó la factura con éxito"}


# Endpoint PUT para actualizar una factura
@app.put("/facturas/{id}")
def editar_factura(id: int, datos_factura: Factura):

    # Inicializa la posición
    posicion = 0

    # Recorre las facturas
    for factura in lista_facturas:

        # Busca coincidencia por ID
        if int(factura.id) == int(id):

            # Actualiza la factura
            lista_facturas[posicion] = datos_factura

            # Retorna mensaje de éxito
            return {"mensaje": "Factura actualizada correctamente"}

        # Incrementa la posición
        posicion = posicion + 1

    # Error si no existe la factura
    raise HTTPException(status_code=404, detail="Factura no encontrada")


# Endpoint DELETE para eliminar una factura
@app.delete("/facturas/{id}")
def eliminar_factura(id: int):

    # Inicializa la posición
    posicion = 0

    # Recorre las facturas
    for factura in lista_facturas:

        # Busca la factura por ID
        if int(factura.id) == int(id):

            # Elimina la factura
            lista_facturas.pop(posicion)

            # Retorna mensaje de éxito
            return {"mensaje": "Factura eliminada correctamente"}

        # Incrementa la posición
        posicion = posicion + 1

    # Error si no existe la factura
    raise HTTPException(status_code=404, detail="Factura no encontrada")


# Endpoint GET para listar todas las transacciones
@app.get("/transacciones")
def listar_transacciones():

    # Retorna la lista de transacciones
    return {"Transacciones": lista_transacciones}


# Endpoint GET para obtener una transacción por ID
@app.get("/transacciones/{id}")
def obtener_transaccion_por_id(id: int):

    # Recorre las transacciones
    for transaccion in lista_transacciones:

        # Verifica coincidencia del ID
        if int(transaccion.id) == int(id):

            # Retorna la transacción encontrada
            return {"Transaccion": transaccion}

    # Error si no existe
    raise HTTPException(status_code=404, detail="Transacción no encontrada")


# Endpoint POST para crear una transacción
@app.post("/transacciones")
def crear_transaccion(datos_transaccion: Transaccion):

    # Agrega la transacción a la lista
    lista_transacciones.append(datos_transaccion)

    # Retorna mensaje de éxito
    return {"mensaje": "Se creó la transacción con éxito"}


# Endpoint PUT para actualizar una transacción
@app.put("/transacciones/{id}")
def editar_transaccion(id: int, datos_transaccion: Transaccion):

    # Inicializa la posición
    posicion = 0

    # Recorre las transacciones
    for transaccion in lista_transacciones:

        # Busca coincidencia por ID
        if int(transaccion.id) == int(id):

            # Actualiza la transacción
            lista_transacciones[posicion] = datos_transaccion

            # Retorna mensaje de éxito
            return {"mensaje": "Transacción actualizada correctamente"}

        # Incrementa la posición
        posicion = posicion + 1

    # Error si no existe la transacción
    raise HTTPException(status_code=404, detail="Transacción no encontrada")


# Endpoint DELETE para eliminar una transacción
@app.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):

    # Inicializa la posición
    posicion = 0

    # Recorre las transacciones
    for transaccion in lista_transacciones:

        # Busca coincidencia por ID
        if int(transaccion.id) == int(id):

            # Guarda la transacción en la posición actual
            lista_transacciones[posicion] = transaccion

            # Elimina la transacción
            lista_transacciones.pop(posicion)

            # Retorna mensaje de éxito
            return {"mensaje": "Transacción eliminada correctamente"}

        # Incrementa la posición
        posicion = posicion + 1

    # Error si no existe la transacción
    raise HTTPException(status_code=404, detail="Transacción no encontrada")