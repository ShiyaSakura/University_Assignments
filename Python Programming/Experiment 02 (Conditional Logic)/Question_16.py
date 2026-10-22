# Write a Python Program To Find The Greatest Among The Two Numbers.

def main() -> None:
    try:
        a = int(input("Please Enter The First Number : "))
        b = int(input("Please Enter The Second Number : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return
    
    if a == b:
        print("Both Numbers Are Equal.")
    else:
        print(f"The Greatest Number Among {a} & {b} Is : {max(a, b)}")

if __name__ == "__main__":
    main()