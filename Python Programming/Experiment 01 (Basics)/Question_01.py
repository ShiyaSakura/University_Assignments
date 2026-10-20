# Write a Python Program To Input The User Age & Check Its Data Type.

MIN_AGE: int = 0
MAX_AGE: int = 120

def main() -> None:
    try:
        age = int(input("Please Enter Your Age : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Whole Number For Age.")
        return

    if not (MIN_AGE <= age <= MAX_AGE):
        print(f"Age Must Be Between {MIN_AGE} & {MAX_AGE}.")
        return

    print(f"Age : {age}")
    print(f"Data Type : {type(age).__name__}")

if __name__ == "__main__":
    main()