#!/usr/bin/env python3
"""
Calculadora de terminal interactiva con soporte para suma, resta y multiplicación.
Utiliza códigos de escape ANSI para dar formato visual y colores en consola.
"""

# Códigos de escape ANSI para colores y estilos en la terminal
RESET = "\033[0m"
NEGRITA = "\033[1m"
CYAN = "\033[36m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
ROJO = "\033[31m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"


def mostrar_encabezado() -> None:
    """Muestra el banner de bienvenida y el título de la calculadora."""
    print(f"\n{CYAN}{NEGRITA}{'=' * 45}{RESET}")
    print(f"{CYAN}{NEGRITA}        CALCULADORA DE TERMINAL{RESET}")
    print(f"{CYAN}{NEGRITA}{'=' * 45}{RESET}")


def mostrar_menu() -> None:
    """Muestra las opciones disponibles en el menú principal."""
    print(f"\n{MAGENTA}{NEGRITA}--- MENÚ DE OPERACIONES ---{RESET}")
    print(f"  {VERDE}{NEGRITA}[1]{RESET} Sumar dos números")
    print(f"  {VERDE}{NEGRITA}[2]{RESET} Restar dos números")
    print(f"  {VERDE}{NEGRITA}[3]{RESET} Multiplicar dos números")
    print(f"  {ROJO}{NEGRITA}[4]{RESET} Salir")
    print(f"{MAGENTA}{'-' * 27}{RESET}")


def solicitar_numero(etiqueta: str) -> float:
    """
    Solicita un valor numérico por consola y valida que sea válido.

    :param etiqueta: Texto descriptivo que indica cuál número se solicita.
    :return: Número decimal (float) válido ingresado por el usuario.
    """
    while True:
        entrada = input(f"{AZUL}{NEGRITA}{etiqueta}: {RESET}").strip()
        try:
            return float(entrada)
        except ValueError:
            print(
                f"{ROJO}❌ Error: Entrada inválida. Por favor, introduce un número.{RESET}"
            )


def sumar(a: float, b: float) -> float:
    """Realiza la suma de dos números."""
    return a + b


def restar(a: float, b: float) -> float:
    """Realiza la resta de dos números (a - b)."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Realiza la multiplicación de dos números (a * b)."""
    return a * b


def formatear_numero(n: float) -> str:
    """Formatea el número para mostrarlo como entero si no tiene decimales."""
    if n.is_integer():
        return str(int(n))
    return f"{n:.4f}".rstrip("0").rstrip(".")


def main() -> None:
    """Bucle principal de la calculadora interactiva."""
    mostrar_encabezado()

    while True:
        mostrar_menu()
        opcion = input(
            f"{AMARILLO}{NEGRITA}Selecciona una opción (1-4): {RESET}"
        ).strip()

        if opcion == "1":
            # Operación de Suma
            print(f"\n{CYAN}{NEGRITA}>> OPERACIÓN: SUMA{RESET}")
            num1 = solicitar_numero("Introduce el primer número")
            num2 = solicitar_numero("Introduce el segundo número")
            resultado = sumar(num1, num2)

            str_num1 = formatear_numero(num1)
            str_num2 = formatear_numero(num2)
            str_res = formatear_numero(resultado)

            print(
                f"\n{VERDE}{NEGRITA}✔ Resultado:{RESET} "
                f"{str_num1} + {str_num2} = {VERDE}{NEGRITA}{str_res}{RESET}"
            )

        elif opcion == "2":
            # Operación de Resta
            print(f"\n{CYAN}{NEGRITA}>> OPERACIÓN: RESTA{RESET}")
            num1 = solicitar_numero("Introduce el primer número")
            num2 = solicitar_numero("Introduce el segundo número")
            resultado = restar(num1, num2)

            str_num1 = formatear_numero(num1)
            str_num2 = formatear_numero(num2)
            str_res = formatear_numero(resultado)

            print(
                f"\n{VERDE}{NEGRITA}✔ Resultado:{RESET} "
                f"{str_num1} - {str_num2} = {VERDE}{NEGRITA}{str_res}{RESET}"
            )

        elif opcion == "3":
            # Operación de Multiplicación
            print(f"\n{CYAN}{NEGRITA}>> OPERACIÓN: MULTIPLICACIÓN{RESET}")
            num1 = solicitar_numero("Introduce el primer número")
            num2 = solicitar_numero("Introduce el segundo número")
            resultado = multiplicar(num1, num2)

            str_num1 = formatear_numero(num1)
            str_num2 = formatear_numero(num2)
            str_res = formatear_numero(resultado)

            print(
                f"\n{VERDE}{NEGRITA}✔ Resultado:{RESET} "
                f"{str_num1} × {str_num2} = {VERDE}{NEGRITA}{str_res}{RESET}"
            )

        elif opcion == "4":
            # Salir de la aplicación
            print(
                f"\n{CYAN}{NEGRITA}¡Gracias por usar la calculadora! Hasta pronto.{RESET}\n"
            )
            break

        else:
            # Opción no válida
            print(
                f"{ROJO}❌ Opción no reconocida. Por favor, elige 1, 2, 3 o 4.{RESET}"
            )


if __name__ == "__main__":
    main()
