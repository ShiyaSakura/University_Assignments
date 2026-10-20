# Write a Python Program To Check Whether A Given Number Is Divisible By 3 & 5 Both.

def main() -> None:
    try:
        num = int(input("Please Enter a Number : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return
    
    if num % 15 == 0:
        print(f"{num} Is Divisible By Both 3 & 5")
    else:
        print(f"{num} Is Not Divisible By Both 3 & 5")

if __name__ == "__main__":
    main()