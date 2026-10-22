# Write a Python Program To Find The Greatest Among Three Numbers Assuming No Two Values Are Same.

def main() -> None:
    try:
        a = int(input("Please Enter The First Number : "))
        b = int(input("Please Enter The Second Number : "))
        c = int(input("Please Enter The Third Number : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return

    if len({a, b, c}) < 3:
        print("Please Enter Three Different Numbers.")
    else:
        print(f"The Greatest Number Among {a}, {b} & {c} Is : {max(a, b, c)}")

if __name__ == "__main__":
    main()