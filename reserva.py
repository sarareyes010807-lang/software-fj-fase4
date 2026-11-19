# ---------------------------------------------------------------
# reserva.py
# Clase Reserva: une un cliente, un servicio y la cantidad de horas.
# Estados posibles de una reserva: PENDIENTE, CONFIRMADA, CANCELADA
# ---------------------------------------------------------------

# Importamos la clase Cliente para poder revisar que lo que llega sea un cliente
from cliente import Cliente
# Importamos la clase base Entidad (de ella hereda Reserva)
from entidad import Entidad
# Importamos las excepciones propias que vamos a usar en este archivo
from excepciones import (ErrorSoftwareFJ, OperacionNoPermitidaError,
                         ReservaInvalidaError, ServicioNoDisponibleError)
# Importamos el log para guardar lo que pasa en el archivo software_fj.log
from logger import log
# Importamos la clase Servicio para revisar que lo que llega sea un servicio
from servicios import Servicio


# Reserva hereda de Entidad (por eso tiene un id y el metodo describir)
class Reserva(Entidad):

    # Metodo que se ejecuta al crear una reserva nueva
    def __init__(self, cliente, servicio, horas):
        super().__init__()  # Llama al constructor de Entidad para asignar el id
        # Revisamos que "cliente" sea realmente un objeto de la clase Cliente
        if not isinstance(cliente, Cliente):
            # Si no lo es, lanzamos nuestro error propio
            raise ReservaInvalidaError("Falta un cliente valido")
        # Revisamos que "servicio" sea realmente un objeto de la clase Servicio
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("Falta un servicio valido")
        # Probamos si las horas sirven para este servicio
        try:
            # Cada servicio tiene sus propias reglas de horas (polimorfismo)
            servicio.validar_horas(horas)
        # Si el servicio lanza uno de nuestros errores, lo capturamos
        except ErrorSoftwareFJ as error:
            # Encadenamiento: "from error" guarda cual fue el error original
            raise ReservaInvalidaError("No se pudo crear la reserva") from error
        self.cliente = cliente    # Guardamos el cliente de la reserva
        self.servicio = servicio  # Guardamos el servicio reservado
        self.horas = horas        # Guardamos la cantidad de horas
        self.estado = "PENDIENTE" # Toda reserva nueva empieza como PENDIENTE

    # Metodo para confirmar la reserva
    def confirmar(self):
        # Solo se puede confirmar si esta PENDIENTE
        if self.estado != "PENDIENTE":
            raise OperacionNoPermitidaError("No se puede confirmar, estado: " + self.estado)
        # Si el servicio esta apagado (disponible = False) no se puede confirmar
        if not self.servicio.disponible:
            raise ServicioNoDisponibleError("El servicio " + self.servicio.nombre + " no esta disponible")
        self.estado = "CONFIRMADA"  # Cambiamos el estado
        # Guardamos en el log que la reserva fue confirmada
        log.info("Reserva " + str(self.id) + " confirmada")

    # Metodo para cancelar la reserva
    def cancelar(self):
        # No tiene sentido cancelar una reserva que ya esta cancelada
        if self.estado == "CANCELADA":
            raise OperacionNoPermitidaError("La reserva ya estaba cancelada")
        self.estado = "CANCELADA"  # Cambiamos el estado
        log.info("Reserva " + str(self.id) + " cancelada")  # Lo anotamos en el log

    # Metodo que confirma la reserva y calcula cuanto cuesta
    def procesar(self, descuento=0):
        # try: aqui ponemos lo que puede fallar
        try:
            self.confirmar()  # Puede lanzar un error si no se puede confirmar
            # Calcula el costo con el descuento recibido
            total = self.servicio.calcular_costo(self.horas, descuento=descuento)
        # except: se ejecuta si hubo un error de los nuestros
        except ErrorSoftwareFJ as error:
            # Anotamos el error en el log
            log.error("Reserva " + str(self.id) + " fallo: " + str(error))
            raise  # Volvemos a lanzar el error para que lo vea quien llamo
        # else: se ejecuta solo si NO hubo ningun error
        else:
            log.info("Reserva " + str(self.id) + " procesada, total: " + str(total))
            return total  # Devolvemos el total a pagar
        # finally: se ejecuta siempre, haya o no error
        finally:
            log.info("Fin de procesar la reserva " + str(self.id))

    # Metodo que devuelve un texto con los datos de la reserva
    def describir(self):
        return ("Reserva " + str(self.id) + " [" + self.estado + "] "
                + self.cliente.get_nombre() + " - " + self.servicio.nombre
                + " por " + str(self.horas) + " horas")
