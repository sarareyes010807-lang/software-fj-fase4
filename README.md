levis/readme-aportes
estos son mis aportes del trabajo en grupo fase 4.py

Implementación de excepciones personalizadas
Mi aporte en esta primera parte consiste en desarrollar las excepciones personalizadas del sistema Software FJ, con el propósito de controlar los posibles errores que se puedan presentar durante la ejecución del programa.

Se creó una clase principal llamada SistemaFJError, de la cual heredan otras excepciones específicas, como ValidacionError, ClienteInvalidoError, ServicioInvalidoError, ReservaError, DuracionInvalidaError, ReservaNoDisponibleError y EstadoReservaError.

Estas excepciones permiten identificar y controlar diferentes situaciones, como el ingreso de datos incorrectos, clientes inválidos, servicios mal configurados, duraciones no permitidas y reservas que no cumplen las condiciones establecidas.

Objetivo: garantizar que el sistema pueda identificar los errores de manera organizada, informar al usuario sobre los problemas y continuar funcionando sin detener completamente la aplicación.
Parte 2. Funciones de validación y configuración del archivo LOG
En esta segunda parte mi aporte consiste en desarrollar funciones encargadas de validar los datos ingresados y configurar el registro de eventos y errores del sistema.

Se implementó la función generar_id(), que permite asignar identificadores únicos a los objetos creados.

También se desarrollaron las funciones validar_texto() y validar_numero(), que comprueban que la información ingresada cumpla con las condiciones establecidas. Estas validaciones evitan datos vacíos, valores incorrectos, números negativos cuando no están permitidos y valores que puedan afectar los cálculos.

Además, se implementó la función configurar_logger(), encargada de crear y configurar el archivo software_fj.log, donde se registran los eventos y errores relevantes de la aplicación, facilitando el seguimiento y la identificación de problemas.

Objetivo: proteger la información del sistema, evitar errores por datos incorrectos y mantener un registro de los acontecimientos importantes durante la ejecución del programa.
