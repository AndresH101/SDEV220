# Andres Hernandez
# M02_LAB 
# This app will test student GPAs for eligbity into the Dean's List or Honor roll

while True:
    last_name = input('What is your last name?: ')
    if last_name == "ZZZ":
        break
    first_name = input('What is your first name?: ')
    student_gpa = float(input('What is your GPA?: '))
    if student_gpa > 3.5:
        print(first_name, last_name, "You are eligible for the Dean's List!")
    if student_gpa > 3.25:
        print(first_name, last_name, "You are eligible for Honor Roll!")
    else:
        print("Not eligible for anything...")