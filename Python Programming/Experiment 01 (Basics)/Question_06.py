# Write a Python Program To Calculate Simple Interest.

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """ Calculate Simple Interest Based On The Formula : SI = (P * R * T) / 100 """
    return (principal * rate * time) / 100

def main() -> None:
    try:
        principal = float(input("Please Enter The Principal Amount : "))
        rate = float(input("Please Enter The Rate Of Interest : "))
        time = float(input("Please Enter The Time (In Years) : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Principal, Rate & Time.")
        return

    if principal <= 0 or rate < 0 or time <= 0:
        print("Invalid Input, Please Enter Positive Values For Principal, Rate & Time.")
        return

    simple_interest = calculate_simple_interest(principal, rate, time)
    print(f"The Simple Interest Is : {simple_interest:.2f} ")

if __name__ == "__main__":
    main()