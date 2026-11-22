# main.py
# Programa principal: simula 15 operaciones (validas e invalidas).
# Si una operacion falla, el programa NO se detiene: sigue con la siguiente.

# Traemos las clases de los otros archivos del proyecto
from cliente import Cliente
from excepciones import SistemaFJError
from logger import configurar_logger, crear_log
from reserva import Reserva
from servicios import Asesoria, AlquilerEquipo, ErrorServicio, ReservaSala


# Ejecuta una operacion y muestra si salio bien o mal
# - numero: numero de la operacion
# - descripcion: texto que explica que se hace
# - operacion: la accion a ejecutar (se manda dentro de un lambda)
def ejecutar(numero, descripcion, operacion):
    print("\n" + str(numero) + ". " + descripcion)  # titulo en pantalla
    crear_log("Operacion " + str(numero) + ": " + descripcion, "info")
    try:
        resultado = operacion()  # ejecuta la operacion
    except (SistemaFJError, ErrorServicio) as error:
        # Errores que previmos nosotros (excepciones propias)
        print("   Error controlado:", error)
        if error.__cause__:  # si trae una causa original (encadenamiento)
            print("   Causa original:", error.__cause__)
        crear_log("Operacion " + str(numero) + " fallo: " + str(error), "error")
    except Exception as error:
        # Cualquier otro error inesperado
        print("   Error inesperado:", error)
        crear_log("Error inesperado en operacion " + str(numero) + ": " + str(error), "error")
    else:
        # Si es un servicio mostramos su descripcion; si no, el resultado tal cual
        if hasattr(resultado, "describir_servicio"):
            print("   Resultado:", resultado.describir_servicio())
        else:
            print("   Resultado:", resultado)
        return resultado  # devolvemos el objeto para usarlo despues
    finally:
        # Se ejecuta siempre, con o sin error
        crear_log("Fin de la operacion " + str(numero), "info")


# Funcion principal con las 15 operaciones
def main():
    configurar_logger()  # prepara el archivo de log (sistema_fj.log)
    crear_log("Inicio de la simulacion", "info")

    # ----- Clientes (operaciones 1 a 4) -----
    ana = ejecutar(1, "Registrar cliente valido (Ana)",
                   lambda: Cliente("Ana Perez", "1100200300", "ana@correo.com", "3001234567"))
    ejecutar(2, "Registrar cliente con correo invalido",
             lambda: Cliente("Luis Gomez", "1100200301", "luiscorreo", "3009876543"))
    ejecutar(3, "Registrar cliente sin nombre",
             lambda: Cliente("", "1100200302", "x@correo.com", "3001112233"))
    carlos = ejecutar(4, "Registrar cliente valido (Carlos)",
                      lambda: Cliente("Carlos Ruiz", "900800700", "carlos@correo.com", "3105556677"))

    # ----- Servicios (operaciones 5 a 8) -----
    sala = ejecutar(5, "Crear sala valida (25 personas)",
                    lambda: ReservaSala("Sala Jupiter", 50000, 25))
    ejecutar(6, "Crear equipo con precio negativo",
             lambda: AlquilerEquipo("Portatil", -100, 5))
    proyector = ejecutar(7, "Crear alquiler de proyectores (3 disponibles)",
                         lambda: AlquilerEquipo("Proyector", 15000, 3))
    asesoria = ejecutar(8, "Crear asesoria de Python",
                        lambda: Asesoria("Asesoria Python", 80000, "Python"))

    # ----- Reservas (operaciones 9 a 15) -----
    reserva1 = ejecutar(9, "Reservar sala por 3 horas", lambda: Reserva(ana, sala, 3))
    ejecutar(10, "Reservar sala por 0 horas (no se permite)", lambda: Reserva(ana, sala, 0))
    ejecutar(11, "Reservar sin cliente", lambda: Reserva(None, proyector, 2))
    reserva2 = ejecutar(12, "Reservar 5 proyectores para Carlos", lambda: Reserva(carlos, proyector, 5))
    ejecutar(13, "Procesar la reserva de la sala (19% de impuesto y 10% de descuento)",
             lambda: reserva1.procesar(impuesto=19, descuento=10))
    ejecutar(14, "Procesar la reserva de 5 proyectores (solo hay 3)",
             lambda: reserva2.procesar())
    ejecutar(15, "Cancelar la reserva de la sala", lambda: reserva1.cancelar())

    # ----- Pruebas extra (no cuentan en las 15) -----
    ejecutar("extra", "Cancelar otra vez la misma reserva", lambda: reserva1.cancelar())

    # ----- Prueba de la "sobrecarga" del calculo de costos -----
    print("\nCostos de 2 proyectores:")
    print("  Solo el subtotal:", proyector.calcular_costo(2))
    print("  Con 19% de impuesto:", proyector.calcular_costo_detallado(2, impuesto=19))
    print("  Con 19% de impuesto y 15% de descuento:",
          proyector.calcular_costo_detallado(2, impuesto=19, descuento=15))

    print("\nFin. Los detalles quedaron en sistema_fj.log")
    crear_log("Fin de la simulacion", "info")


# Ejecuta el programa
main()
