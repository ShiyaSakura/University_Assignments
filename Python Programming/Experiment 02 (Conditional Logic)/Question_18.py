# Write a Python Program To Check Whether The Quadratic Equation Has Real Roots Or Imaginary Roots.

from math import sqrt

def solve_quadratic(a: float, b: float, c: float) -> tuple[str, tuple[float, float] | float]:
    """Computes The Roots Of a Quadratic Equation Ax² + Bx + C = 0 & Returns The Type Of Roots Along With Their Values."""
    discriminant: float = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        return "distinct", (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        return "equal", root
    else:
        real_part = -b / (2 * a)
        imaginary_part = sqrt(abs(discriminant)) / abs(2 * a)
        return "complex", (real_part, imaginary_part)

def main() -> None:
    try:
        a = float(input("Please Enter The Coefficient Of X² : "))
        b = float(input("Please Enter The Coefficient Of X : "))
        c = float(input("Please Enter The Constant c : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Coefficients And Constant.")
        return

    if a == 0:
        print("The Coefficient Of X² Cannot Be Zero, Please Enter A Valid Quadratic Equation.")
        return

    nature, roots = solve_quadratic(a, b, c)

    if nature == "distinct":
        print("The Quadratic Equation Has Two Real & Distinct Roots.")
        print(f"The Roots Are : {roots[0]:.2f} & {roots[1]:.2f}")
    elif nature == "equal":
        print("The Quadratic Equation Has Two Real & Equal Roots.")
        print(f"The Root Is : {roots:.2f}")
    else:
        print("The Quadratic Equation Has Imaginary Roots.")
        print(f"The Roots Are : {roots[0]:.2f} + {roots[1]:.2f}i & {roots[0]:.2f} - {roots[1]:.2f}i")

if __name__ == "__main__":
    main()