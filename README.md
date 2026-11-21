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
