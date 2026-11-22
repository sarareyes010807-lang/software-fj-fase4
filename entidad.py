# entidad.py
# Clase abstracta general del sistema.
# De ella heredan Cliente y Reserva.

from abc import ABC, abstractmethod


class Entidad(ABC):
    contador = 0  # cuenta cuantos objetos se han creado

    def __init__(self):
        Entidad.contador += 1       # sumamos uno al contador
        self.id = Entidad.contador  # cada objeto queda con un id diferente

    @abstractmethod
    def describir(self):
        """Cada clase hija debe explicar como se describe."""
        pass

    def __str__(self):
        # Al imprimir el objeto se muestra su descripcion
        return self.describir()
