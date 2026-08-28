#!/usr/bin/env python3
"""
Calculadora de terminal interactiva con soporte para operaciones básicas y avanzadas:
suma, resta, multiplicación, división, potencia y factorial.
Utiliza códigos de escape ANSI para dar formato visual y colores en consola.
"""

import math

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
    print(f"  {VERDE}{NEGRITA}[4]{RESET} Dividir dos números")
    print(f"  {VERDE}{NEGRITA}[5]{RESET} Potencia (base ^ exponente)")
    print(f"  {VERDE}{NEGRITA}[6]{RESET} Factorial (n!)")
    print(f"  {ROJO}{NEGRITA}[7]{RESET} Salir")
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


def solicitar_entero_no_negativo(etiqueta: str) -> int:
    """
    Solicita un número entero no negativo para operaciones como factorial.

    :param etiqueta: Texto descriptivo que indica el valor solicitado.
    :return: Número entero >= 0 ingresado por el usuario.
    """
    while True:
        entrada = input(f"{AZUL}{NEGRITA}{etiqueta}: {RESET}").strip()
        try:
            valor = int(entrada)
            if valor < 0:
                print(
                    f"{ROJO}❌ Error: El número debe ser un entero no negativo (>= 0).{RESET}"
                )
                continue
            return valor
        except ValueError:
            print(
                f"{ROJO}❌ Error: Entrada inválida. Debe ser un número entero.{RESET}"
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


def dividir(a: float, b: float) -> float:
    """
    Realiza la división de dos números (a / b).
    
    :raises ZeroDivisionError: Si el divisor es 0.
    """
    if b == 0:
        raise ZeroDivisionError("No es posible dividir entre cero.")
    return a / b


def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de una base elevada a un exponente (base ^ exponente).
    Soporta exponentes positivos, negativos y decimales.
    
    :raises ZeroDivisionError: Si la base es 0 y el exponente es negativo.
    """
    if base == 0 and exponente < 0:
        raise ZeroDivisionError("Cero no puede elevarse a un exponente negativo.")
    return base ** exponente


def calcular_factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo (n!).
    
    :raises ValueError: Si el número es negativo.
    """
    if n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos.")
    return math.factorial(n)


def formatear_numero(n: float) -> str:
    """Formatea el número para mostrarlo como entero si no tiene decimales."""
    if isinstance(n, int) or (isinstance(n, float) and n.is_integer()):
        return str(int(n))
    return f"{n:.6f}".rstrip("0").rstrip(".")


def main() -> None:
    """Bucle principal de la calculadora interactiva."""
    mostrar_encabezado()

    while True:
        mostrar_menu()
        opcion = input(
            f"{AMARILLO}{NEGRITA}Selecciona una opción (1-7): {RESET}"
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
            # Operación de División
            print(f"\n{CYAN}{NEGRITA}>> OPERACIÓN: DIVISIÓN{RESET}")
            num1 = solicitar_numero("Introduce el dividendo")
            while True:
                num2 = solicitar_numero("Introduce el divisor")
                if num2 == 0:
                    print(f"{ROJO}❌ Error: No se puede dividir entre cero. Intenta con otro divisor.{RESET}")
                else:
                    break

            resultado = dividir(num1, num2)
            str_num1 = formatear_numero(num1)
            str_num2 = formatear_numero(num2)
            str_res = formatear_numero(resultado)

            print(
                f"\n{VERDE}{NEGRITA}✔ Resultado:{RESET} "
                f"{str_num1} ÷ {str_num2} = {VERDE}{NEGRITA}{str_res}{RESET}"
            )

        elif opcion == "5":
            # Operación de Potencia
            print(f"\n{CYAN}{NEGRITA}>> OPERACIÓN: POTENCIA{RESET}")
            base = solicitar_numero("Introduce la base")
            exponente = solicitar_numero("Introduce el exponente")

            try:
                resultado = calcular_potencia(base, exponente)
                str_base = formatear_numero(base)
                str_exp = formatear_numero(exponente)
                str_res = formatear_numero(resultado)

                print(
                    f"\n{VERDE}{NEGRITA}✔ Resultado:{RESET} "
                    f"{str_base} ^ {str_exp} = {VERDE}{NEGRITA}{str_res}{RESET}"
                )
            except ZeroDivisionError as e:
                print(f"{ROJO}❌ Error matemático: {e}{RESET}")

        elif opcion == "6":
            # Operación de Factorial
            print(f"\n{CYAN}{NEGRITA}>> OPERACIÓN: FACTORIAL{RESET}")
            n = solicitar_entero_no_negativo("Introduce un número entero no negativo (n >= 0)")
            resultado = calcular_factorial(n)

            print(
                f"\n{VERDE}{NEGRITA}✔ Resultado:{RESET} "
                f"{n}! = {VERDE}{NEGRITA}{resultado}{RESET}"
            )

        elif opcion == "7":
            # Salir de la aplicación
            print(
                f"\n{CYAN}{NEGRITA}¡Gracias por usar la calculadora! Hasta pronto.{RESET}\n"
            )
            break

        else:
            # Opción no válida
            print(
                f"{ROJO}❌ Opción no reconocida. Por favor, elige una opción del 1 al 7.{RESET}"
            )


if __name__ == "__main__":
    main()
