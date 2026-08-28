#!/usr/bin/env python3
"""
Interactive terminal calculator supporting basic and advanced operations:
addition, subtraction, multiplication, division, power, and factorial.
Uses ANSI escape codes for formatted console colors and layout.
"""

import math

# ANSI escape codes for terminal colors and formatting
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"


def display_header() -> None:
  """Display the welcoming banner and calculator title."""
  print(f"\n{CYAN}{BOLD}{'=' * 45}{RESET}")
  print(f"{CYAN}{BOLD}        TERMINAL CALCULATOR{RESET}")
  print(f"{CYAN}{BOLD}{'=' * 45}{RESET}")


def display_menu() -> None:
  """Display available operation options in the main menu."""
  print(f"\n{MAGENTA}{BOLD}--- OPERATIONS MENU ---{RESET}")
  print(f"  {GREEN}{BOLD}[1]{RESET} Add two numbers")
  print(f"  {GREEN}{BOLD}[2]{RESET} Subtract two numbers")
  print(f"  {GREEN}{BOLD}[3]{RESET} Multiply two numbers")
  print(f"  {GREEN}{BOLD}[4]{RESET} Divide two numbers")
  print(f"  {GREEN}{BOLD}[5]{RESET} Power (base ^ exponent)")
  print(f"  {GREEN}{BOLD}[6]{RESET} Factorial (n!)")
  print(f"  {RED}{BOLD}[7]{RESET} Exit")
  print(f"{MAGENTA}{'-' * 27}{RESET}")


def prompt_number(label: str) -> float:
  """Prompt user for a valid decimal or integer number.

  :param label: Descriptive label for the expected number.
  :return: Validated float value.
  """
  while True:
    raw_input_val = input(f"{BLUE}{BOLD}{label}: {RESET}").strip()
    try:
      return float(raw_input_val)
    except ValueError:
      print(f"{RED}❌ Error: Invalid input. Please enter a valid number.{RESET}")


def prompt_non_negative_integer(label: str) -> int:
  """Prompt user for a non-negative integer (e.g., for factorial).

  :param label: Descriptive prompt label.
  :return: Validated non-negative integer (n >= 0).
  """
  while True:
    raw_input_val = input(f"{BLUE}{BOLD}{label}: {RESET}").strip()
    try:
      val = int(raw_input_val)
      if val < 0:
        print(f"{RED}❌ Error: Number must be a non-negative integer (>= 0).{RESET}")
        continue
      return val
    except ValueError:
      print(f"{RED}❌ Error: Invalid input. Please enter a whole integer.{RESET}")


def add(a: float, b: float) -> float:
  """Calculate the sum of two numbers."""
  return a + b


def subtract(a: float, b: float) -> float:
  """Calculate the subtraction of two numbers (a - b)."""
  return a - b


def multiply(a: float, b: float) -> float:
  """Calculate the multiplication of two numbers (a * b)."""
  return a * b


def divide(a: float, b: float) -> float:
  """Calculate the division of two numbers (a / b).

  :raises ZeroDivisionError: If the divisor is 0.
  """
  if b == 0:
    raise ZeroDivisionError("Cannot divide by zero.")
  return a / b


def power(base: float, exponent: float) -> float:
  """Calculate base raised to the power of exponent (base ^ exponent).

  :raises ZeroDivisionError: If base is zero with a negative exponent.
  """
  if base == 0 and exponent < 0:
    raise ZeroDivisionError("Zero cannot be raised to a negative power.")
  return base ** exponent


def factorial(n: int) -> int:
  """Calculate the factorial of a non-negative integer (n!).

  :raises ValueError: If the input is negative.
  """
  if n < 0:
    raise ValueError("Factorial is only defined for non-negative integers.")
  return math.factorial(n)


def format_number(n: float) -> str:
  """Format a float to integer representation if there is no decimal component."""
  if isinstance(n, int) or (isinstance(n, float) and n.is_integer()):
    return str(int(n))
  return f"{n:.6f}".rstrip("0").rstrip(".")


def main() -> None:
  """Main execution loop for the interactive terminal calculator."""
  display_header()

  while True:
    display_menu()
    choice = input(f"{YELLOW}{BOLD}Select an option (1-7): {RESET}").strip()

    if choice == "1":
      # Addition Operation
      print(f"\n{CYAN}{BOLD}>> OPERATION: ADDITION{RESET}")
      num1 = prompt_number("Enter the first number")
      num2 = prompt_number("Enter the second number")
      result = add(num1, num2)

      str_num1 = format_number(num1)
      str_num2 = format_number(num2)
      str_res = format_number(result)

      print(f"\n{GREEN}{BOLD}✔ Result:{RESET} {str_num1} + {str_num2} = {GREEN}{BOLD}{str_res}{RESET}")

    elif choice == "2":
      # Subtraction Operation
      print(f"\n{CYAN}{BOLD}>> OPERATION: SUBTRACTION{RESET}")
      num1 = prompt_number("Enter the first number")
      num2 = prompt_number("Enter the second number")
      result = subtract(num1, num2)

      str_num1 = format_number(num1)
      str_num2 = format_number(num2)
      str_res = format_number(result)

      print(f"\n{GREEN}{BOLD}✔ Result:{RESET} {str_num1} - {str_num2} = {GREEN}{BOLD}{str_res}{RESET}")

    elif choice == "3":
      # Multiplication Operation
      print(f"\n{CYAN}{BOLD}>> OPERATION: MULTIPLICATION{RESET}")
      num1 = prompt_number("Enter the first number")
      num2 = prompt_number("Enter the second number")
      result = multiply(num1, num2)

      str_num1 = format_number(num1)
      str_num2 = format_number(num2)
      str_res = format_number(result)

      print(f"\n{GREEN}{BOLD}✔ Result:{RESET} {str_num1} × {str_num2} = {GREEN}{BOLD}{str_res}{RESET}")

    elif choice == "4":
      # Division Operation
      print(f"\n{CYAN}{BOLD}>> OPERATION: DIVISION{RESET}")
      num1 = prompt_number("Enter the dividend")
      while True:
        num2 = prompt_number("Enter the divisor")
        if num2 == 0:
          print(f"{RED}❌ Error: Cannot divide by zero. Please enter another divisor.{RESET}")
        else:
          break

      result = divide(num1, num2)
      str_num1 = format_number(num1)
      str_num2 = format_number(num2)
      str_res = format_number(result)

      print(f"\n{GREEN}{BOLD}✔ Result:{RESET} {str_num1} ÷ {str_num2} = {GREEN}{BOLD}{str_res}{RESET}")

    elif choice == "5":
      # Power Operation
      print(f"\n{CYAN}{BOLD}>> OPERATION: POWER{RESET}")
      base = prompt_number("Enter the base")
      exponent = prompt_number("Enter the exponent")

      try:
        result = power(base, exponent)
        str_base = format_number(base)
        str_exp = format_number(exponent)
        str_res = format_number(result)

        print(f"\n{GREEN}{BOLD}✔ Result:{RESET} {str_base} ^ {str_exp} = {GREEN}{BOLD}{str_res}{RESET}")
      except ZeroDivisionError as e:
        print(f"{RED}❌ Math error: {e}{RESET}")

    elif choice == "6":
      # Factorial Operation
      print(f"\n{CYAN}{BOLD}>> OPERATION: FACTORIAL{RESET}")
      n = prompt_non_negative_integer("Enter a non-negative integer (n >= 0)")
      result = factorial(n)

      print(f"\n{GREEN}{BOLD}✔ Result:{RESET} {n}! = {GREEN}{BOLD}{result}{RESET}")

    elif choice == "7":
      # Exit
      print(f"\n{CYAN}{BOLD}Thank you for using the calculator! Goodbye.{RESET}\n")
      break

    else:
      # Invalid Option
      print(f"{RED}❌ Unrecognized option. Please choose a number from 1 to 7.{RESET}")


if __name__ == "__main__":
  main()
