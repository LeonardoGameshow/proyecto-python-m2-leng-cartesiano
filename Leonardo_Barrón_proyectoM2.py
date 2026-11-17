# ==============================================================================
# Proyecto M2: Consolidación de Retos (Fundamentos de Python)
# Autor: Leonardo Leonel Barrón Espinosa
# Descripción: Script unificado que incluye el validador de longitud de palabras 
# con historial (listas) y el calculador de cuadrantes en plano cartesiano 
# utilizando tuplas y validación con ciclos while.
# ==============================================================================

def evaluar_longitud_palabra(historial_palabras):
    """Función 1: Evalúa la longitud de una palabra y guarda cada intento en una lista."""
    print("\n--- [Reto 1] Validación de Longitud de Palabra ---")
    while True:
        palabra = input("Ingresa una palabra (debe tener entre 4 y 8 letras, o escribe 'salir' para volver al menú): ").strip()
        
        if palabra.lower() == 'salir':
            print("Regresando al menú principal...\n")
            break
            
        # Agregamos cada intento a la lista (colección mutable)
        historial_palabras.append(palabra)
        longitud = len(palabra)
        
        if 4 <= longitud <= 8:
            print(f"¡Palabra correcta! Tiene {longitud} letras.")
            print(f"Historial de intentos en la sesión: {historial_palabras}\n")
            break
        elif longitud < 4:
            print(f"Hacen falta letras (tiene {longitud}). Inténtalo de nuevo.")
            print(f"Historial actual: {historial_palabras}\n")
        else:
            print(f"Demasiadas letras (tiene {longitud}). Inténtalo de nuevo.")
            print(f"Historial actual: {historial_palabras}\n")


def determinar_cuadrante():
    """Función 2: Determina el cuadrante usando una tupla para los nombres y casting de datos."""
    print("\n--- [Reto 2] Ubicación en Plano Cartesiano ---")
    print("Nota: Las coordenadas X y Y no pueden ser 0.")
    
    # Tupla con los nombres fijos de los cuadrantes (inmutable y ordenada)
    nombres_cuadrantes = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")
    
    while True:
        try:
            # Demostración de casting explícito de string a float
            x = float(input("Ingresa la coordenada X: "))
            y = float(input("Ingresa la coordenada Y: "))

            if x == 0 or y == 0:
                print("Error: Las coordenadas no pueden ser cero (0). Inténtalo de nuevo.\n")
                continue

            # Estructura condicional y asignación mediante índices de la tupla
            if x > 0 and y > 0:
                print(f"El punto ({x}, {y}) se encuentra en el {nombres_cuadrantes[0]}.\n")
            elif x < 0 and y > 0:
                print(f"El punto ({x}, {y}) se encuentra en el {nombres_cuadrantes[1]}.\n")
            elif x < 0 and y < 0:
                print(f"El punto ({x}, {y}) se encuentra en el {nombres_cuadrantes[2]}.\n")
            else:
                print(f"El punto ({x}, {y}) se encuentra en el {nombres_cuadrantes[3]}.\n")
            
            break

        except ValueError:
            # Manejo de excepciones si el usuario ingresa letras en lugar de números
            print("Error: Debes ingresar números válidos para las coordenadas. Inténtalo de nuevo.\n")


def main():
    """Función principal que despliega el menú interactivo del proyecto."""
    # Lista para almacenar el historial de palabras de toda la sesión
    historial_palabras = []
    
    while True:
        print("==========================================")
        print("     PROYECTO M2: MENÚ PRINCIPAL          ")
        print("==========================================")
        print("1. Evaluar longitud de palabra")
        print("2. Determinar cuadrante en plano cartesiano")
        print("3. Ver historial de palabras ingresadas")
        print("4. Salir del programa")
        print("==========================================")
        
        opcion = input("Elige una opción (1-4): ").strip()
        
        if opcion == '1':
            evaluar_longitud_palabra(historial_palabras)
        elif opcion == '2':
            determinar_cuadrante()
        elif opcion == '3':
            print(f"\n--- Historial de palabras de la sesión ---")
            if historial_palabras:
                print(historial_palabras)
            else:
                print("Aún no se han ingresado palabras.")
            print("-" * 42 + "\n")
        elif opcion == '4':
            print("\n¡Gracias por usar el programa! Saliendo...")
            break
        else:
            print("\nOpción no válida. Por favor, elige un número entre 1 y 4.\n")


if __name__ == "__main__":
    main()