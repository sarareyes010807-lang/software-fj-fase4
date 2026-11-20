levis/readme-aportes


estos son mis aportes del trabajo en grupo fase 4.py
f# Software FJ - Sistema Integral de Gestion de Clientes, Servicios y Reservas

Proyecto del curso Programacion (213023) - UNAD. Ejercicio 1 de la Fase 4. Sistema orientado a objetos, sin bases de datos, con manejo avanzado de excepciones y archivo de log.

Como ejecutarlo
Requisito: Python 3.10 o superior (recomendado 3.12). Todos los archivos .py deben estar en la misma carpeta.

python software_fj.py
Se ejecuta una demostracion automatica de 30 operaciones: 16 exitosas, 13 errores controlados y 1 error inesperado provocado a proposito. El programa no se detiene y registra todo en software_fj.log, que se crea junto al programa. Al final espera un Enter para que la ventana no se cierre sola.



Mi aporte fue:
- Crear las excepciones personalizadas en excepciones.py, para que el programa no se caiga y muestre errores claros, y configurar el archivo de log donde queda guardado todo.
- Crear las validaciones en validaciones.py, para revisar que los textos, los números y los id estén bien escritos antes de guardarlos.
- Crear las clases principales: EntidadSistema, Cliente y Servicio, con sus atributos privados y sus validaciones.
- Crear los tres servicios especializados: Sala, Equipo y Asesoría, cada uno con sus propias reglas.
- Crear la clase Reserva con sus estados, el gestor SistemaFJ que une a los clientes, servicios y reservas, y la demostración inicial de 17 operaciones.

Lo hice de esta forma para que el sistema quedara orden

## Parte de Sarai

### Mi aporte
Hice la clase Reserva (reserva.py), la simulación (main.py) y el README.

### reserva.py
- Une un cliente, un servicio y las horas. La reserva puede estar PENDIENTE, CONFIRMADA o CANCELADA.
- Si los datos no sirven, lanza un error propio y guarda el error original con raise from.
- confirmar() y cancelar() revisan que la operación se pueda hacer.
- procesar() usa try, except, else y finally, y todo queda anotado en el log.

### main.py
- Hace 15 operaciones de prueba, unas correctas y otras con errores a propósito.
- Si una falla, el programa no se detiene y sigue con la siguiente.

### Cómo ejecutarlo
Poner todos los archivos .py en la misma carpeta y ejecutar: python main.py
Los errores quedan en el archivo software_fj.log.

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
