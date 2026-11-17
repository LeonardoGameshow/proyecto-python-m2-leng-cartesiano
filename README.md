# Proyecto M2: Fundamentos de Python

## Autor
- **Nombre:** Leonardo Leonel Barrón Espinosa
- **Bootcamp:** U Camp — Fundamentos de Python

---

## ¿Qué es este proyecto y qué hace?
Este proyecto es una aplicación de consola desarrollada en Python que consolida los conocimientos fundamentales del lenguaje. Unifica dos herramientas de validación y cálculo dentro de un **menú interactivo** centralizado:

1. **Validador de Longitud de Palabras:** Solicita al usuario una palabra y evalúa si cumple con una longitud de entre 4 y 8 caracteres mediante la función `len()`. Si la palabra es muy corta o muy larga, informa el error y vuelve a solicitarla hasta obtener una entrada válida, guardando todos los intentos realizados durante la sesión en un historial.
2. **Calculador de Cuadrantes Cartesianos:** Solicita coordenadas numéricas ($X$ y $Y$), valida que sean números reales y rechaza explícitamente el valor cero (`0`) para determinar en cuál de los cuatro cuadrantes del plano cartesiano se ubica el punto.

---

## ¿Cómo lo apliqué? (Evolución Técnica)
El desarrollo se construyó de forma progresiva integrando distintas estructuras de control y datos:

* **Lógica de bifurcación (`if-elif-else`):** Se utilizó para evaluar los rangos de longitud de las cadenas de texto y las combinaciones de signos positivos/negativos de las coordenadas en el plano.
* **Ciclos `while` y validación de datos:** Se implementaron bucles infinitos controlados (`while True`) para evitar que el programa avance o finalice si el usuario ingresa coordenadas iguales a cero o palabras fuera de rango, garantizando la integridad de los datos.
* **Manejo de excepciones (`try-except`) y Casting:** Se aplicó conversión explícita de texto a número decimal (`float()`) protegida con bloques `try-except ValueError` para evitar que el programa se detenga abruptamente si el usuario escribe letras en lugar de números.
* **Colecciones de datos (Listas y Tuplas):** 
  * Se empleó una **lista (`list`)** mutable para ir almacenando dinámicamente cada palabra intentada por el usuario durante la ejecución.
  * Se utilizó una **tupla (`tuple`)** inmutable para guardar los nombres fijos de los cuatro cuadrantes y acceder a ellos mediante índices.
* **Modularización y PEP8:** Se dividió la lógica en funciones independientes (`evaluar_longitud_palabra`, `determinar_cuadrante` y `main`) conectadas por un menú interactivo limpio y documentado.

---

## Cómo ejecutar el programa
1. Clona este repositorio o descarga el archivo `.py`.
2. Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python Leonardo_Barrón_proyectoM2.py
