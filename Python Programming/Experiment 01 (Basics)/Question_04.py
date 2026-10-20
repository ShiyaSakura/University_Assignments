# Write a Python Program To Perform Basic Arithmetic Operations On Two Numbers.

def main() -> None:
    try:
        a = int(input("Please Enter The First Number : "))
        b = int(input("Please Enter The Second Number : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Integer.")
        return

    print(f"The Addition Of {a} & {b} Is : {a + b}")
    print(f"The Subtraction Of {a} & {b} Is : {a - b}")
    print(f"The Multiplication Of {a} & {b} Is : {a * b}")

    if b != 0:
        print(f"The Quotient & Remainder Of {a} & {b} Are : {a // b} & {a % b}")
    else:
        print("Division By Zero Is Not Allowed.")

if __name__ == "__main__":
    main()