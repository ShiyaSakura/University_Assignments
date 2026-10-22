# Write a Python Program To Check Whether A Given Number Is A Multiple Of 5 Or Not.

def main() -> None:
    try:
        num = int(input("Please Enter a Number : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return
        
    if num % 5 == 0:
        print(f"{num} Is a Multiple Of 5")
    else:
        print(f"{num} Is Not a Multiple Of 5")

if __name__ == "__main__":
    main()