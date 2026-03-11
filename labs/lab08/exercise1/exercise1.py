def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id and score on alternating lines)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    # TODO: Implement this function
    input_file = open('labs/lab08/exercise1/data/scores.txt','r')
    passing_students = []
    for line in input_file:
        student_id, score_str = line.split()
        score = int(score_str)
        if score >= 80:
            passing_students.append(f"{student_id} {score}")
    input_file.close()

    output_file = open('labs/lab08/exercise1/data/passing.txt','w')
    for student in passing_students:
        output_file.write(f"{student}\n")
    output_file.close()

    return len(passing_students)

# Test your code here
result = filter_passing_scores("data/scores.txt", "data/passing.txt")
print(f"Passing students: {result}")
