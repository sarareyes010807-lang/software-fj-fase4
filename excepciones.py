"""Módulo de excepciones personalizadas del sistema."""

class SistemaFJError(Exception):
    """Error base del sistema."""
    pass

class ValidacionError(SistemaFJError):
    """Error de validación de datos."""
    pass

class DatoInvalidoError(ValidacionError):
    """Error cuando un dato es inválido."""
    pass

class ParametroFaltanteError(ValidacionError):
    """Error cuando falta un parámetro."""
    pass

class OperacionNoPermitidaError(SistemaFJError):
    """Error cuando una operación no está permitida."""
    pass

class ClienteNoEncontradoError(SistemaFJError):
    """Error cuando no se encuentra el cliente."""
    pass

class ServicioNoEncontradoError(SistemaFJError):
    """Error cuando no se encuentra el servicio."""
    pass

class ReservaNoEncontradaError(SistemaFJError):
    """Error cuando no se encuentra la reserva."""
    pass

class ReservaError(SistemaFJError):
    """Error general de reserva."""
    pass

class EstadoReservaError(ReservaError):
    """Error de estado de la reserva."""
    pass

class CalculoCostoError(SistemaFJError):
    """Error en el cálculo del costo."""
    pass
