Aporte - Levis Narvaez

Yo me encargué de crear la base del sistema para que no se caiga y quede todo guardado.

Lo que hice:

1. Creé el archivo excepciones.py
Ahí creé todas las excepciones personalizadas del sistema para que el programa no se cierre cuando haya un error, sino que avise qué pasó.
Creé: SistemaFJError, ValidacionError, DatoInvalidoError, ParametroFaltanteError, OperacionNoPermitidaError, ClienteNoEncontradoError, ServicioNoEncontradoError, ReservaNoEncontradaError, ReservaError, EstadoReservaError y CalculoCostoError.

2. Creé el archivo logger.py
Ahí configuré el sistema de registro (log) donde queda guardada toda la actividad del sistema, con la fecha, la hora, el nivel del mensaje y la función que lo generó. Con las funciones configurar_logger, crear_log, get_nombre_archivo_log y get_timestamp_actual.

3. Creé el archivo fase 4-practica simulada.py
Ahí está el programa principal. Creé las clases EntidadSistema, Cliente, Servicio, Sala, Equipo, Asesoría y la clase Reserva con el gestor SistemaFJ, donde se hacen las reservas, se calculan los costos y se validan los datos usando las excepciones y el logger que creé.
## Parte de Mariela

### Mi aporte

Desarrollé el módulo de servicios (`servicios.py`), encargado de definir la estructura y el funcionamiento de los servicios ofrecidos por el sistema.

**servicios.py**

- Creé la clase abstracta `Servicio`, estableciendo atributos como nombre, descripción y precio base, junto con métodos que deben implementar los servicios especializados.
- Implementé validaciones para los precios, cantidades, capacidades y parámetros específicos, evitando datos incorrectos en el sistema.
- Desarrollé los tres servicios especializados: `ReservaSala`, `AlquilerEquipo` y `Asesoria`, cada uno con sus propias características y reglas.
- Implementé los métodos para calcular costos y describir los servicios, teniendo en cuenta horas de uso o cantidad de equipos según corresponda.
- Incorporé el cálculo detallado de costos con impuestos y descuentos porcentuales, incluyendo validaciones para evitar valores fuera de los rangos permitidos.
- Apliqué principios de programación orientada a objetos, como abstracción, herencia y encapsulamiento, para contribuir a la organización y funcionamiento del sistema.
