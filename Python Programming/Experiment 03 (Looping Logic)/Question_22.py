# Write a Python Program To Find Factorial Of a Given Number.

def main() -> None:
    try:
        n = int(input("Please Enter a Number To Find Its Factorial : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 0:
        print("Invalid Input, Factorial Is Not Defined For Negative Numbers.")
        return
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial Of {n} Is : {factorial}")

if __name__ == "__main__":
    main()