Sistema de Control de Pacientes e Historias Clínicas
===================
Rehabilitar IPS
Fecha publicación: 24 Julio 2015
Versión: 0.0.1
Autor: Jeison Giraldo


Este documento pretende ser una lista de requerimientos inicialmente propuestos para el desarrollo de un sistema web de control y gestión de pacientes en distintas áreas de terapia ocupacional.

--


Descripción del problema
-

El instituto prestador de servicio de terapias físicas y ocupacionales Rehabilitar I.P.S posee actualmente los siguientes inconvenientes en el control de citas médicas, historias clínicas, evoluciones de los pacientes, entre otros:

* Los documentos de los pacientes son controlados de forma física por varios empleados, provocando en ocasiones desorden e inconsistencias en la entrega de información e informes detallados de los pacientes.
* Para los profesionales encargados de los pacientes, es de vital importancia llevar un control de evoluciones médicas con detalles. Actualmente se manejan formularios impresos para obtener la información de cada terapia realizada a los pacientes.
* No se posee un análisis exacto de la evolución o mejoría de cada paciente. Por este motivo se hace necesario poder consultar la información del paciente mediante su historia clínica, con los procedimientos médicos realizados, terapia aplicada y avance de la enfermedad.
* La I.P.S tiene un sistema de gestión de pacientes realizado anteriormente por otro desarrollador. Este sistema está instalado de forma local en el equipo de cómputo terminal de la sala de recepción. El sistema no se ha desarrollado con objetivos específicos de acuerdo a las necesidades del personal del centro médico. Solamente una persona a la vez puede acceder y consultar la información.
* Se requiere un sistema web, de tipo cliente-servidor, donde el personal pueda acceder desde cualquier dispositivo, con conexión a internet, mediante un usuario y clave.
* El sistema deberá estar disponible 24/7.
* Aparte del control de pacientes y sus historias clínicas con sus respectivas evoluciones médicas asociadas, el sistema debe permitir gestionar modulos asociados, como un módulo de asignación de citas con un médico, un módulo de control de pagos, un módulo de facturación, etc.

-

Propuesta de Stack Tecnológico
==============================

El stack tecnológico es el conjunto de herramientas o tecnologías que nos van a permitir desarrollar un proyecto desde cero. Para este proyecto en concreto he decidido usar las siguientes tecnologías para desarrollo web:

### Django Web Framework
---
Django es un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como Modelo–vista–controlador. Permite desarrollar aplicaciones web con metodológías para el desarrollo ágil de proyectos tanto grandes, como pequeños o personales. La meta fundamental de Django es facilitar la creación de sitios web complejos. Django pone énfasis en el re-uso, la conectividad y extensibilidad de componentes.

> **Más información:** Para conocer más de Django, puede visitar este [link][1]

### AngularJS

AngularJS es un framework de JavaScript de código abierto, mantenido por Google, que ayuda con la gestión de lo que se conoce como aplicaciones de una sola página. Su objetivo es aumentar las aplicaciones basadas en navegador con capacidad de Modelo Vista Controlador (MVC), en un esfuerzo para hacer que el desarrollo y las pruebas sean más fáciles.

> **Más información:** Para conocer más de AngularJS, puede visitar este [link][2]

### HTML5
-
HTML5 es una colección de estándares para el diseño y desarrollo de páginas web. Esta colección representa la manera en que se presenta la información en el explorador de internet y la manera de interactuar con ella.

> **Más información:** Para conocer más de HTML5, puede visitar este [link][3]

### JQuery
-
jQuery es una biblioteca gratuita de Javascript, cuyo objetivo principal es simplificar las tareas de creación de páginas web responsivas, acordes a lo estipulado en la Web 2.0, la cuál funciona en todos los navegadores modernos.  Finalmente, jQuery agrega una cantidad impresionante de efectos nuevos a Javascript, los cuáles podrán ser utilizados en sitios Web.

> **Más información:** Para conocer más de jQuery, puede visitar este [link][4]

### Bootstrap 3
-
Bootstrap, es un framework originalmente creado por Twitter, que permite crear interfaces web con CSS y JavaScript, cuya particularidad es la de adaptar la interfaz del sitio web al tamaño del dispositivo en que se visualice. Es decir, el sitio web se adapta automáticamente al tamaño de una PC, una Tablet u otro dispositivo.

> **Más información:** Para conocer más de Bootstrap 3, puede visitar este [link][5]


Requerimientos funcionales
==========================
A continuación un listado aproximado de las tareas puntuales y funcionales que debería cumplir el sistema de información:

##Requerimientos de almacenamiento:


Almacenamiento     |
 ---- | ---
Datos por paciente: | Número de documento, nombres, apellidos, dirección, fecha de nacimiento, lugar de nacimiento, sexo, teléfono, tipo de sangre, antecedentes médicos, alergia a medicamentos, eps.
Datos por evoluciones:    | Fecha, hora entrada, hora salida, diagnóstico, detalle terapia realizada, medico tratante, observaciones.
Datos por historias clínicas:     | Fecha creación, evoluciones asociadas, detalle enfermedad, paciente.
Datos por médico tratante: | Nombres, apellidos, especialidad, telefono, direccion, usuario, clave.
Datos por citas médicas: | Fecha programación, fecha de citación, paciente, medico tratante, estado.
Datos por ingresos/egresos: | Fecha, cantidad, valor unidad, concepto, proveedor.

##Requerimientos de procesamiento:

Procesamiento |
 ---- | ----
Cálculo de edad de paciente | (Fecha actual - fecha nacimiento).
Cálculo de ingresos/egresos | Cálculo por rango de fechas, diario, semanal, mensual, anual.
Cálculo de terapias realizadas | Cálculo por rango de fechas, diario, semanal, mensual, anual.
Cálculo de citas asignadas | Cálculo por rango de fechas, diario, semanal, mensual, anual.
Cálculo de terapias realizadas | Cálculo por rango de fechas, diario, semanal, mensual, anual.
Cálculo de pacientes activos | Cálculo de pacientes que reciben terapia de forma programada o regular.
Cálculo de valor de terapias | Cálculo del valor de terapias realizadas a pacientes.

##Requerimientos de consultas/informes:

Consultas/Informes |
---- | ----
Informe de pacientes | Informe total de pacientes activos
Informe de pacientes por detalle | Informe de pacientes según filtros (documento, sexo, edad, fecha nacimiento, eps, tipo enfermedad, medico tratante)
Informe de pacientes por detalle | Informe de pacientes por médico tratante
Informe de evoluciones | Informe de evoluciones aplicadas por médico tratante
Informe de historias clínicas | Informe de historias clinicas a cargo del médico tratante.
Informe de evoluciones | Informe de evoluciones asociadas a la historia clínica de un paciente.
Informe de citas | Informe de paciente por citas asistidas.


[1]: http://www.djangoproject.com/
[2]: https://angularjs.org/
[3]: https://es.wikipedia.org/wiki/HTML5/
[4]: http://www.jquery.com/
[5]: http://www.getbootstrap.com/