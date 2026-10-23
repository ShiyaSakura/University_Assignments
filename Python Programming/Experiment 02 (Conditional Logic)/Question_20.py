# Write a Python Program To Take Any Date As Input & Display Next Date Of The Calendar.

def check_leap_year(year: int) -> bool:
    """Checks Whether a Given Year Is a Leap Year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main() -> None:   
    try:
        day = int(input("Please Enter a Day : "))
        month = int(input("Please Enter a Month : "))
        year = int(input("Please Enter a Year : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Day, Month & Year.")
        return

    if year <= 0:
        print("Invalid Input, Please Enter a Positive Calendar Year.")
        return

    if month < 1 or month > 12:
        print("Invalid Month, Please Enter A Valid Month Between 1 & 12.")
    else:
        is_leap = check_leap_year(year)
        month_days = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if day < 1 or day > month_days[month - 1]:
            print(f"Invalid Day, Please Enter A Day Between 1 & {month_days[month - 1]}.")
        else:
            print(f"You Entered The Date As : {day}/{month}/{year}")
            if day < month_days[month - 1]:
                day += 1
            else:
                day = 1
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
            print(f"The Next Date Is : {day}/{month}/{year}")

if __name__ == "__main__":
    main()