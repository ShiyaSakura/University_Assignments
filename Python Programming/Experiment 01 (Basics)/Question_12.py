# Write a Python Program To Find Left & Right Shifted Value Of A Given Number.

def main() -> None:  
    try:
        a = int(input("Please Enter a Number : "))
        x = int(input("Please Enter The Number Of Bits You Want To Shift : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return
    
    if x < 0:
        print("Invalid Input, Please Enter a Positive Number For The Number Of Bits To Shift.")
        return

    left_shift = a << x
    right_shift = a >> x

    print(f"Left Shifted Value Of {a} Is : {left_shift}")
    print(f"Right Shifted Value Of {a} Is : {right_shift}")

if __name__ == "__main__":
    main()