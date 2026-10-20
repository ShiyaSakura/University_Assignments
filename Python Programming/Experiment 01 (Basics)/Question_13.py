# Write a Python Program To Use Membership Operators To Find Whether A Given Number Is Present In A List Or Not.

def main() -> None:  
    try:
        print("Please Enter The List Elements (Separated By Space) : ", end = "")
        list_number = [int(x) for x in input().split()]

        num = int(input("Please Enter A Number To Check Its Presence In The List : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return

    print("The Given List Is : ", list_number)

    print(f"Is {num} Present In The List? --> {num in list_number}")
    print(f"Is {num} Not Present In The List? --> {num not in list_number}")

if __name__ == "__main__":
    main()