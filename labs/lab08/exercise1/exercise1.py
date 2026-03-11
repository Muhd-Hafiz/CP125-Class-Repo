def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id score per line)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    # TODO: Implement this function
    f = open(input_file,"r")
    reader = f.readlines()
    f.close()

    passsing_students = []
    for line in reader:
        student_id, score = line.split()
        if int(score) >= 80:
            passsing_students.append(student_id)
    f.close()

    f = open(output_file, "w")
    f.write("\n".join(passsing_students))
    f.close()

    return len(names)

# Test your code here
result = filter_passing_scores("data/scores.txt", "data/passing.txt")
print(f"Passing students: {result}")
