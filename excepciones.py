# Excepciones propias del proyecto Software FJ.
# Todas heredan de ErrorSoftwareFJ para poder capturarlas juntas.

class ErrorSoftwareFJ(Exception):
    """Error general del programa."""
    pass


class DatoFaltanteError(ErrorSoftwareFJ):
    """Falta un dato obligatorio (esta vacio)."""
    pass


class ClienteInvalidoError(ErrorSoftwareFJ):
    """Un dato del cliente no es valido."""
    pass


class ServicioInvalidoError(ErrorSoftwareFJ):
    """Un dato del servicio no es valido."""
    pass


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """El servicio no esta disponible."""
    pass


class ReservaInvalidaError(ErrorSoftwareFJ):
    """No se pudo crear la reserva."""
    pass


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """La operacion no se puede hacer en el estado actual."""
    pass
