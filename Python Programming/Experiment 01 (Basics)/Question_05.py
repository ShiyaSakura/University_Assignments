# Write a Python Program To Compute The Length Of The Hypotenuse Of a Right Triangle Using Pythagoras Theorem.

from math import sqrt

def calculate_hypotenuse(base: float, perpendicular: float) -> float:
    """Return The Hypotenuse Given Two Positive Side Lengths."""
    return sqrt(base**2 + perpendicular**2)

def main() -> None:
    try:
        base = float(input("Please Enter Length Of The Base : "))
        perpendicular = float(input("Please Enter Length Of The Perpendicular : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if base <= 0 or perpendicular <= 0:
        print("Invalid Input, Please Enter Positive Numbers Only.")
        return

    hypotenuse = calculate_hypotenuse(base, perpendicular)
    print(f"The Length Of The Hypotenuse Is : {hypotenuse:.2f}")

if __name__ == "__main__":
    main()