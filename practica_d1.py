"""
Práctica D1 — Menú de opciones con patrones
Descripción: Programa interactivo para gestionar y calcular estadísticas de notas de alumnos.
"""


def main():
    contador = 0
    acumulador = 0.0
    nota_maxima = None
    nota_minima = None

    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Introducir una nota")
        print("2. Ver el número de notas introducidas")
        print("3. Ver la media")
        print("4. Ver la nota más alta y la más baja")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        match opcion:
            case "1":
                # Bloque para introducir y validar la nota
                try:
                    nota = float(input("Introduce la nota (entre 0 y 10): "))
                    if 0 <= nota <= 10:
                        contador += 1
                        acumulador += nota

                        # Actualizar extremos (máxima y mínima)
                        if nota_maxima is None or nota > nota_maxima:
                            nota_maxima = nota
                        if nota_minima is None or nota < nota_minima:
                            nota_minima = nota

                        print("¡Nota registrada correctamente!")
                    else:
                        print("Error: La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Error: Por favor, introduce un número válido.")

            case "2":
                # Bloque para ver el total de notas
                print(f"Número de notas introducidas: {contador}")

            case "3":
                # Bloque para calcular y mostrar la media
                if contador == 0:
                    print(
                        "Aviso: No se puede calcular la media porque no se ha introducido ninguna nota."
                    )
                else:
                    media = acumulador / contador
                    print(f"La nota media es: {media:.2f}")

            case "4":
                # Bloque para mostrar los extremos
                if contador == 0:
                    print("Aviso: No hay notas registradas todavía.")
                else:
                    print(f"Nota más alta: {nota_maxima}")
                    print(f"Nota más baja: {nota_minima}")

            case "5":
                print("Saliendo del programa. ¡Hasta luego!")
                break

            case _:
                print("Opción no válida. Por favor, elige un número del 1 al 5.")


if __name__ == "__main__":
    main()
