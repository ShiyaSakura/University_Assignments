# Write a Python Program To Find Whether a Given Year Is a Leap Year Or Not.

def check_leap_year(year: int) -> bool:
    """Checks Whether a Given Year Is a Leap Year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main() -> None:
    try:
        year = int(input("Please Enter a Year : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number For Year.")
        return

    if year <= 0:
        print("Invalid Input, Please Enter a Positive Calendar Year.")
        return

    if check_leap_year(year):
        print(f"{year} Is a Leap Year.")
    else:
        print(f"{year} Is Not a Leap Year.")

if __name__ == "__main__":
    main()