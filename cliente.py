# cliente.py
# Clase Cliente: guarda los datos personales (privados) y los valida.

from entidad import Entidad
from excepciones import DatoInvalidoError, ParametroFaltanteError


class Cliente(Entidad):

    def __init__(self, nombre, documento, correo, telefono):
        super().__init__()  # asigna el id
        # Primero revisamos que ningun dato venga vacio
        datos = [(nombre, "nombre"), (documento, "documento"),
                 (correo, "correo"), (telefono, "telefono")]
        for dato, campo in datos:
            if dato is None or str(dato).strip() == "":
                raise ParametroFaltanteError("Falta el dato: " + campo)

        # Luego validamos cada dato
        if len(nombre) < 3:
            raise DatoInvalidoError("El nombre es muy corto: " + nombre)
        if not documento.isdigit() or len(documento) < 6:
            raise DatoInvalidoError("Documento invalido: " + documento)
        if "@" not in correo or "." not in correo:
            raise DatoInvalidoError("Correo invalido: " + correo)
        if not telefono.isdigit() or len(telefono) != 10:
            raise DatoInvalidoError("El telefono debe tener 10 digitos: " + telefono)

        # Atributos privados (encapsulacion): se leen con los metodos get
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def describir(self):
        return "Cliente " + str(self.id) + ": " + self.__nombre + " (" + self.__correo + ")"
