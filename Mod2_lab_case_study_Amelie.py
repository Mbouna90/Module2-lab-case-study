# Amelie Mbouna Djouda 
# Description: This program collects student names and GPAs, then determines
# if the student qualifies for the Dean's List (3.5+) or Honor Roll (3.25+).

while True:
     # Get the student  last name 
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")

    if last_name.upper() == 'ZZZ':
        print("Processing complete.")
        break

     # Get the student  first name 
    first_name = input("Enter student's first name: ")

     # Get the student's GPA
    try:
        gpa = float(input("Enter student's GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.")
        continue

    print(f"\nStudent: {first_name} {last_name}")

     # Test for Dean's List and Honor Roll
    if gpa >= 3.5:
        print("Congratulations! The student has made the Dean's List.")
    elif gpa >= 3.25:
        print("Great job! The student has made the Honor Roll.")
    else:
        print("The student did not qualify for Dean's List or Honor Roll.")

    print("-" * 40)