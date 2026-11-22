# reserva.py
# Clase Reserva: une un cliente, un servicio y la cantidad (horas o unidades).
# Estados posibles: PENDIENTE, CONFIRMADA, CANCELADA

# Traemos las clases y funciones que necesitamos de los otros archivos
from cliente import Cliente
from entidad import Entidad
from excepciones import (CalculoCostoError, EstadoReservaError,
                         ReservaError, SistemaFJError)
from logger import crear_log
from servicios import ErrorServicio, Servicio


# Reserva hereda de Entidad (por eso tiene id y el metodo describir)
class Reserva(Entidad):

    def __init__(self, cliente, servicio, cantidad):
        super().__init__()  # asigna el id
        # Revisamos que el cliente sea realmente un Cliente
        if not isinstance(cliente, Cliente):
            raise ReservaError("Falta un cliente valido")
        # Revisamos que el servicio sea realmente un Servicio
        if not isinstance(servicio, Servicio):
            raise ReservaError("Falta un servicio valido")
        # La cantidad (horas o unidades) debe ser un numero mayor que cero
        if isinstance(cantidad, bool) or not isinstance(cantidad, (int, float)) or cantidad <= 0:
            raise ReservaError("La cantidad debe ser un numero mayor que cero")
        # Probamos que el servicio este bien configurado
        try:
            servicio.validar_parametros()
        except ErrorServicio as error:
            # Encadenamiento: "from error" guarda cual fue el error original
            raise ReservaError("No se pudo crear la reserva") from error
        self.cliente = cliente      # cliente que reserva
        self.servicio = servicio    # servicio reservado
        self.cantidad = cantidad    # horas o unidades reservadas
        self.estado = "PENDIENTE"   # toda reserva nueva empieza PENDIENTE

    # Confirma la reserva
    def confirmar(self):
        # Solo se puede confirmar si esta PENDIENTE
        if self.estado != "PENDIENTE":
            raise EstadoReservaError("No se puede confirmar, estado actual: " + self.estado)
        self.estado = "CONFIRMADA"
        crear_log("Reserva " + str(self.id) + " confirmada", "info")

    # Cancela la reserva
    def cancelar(self):
        # No se puede cancelar dos veces
        if self.estado == "CANCELADA":
            raise EstadoReservaError("La reserva ya estaba cancelada")
        self.estado = "CANCELADA"
        crear_log("Reserva " + str(self.id) + " cancelada", "info")

    # Calcula el costo y confirma la reserva
    # impuesto y descuento van en porcentaje (por ejemplo 19 es 19%)
    def procesar(self, impuesto=0, descuento=0):
        # try: aqui ponemos lo que puede fallar
        try:
            try:
                # Primero calculamos el costo con el servicio (polimorfismo)
                total = self.servicio.calcular_costo_detallado(self.cantidad, impuesto, descuento)
            except ErrorServicio as error:
                # Encadenamiento de excepciones: guardamos el error original
                raise CalculoCostoError("No se pudo calcular el costo") from error
            self.confirmar()  # si el costo salio bien, confirmamos
        # except: se ejecuta si hubo un error de los del sistema
        except SistemaFJError as error:
            crear_log("Reserva " + str(self.id) + " fallo: " + str(error), "error")
            raise  # volvemos a lanzar el error para que lo vea quien llamo
        # else: se ejecuta solo si NO hubo error
        else:
            crear_log("Reserva " + str(self.id) + " procesada, total: " + str(total), "info")
            return total
        # finally: se ejecuta siempre
        finally:
            crear_log("Fin de procesar la reserva " + str(self.id), "info")

    def describir(self):
        return ("Reserva " + str(self.id) + " [" + self.estado + "] "
                + self.cliente.get_nombre() + " - " + self.servicio.nombre
                + " x " + str(self.cantidad))
