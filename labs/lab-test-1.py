def determine_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60 and marks <= 79:
        return "B"
    elif marks >= 50 and marks <= 59:
        return "C"
    elif marks >= 40 and marks <= 49:
        return "D"
    else:
        return "F"
    
student_marks = int(input("Enter the student's marks"))
grade = determine_grade(student_marks)  
print(f"Mark : {student_marks}")
print(f"Grade : {grade}") 


