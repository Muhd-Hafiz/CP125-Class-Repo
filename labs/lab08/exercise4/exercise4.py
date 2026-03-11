import csv

def calculate_final_grades(input_file, output_file):
    """
    Calculate final grades from midterm and final scores.

    Args:
        input_file: path to scores CSV (student_id,midterm,final)
        output_file: path to output CSV file

    Returns:
        float: average of all final grades
    """
    # TODO: Implement this function
    input_file = open("labs/lab08/exercise4/data/scores.csv", 'r', newline='')
    reader = csv.DictReader(input_file)
    rows = []
    total_grade = 0
    
    for row in reader:
        student_id = row['student_id']
        midterm = float(row['midterm'])
        final = float(row['final'])
        final_grade = (midterm * 0.4) + (final * 0.6)
        row['final_grade'] = final_grade
        rows.append(row)
        total_grade += final_grade
    input_file.close()

    output_file = open("labs/lab08/exercise4/data/grades.csv", 'w', newline='')
    fieldnames = ['student_id','final_grade']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow({'student_id': row['student_id'], 'final_grade': row['final_grade']})
    output_file.close()
    
    avg_grade = total_grade / len(rows) if rows else 0
    return avg_grade

# Test your code here
result = calculate_final_grades("data/scores.csv", "data/grades.csv")
print(f"Average final grade: {result:.2f}")
