"""Command-line interface for the calculator application."""

from app.calculator import Calculator


HELP_TEXT = """
Available commands:
  add       Add two numbers
  subtract  Subtract the second number from the first
  multiply  Multiply two numbers
  divide    Divide the first number by the second
  history   Show calculation history
  help      Show this help message
  exit      Exit the calculator
"""


def get_number(prompt: str) -> float:
    """Prompt the user until a valid number is entered."""
    while True:
        value = input(prompt)

        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please try again.")


def run_calculator():
    """Run the calculator REPL."""
    calculator = Calculator()

    print("Professional Calculator")
    print("Type 'help' to see available commands.")

    while True:
        command = input("\nEnter command: ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        if command == "help":
            print(HELP_TEXT)
            continue

        if command == "history":
            history = calculator.get_history()

            if not history:
                print("No calculations in history.")
            else:
                for calculation in history:
                    print(calculation)

            continue

        if command not in {"add", "subtract", "multiply", "divide"}:
            print("Invalid command. Type 'help' for options.")
            continue

        first_number = get_number("Enter first number: ")
        second_number = get_number("Enter second number: ")

        try:
            result = calculator.calculate(
                command,
                first_number,
                second_number
            )
            print(f"Result: {result}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":  # pragma: no cover
    run_calculator()