# Write a Python Program To Generate a Student Grade Sheet Based On Marks Obtained.

SUBJECTS = ["English", "Physics", "Chemistry", "Mathematics", "Computer Science"]

def get_grade(cgpa: float) -> str:
    """Returns The Grade Based On CGPA."""
    if cgpa >= 9.0:
        return "O"
    elif cgpa >= 8.0:
        return "A+"
    elif cgpa >= 7.0:
        return "A"
    elif cgpa >= 6.0:
        return "B"
    elif cgpa >= 5.0:
        return "C"
    else:
        return "F"

def display_grade_sheet(name: str, total_marks: float, percentage: float, cgpa: float, grade: str) -> None:
    """Displays The Student Grade Sheet."""
    print(f"Student Name : {name}")
    print(f"Total Marks : {total_marks} / {len(SUBJECTS) * 100}")
    print(f"Percentage : {percentage:.2f} %")
    print(f"CGPA : {cgpa:.2f}")
    print(f"Grade Obtained : {grade}")

def main() -> None:
    try:
        name = input("Please Enter The Student Name : ").strip()
        if not name:
            print("Invalid Input, Student Name Cannot Be Empty.")
            return
        
        marks = []
        for subject in SUBJECTS:
            mark = float(input(f"Please Enter The Marks Obtained In {subject} : "))
            marks.append(mark)
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Marks Obtained In Each Subject.")
        return

    if any(num < 0 or num > 100 for num in marks):
        print("Invalid Input, Please Enter Marks Between 0 & 100 For Each Subject.")
        return

    total_marks = sum(marks)
    percentage = (total_marks / (len(marks) * 100)) * 100
    cgpa = percentage / 10

    grade = get_grade(cgpa)
    display_grade_sheet(name, total_marks, percentage, cgpa, grade)

if __name__ == "__main__":
    main()