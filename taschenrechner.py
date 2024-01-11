def calculate(numbers, operators):
    result = float(numbers[0])
    for i in range(1, len(numbers)):
        if operators[i - 1] == "+":
            result += float(numbers[i])
        elif operators[i - 1] == "-":
            result -= float(numbers[i])
        elif operators[i - 1] == "*":
            result *= float(numbers[i])
        elif operators[i - 1] == "/" and float(numbers[i]) != 0:
            result /= float(numbers[i])
        else:
            print("Ungültige Operation oder Division durch Null.")
            return None
    return result
operators = ["+", "-", "*", "/"]
while True:
    user_input = input("Gib deine Rechenaufgabe ein oder 'exit' zum Beenden:\n")
    if user_input.lower() == "exit":
        print("Das Programm wird beendet.")
        break
    elements = user_input.split()

    numbers = [elements[i] for i in range(0, len(elements), 2)]
    operators_input = [elements[i] for i in range(1, len(elements), 2)]
    if len(numbers) <= len(operators_input):
        print("Ungültige Eingabe. Bitte gebe eine gültige Rechenoperation ein.")
        continue
    result = calculate(numbers, operators_input)

    if result is not None:
        print(f"Ergebnis: {result}")
