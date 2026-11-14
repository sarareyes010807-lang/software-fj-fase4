
"""
Modulo de servicios de Software FJ.
Contiene la clase abstracta Servicio y sus tres servicios especializados.
"""

from abc import ABC, abstractmethod
import logging


# Importar la excepcion general del proyecto
try:
    from excepciones import ErrorSoftwareFJ
except ImportError:
    class ErrorSoftwareFJ(Exception):
        """Excepcion general de respaldo."""
        pass


class ErrorServicio(ErrorSoftwareFJ):
    """Error relacionado con la gestion de servicios."""
    pass


class Servicio(ABC):
    """Clase abstracta que representa un servicio."""

    def __init__(self, nombre, descripcion, precio_base):
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio_base = self._validar_numero(
            precio_base, "El precio base"
        )

    @staticmethod
    def _validar_numero(valor, campo):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ErrorServicio(f"{campo} debe ser numerico.")

        if valor < 0:
            raise ErrorServicio(f"{campo} no puede ser negativo.")

        return float(valor)

    @property
    def nombre(self):
        return self._nombre

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Devuelve la descripcion del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self):
        """Valida los datos particulares del servicio."""
        pass

    def calcular_costo_detallado(self, cantidad=1, impuesto=0,
                                 descuento=0):
        """Calcula el costo con impuestos y descuentos opcionales."""
        subtotal = self.calcular_costo(cantidad)

        impuesto = self._validar_numero(impuesto, "El impuesto")
        descuento = self._validar_numero(descuento, "El descuento")

        if impuesto > 100 or descuento > 100:
            raise ErrorServicio(
                "El impuesto y el descuento deben estar entre 0 y 100."
            )

        total = subtotal + subtotal * impuesto / 100
        total -= subtotal * descuento / 100

        return round(total, 2)


class ReservaSala(Servicio):
    """Servicio especializado en reservas de salas."""

    def __init__(self, nombre, precio_base, capacidad,
                 descripcion="Reserva de sala"):
        super().__init__(nombre, descripcion, precio_base)
        self._capacidad = capacidad
        self.validar_parametros()

    def validar_parametros(self):
        if isinstance(self._capacidad, bool) or not isinstance(
            self._capacidad, int
        ):
            raise ErrorServicio("La capacidad debe ser un numero entero.")

        if self._capacidad <= 0:
            raise ErrorServicio("La capacidad debe ser mayor que cero.")

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):
        cantidad = self._validar_numero(cantidad, "Las horas")

        if cantidad <= 0:
            raise ErrorServicio("Las horas deben ser mayores que cero.")

        return round(self._precio_base * cantidad, 2)

    def describir_servicio(self):
        return (
            f"{self._nombre}: {self._descripcion}. "
            f"Capacidad: {self._capacidad} personas. "
            f"Precio por hora: ${self._precio_base:.2f}"
        )


class AlquilerEquipo(Servicio):
    """Servicio especializado en alquiler de equipos."""

    def __init__(self, nombre, precio_base, cantidad_disponible,
                 descripcion="Alquiler de equipos"):
        super().__init__(nombre, descripcion, precio_base)
        self._cantidad_disponible = cantidad_disponible
        self.validar_parametros()

    def validar_parametros(self):
        if isinstance(self._cantidad_disponible, bool) or not isinstance(
            self._cantidad_disponible, int
        ):
            raise ErrorServicio(
                "La cantidad disponible debe ser un numero entero."
            )

        if self._cantidad_disponible < 0:
            raise ErrorServicio(
                "La cantidad disponible no puede ser negativa."
            )

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ErrorServicio("La cantidad de equipos debe ser entera.")

        if cantidad <= 0:
            raise ErrorServicio("Debe alquilar al menos un equipo.")

        if cantidad > self._cantidad_disponible:
            raise ErrorServicio("No hay suficientes equipos disponibles.")

        return round(self._precio_base * cantidad, 2)

    def describir_servicio(self):
        return (
            f"{self._nombre}: {self._descripcion}. "
            f"Disponibles: {self._cantidad_disponible}. "
            f"Precio por equipo: ${self._precio_base:.2f}"
        )


class Asesoria(Servicio):
    """Servicio especializado en asesorias."""

    def __init__(self, nombre, precio_base, especialidad,
                 descripcion="Asesoria especializada"):
        super().__init__(nombre, descripcion, precio_base)
        self._especialidad = especialidad
        self.validar_parametros()

    def validar_parametros(self):
        if not isinstance(self._especialidad, str):
            raise ErrorServicio("La especialidad debe ser texto.")

        if not self._especialidad.strip():
            raise ErrorServicio("Debe indicar una especialidad.")

    def calcular_costo(self, cantidad=1, impuesto=0, descuento=0):
        cantidad = self._validar_numero(cantidad, "Las horas")

        if cantidad <= 0:
            raise ErrorServicio("Las horas deben ser mayores que cero.")

        return round(self._precio_base * cantidad, 2)

    def describir_servicio(self):
        return (
            f"{self._nombre}: {self._descripcion}. "
            f"Especialidad: {self._especialidad}. "
            f"Tarifa por hora: ${self._precio_base:.2f}"
        )
