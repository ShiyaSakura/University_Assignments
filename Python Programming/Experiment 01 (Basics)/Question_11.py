# Write a Python Program To Print The Truth Table For The Given Bitwise Operator.

def print_truth_table(operator: str) -> None:
    """Prints The Truth Table For The Given Bitwise Operator."""

    operations = {
        "&": lambda a, b: a & b,
        "|": lambda a, b: a | b,
        "^": lambda a, b: a ^ b,
        "~": lambda a : ~a & 1
    }

    if operator not in operations:
        print("Invalid Input, Please Enter a Valid Bitwise Operator.")
        return

    operation = operations[operator]
    print(f"Truth Table For '{operator}' Operator")

    if operator == "~":
        print("----------")

        print("A | Result")
        for a in [0, 1]:
            result = operation(a)
            print(f"{a} | {result}")

        print("----------")
    else:
        print("------------")

        print("A B | Result")
        for a in [0, 1]:
            for b in [0, 1]:
                result = operation(a, b)
                print(f"{a} {b} | {result}")

        print("------------")

def main() -> None:
    operator = input("Please Enter a Bitwise Operator (&, |, ^, ~) : ").strip()
    print_truth_table(operator)

if __name__ == "__main__":
    main()