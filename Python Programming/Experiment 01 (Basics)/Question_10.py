# Write a Python Program To Find Sum Of First N Natural Numbers.

def sum_of_natural_numbers(n: int) -> int:
    """Calculate The Sum Of The First N Natural Numbers Using Gauss's Formula."""
    return n * (n + 1) // 2

def main() -> None:
    try:
        n = int(input("Please Enter a Number (To Get Sum Of First N Natural Numbers) : "))
    except ValueError:
        print("Invalid Input, Please Enter A Valid Number.")
        return
    
    if n < 1:
        print("Invalid Input, Please Enter A Positive Number.")
        return
    
    sum_number = sum_of_natural_numbers(n)
    print(f"The Sum Of First {n} Natural Numbers Is : {sum_number}")

if __name__ == "__main__":
    main()