# Write a Python Program To Convert Given Seconds Into Hours, Minutes & Remaining Seconds.

def main() -> None:
    try :
        seconds = int(input("Please Enter The Number Of Seconds : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number For Seconds.")
        return
    
    if seconds < 0:
        print("Invalid Input, Please Enter a Positive Value For Seconds.")
        return

    hours, remaining_seconds = divmod(seconds, 3600)
    minutes, remaining_seconds = divmod(remaining_seconds, 60)

    print(f"The Conversion Of {seconds} Seconds Is : {hours} Hours {minutes} Minutes {remaining_seconds} Seconds")

if __name__ == "__main__":
    main()