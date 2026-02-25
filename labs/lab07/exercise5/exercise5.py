def find_at_risk_departments(departments, threshold):
    # TODO: Your code here
    # Hint: use .values() on the inner dict — no nested for loop
    
    at_risk_departments = []
    for dept, students in departments.items():
        below_threshold = sum(1 for score in students.values() if score < threshold)
        total_students = len(students)
        if below_threshold > total_students / 2:
            at_risk_departments.append(dept)
    return sorted(at_risk_departments)


departments = {
    "CS":      {"Ali": 85, "Sara": 55, "Zaki": 62},
    "Math":    {"Hana": 90, "Reza": 88},
    "English": {"Tom": 45, "Jay": 50, "Lin": 48},
}
print(find_at_risk_departments(departments, 65))