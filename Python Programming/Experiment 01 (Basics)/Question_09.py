# Write a Python Program To Swap Two Numbers Without Taking Additional Variable.

def main() -> None:
    try:
        a = int(input("Please Enter The First Number : "))
        b = int(input("Please Enter The Second Number : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return
    
    a, b = b, a

    print(f"After Swapping First Number Is : {a}")
    print(f"After Swapping Second Number Is : {b}")

if __name__ == "__main__":
    main()