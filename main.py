# Programa principal: simula 15 operaciones (validas e invalidas).
# Si una operacion falla, el programa sigue con la siguiente.

from cliente import Cliente
from excepciones import ErrorSoftwareFJ
from logger import log
from reserva import Reserva
from servicios import Asesoria, AlquilerEquipo, ReservaSala


def ejecutar(numero, descripcion, operacion):
    """Ejecuta una operacion y muestra si salio bien o mal."""
    print("\n" + str(numero) + ". " + descripcion)
    log.info("Operacion " + str(numero) + ": " + descripcion)
    try:
        resultado = operacion()
    except ErrorSoftwareFJ as error:
        # Errores que previmos nosotros
        print("   Error controlado:", error)
        if error.__cause__:
            print("   Causa original:", error.__cause__)
        log.error("Operacion " + str(numero) + " fallo: " + str(error))
    except Exception as error:
        # Cualquier otro error inesperado
        print("   Error inesperado:", error)
        log.error("Error inesperado en operacion " + str(numero) + ": " + str(error))
    else:
        print("   Resultado:", resultado)
        return resultado
    finally:
        log.info("Fin de la operacion " + str(numero))


def main():
    log.info("Inicio de la simulacion")

    # Clientes
    ana = ejecutar(1, "Registrar cliente valido (Ana)",
                   lambda: Cliente("Ana Perez", "1100200300", "ana@correo.com", "3001234567"))
    ejecutar(2, "Registrar cliente con correo invalido",
             lambda: Cliente("Luis Gomez", "1100200301", "luiscorreo", "3009876543"))
    ejecutar(3, "Registrar cliente sin nombre",
             lambda: Cliente("", "1100200302", "x@correo.com", "3001112233"))
    carlos = ejecutar(4, "Registrar cliente valido (Carlos)",
                      lambda: Cliente("Carlos Ruiz", "900800700", "carlos@correo.com", "3105556677"))

    # Servicios
    sala = ejecutar(5, "Crear sala valida",
                    lambda: ReservaSala("Jupiter", 50000, 25))
    ejecutar(6, "Crear equipo con tarifa negativa",
             lambda: AlquilerEquipo("Portatil", -100, "computador"))
    equipo = ejecutar(7, "Crear alquiler de proyector",
                      lambda: AlquilerEquipo("Proyector", 15000, "proyector"))
    asesoria = ejecutar(8, "Crear asesoria senior",
                        lambda: Asesoria("Asesoria en Python", 80000, "senior"))

    # Reservas
    reserva1 = ejecutar(9, "Reservar sala por 3 horas", lambda: Reserva(ana, sala, 3))
    ejecutar(10, "Reservar sala por 12 horas (no se permite)", lambda: Reserva(ana, sala, 12))
    ejecutar(11, "Reservar sin cliente", lambda: Reserva(None, equipo, 2))

    # Procesar y cancelar
    ejecutar(12, "Procesar la reserva con 10% de descuento", lambda: reserva1.procesar(descuento=0.10))
    ejecutar(13, "Confirmar otra vez la misma reserva", lambda: reserva1.confirmar())
    reserva2 = ejecutar(14, "Reservar asesoria para Carlos (2 horas)", lambda: Reserva(carlos, asesoria, 2))
    asesoria.disponible = False  # apagamos el servicio
    ejecutar(15, "Procesar reserva de un servicio no disponible", lambda: reserva2.procesar())

    # Prueba de la "sobrecarga" del calculo de costos
    print("\nCostos del proyector por 5 horas:")
    print("  Con IVA:", equipo.calcular_costo(5))
    print("  Sin impuesto:", equipo.calcular_costo(5, impuesto=0))
    print("  Con IVA y 15% de descuento:", equipo.calcular_costo(5, descuento=0.15))

    print("\nFin. Los detalles quedaron en software_fj.log")
    log.info("Fin de la simulacion")


main()
