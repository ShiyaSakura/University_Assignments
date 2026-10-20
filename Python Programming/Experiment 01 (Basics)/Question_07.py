# Write a Python Program To Find Area Of Triangle When Length Of Sides Are Given.

from math import sqrt

def calculate_area_of_triangle(side1: float, side2: float, side3: float) -> float:
    """ Calculate Area Of Triangle Using Heron's Formula """
    s = (side1 + side2 + side3) / 2 
    return sqrt(s * (s - side1) * (s - side2) * (s - side3))

def main() -> None:
    try:
        side1 = float(input("Please Enter Length Of The First Side : "))
        side2 = float(input("Please Enter Length Of The Second Side : "))
        side3 = float(input("Please Enter Length Of The Third Side : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Length Of Sides.")
        return

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Invalid Input, Please Enter Positive Values For Length Of Sides.")
        return

    if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        print("Invalid Input, The Given Lengths Cannot Form A Triangle.")
        return

    area = calculate_area_of_triangle(side1, side2, side3)
    print(f"The Area Of The Triangle Is : {area:.2f}")

if __name__ == "__main__":
    main()