# ---------------------------------------------------------------
# main.py
# Programa principal: simula 15 operaciones (validas e invalidas).
# Si una operacion falla, el programa NO se detiene: sigue con la siguiente.
# ---------------------------------------------------------------

# Traemos las clases de los otros archivos del proyecto
from cliente import Cliente
from excepciones import ErrorSoftwareFJ
from logger import log
from reserva import Reserva
from servicios import Asesoria, AlquilerEquipo, ReservaSala


# Funcion que ejecuta una operacion y muestra si salio bien o mal
# - numero: el numero de la operacion
# - descripcion: texto que explica que se hace
# - operacion: la accion a ejecutar (se manda dentro de un lambda)
def ejecutar(numero, descripcion, operacion):
    print("\n" + str(numero) + ". " + descripcion)  # Muestra el titulo en pantalla
    log.info("Operacion " + str(numero) + ": " + descripcion)  # Lo anota en el log
    try:
        resultado = operacion()  # Ejecuta la operacion que nos mandaron
    except ErrorSoftwareFJ as error:
        # Errores que previmos nosotros (excepciones propias)
        print("   Error controlado:", error)
        if error.__cause__:  # Si el error trae una causa original (encadenamiento)
            print("   Causa original:", error.__cause__)
        log.error("Operacion " + str(numero) + " fallo: " + str(error))
    except Exception as error:
        # Cualquier otro error que no esperabamos
        print("   Error inesperado:", error)
        log.error("Error inesperado en operacion " + str(numero) + ": " + str(error))
    else:
        # Si no hubo error, mostramos el resultado
        print("   Resultado:", resultado)
        return resultado  # Devolvemos el objeto creado para usarlo despues
    finally:
        # Esto se ejecuta siempre, con o sin error
        log.info("Fin de la operacion " + str(numero))


# Funcion principal donde estan las 15 operaciones
def main():
    log.info("Inicio de la simulacion")  # Primera linea del log

    # ----- Clientes (operaciones 1 a 4) -----
    # 1: cliente con todos los datos correctos
    ana = ejecutar(1, "Registrar cliente valido (Ana)",
                   lambda: Cliente("Ana Perez", "1100200300", "ana@correo.com", "3001234567"))
    # 2: correo sin "@" -> debe dar error
    ejecutar(2, "Registrar cliente con correo invalido",
             lambda: Cliente("Luis Gomez", "1100200301", "luiscorreo", "3009876543"))
    # 3: nombre vacio -> debe dar error de dato faltante
    ejecutar(3, "Registrar cliente sin nombre",
             lambda: Cliente("", "1100200302", "x@correo.com", "3001112233"))
    # 4: segundo cliente valido
    carlos = ejecutar(4, "Registrar cliente valido (Carlos)",
                      lambda: Cliente("Carlos Ruiz", "900800700", "carlos@correo.com", "3105556677"))

    # ----- Servicios (operaciones 5 a 8) -----
    # 5: sala valida de 25 personas
    sala = ejecutar(5, "Crear sala valida",
                    lambda: ReservaSala("Jupiter", 50000, 25))
    # 6: tarifa negativa -> debe dar error
    ejecutar(6, "Crear equipo con tarifa negativa",
             lambda: AlquilerEquipo("Portatil", -100, "computador"))
    # 7: alquiler de proyector valido
    equipo = ejecutar(7, "Crear alquiler de proyector",
                      lambda: AlquilerEquipo("Proyector", 15000, "proyector"))
    # 8: asesoria de nivel senior
    asesoria = ejecutar(8, "Crear asesoria senior",
                        lambda: Asesoria("Asesoria en Python", 80000, "senior"))

    # ----- Reservas (operaciones 9 a 11) -----
    # 9: reserva valida de 3 horas
    reserva1 = ejecutar(9, "Reservar sala por 3 horas", lambda: Reserva(ana, sala, 3))
    # 10: 12 horas es mas de lo permitido para una sala -> error encadenado
    ejecutar(10, "Reservar sala por 12 horas (no se permite)", lambda: Reserva(ana, sala, 12))
    # 11: sin cliente (None) -> error
    ejecutar(11, "Reservar sin cliente", lambda: Reserva(None, equipo, 2))

    # ----- Procesar y cancelar (operaciones 12 a 15) -----
    # 12: procesa la reserva 1 con 10% de descuento
    ejecutar(12, "Procesar la reserva con 10% de descuento", lambda: reserva1.procesar(descuento=0.10))
    # 13: confirmar de nuevo una reserva ya confirmada -> error
    ejecutar(13, "Confirmar otra vez la misma reserva", lambda: reserva1.confirmar())
    # 14: reserva de asesoria para Carlos
    reserva2 = ejecutar(14, "Reservar asesoria para Carlos (2 horas)", lambda: Reserva(carlos, asesoria, 2))
    asesoria.disponible = False  # Apagamos el servicio para probar el error
    # 15: procesar una reserva de un servicio no disponible -> error
    ejecutar(15, "Procesar reserva de un servicio no disponible", lambda: reserva2.procesar())

    # ----- Prueba de la "sobrecarga" del calculo de costos -----
    print("\nCostos del proyector por 5 horas:")
    print("  Con IVA:", equipo.calcular_costo(5))                        # Solo horas
    print("  Sin impuesto:", equipo.calcular_costo(5, impuesto=0))       # Con impuesto en 0
    print("  Con IVA y 15% de descuento:", equipo.calcular_costo(5, descuento=0.15))  # Con descuento

    print("\nFin. Los detalles quedaron en software_fj.log")
    log.info("Fin de la simulacion")  # Ultima linea del log


# Ejecuta el programa
main()
