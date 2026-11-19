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
