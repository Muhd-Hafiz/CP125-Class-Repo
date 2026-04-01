import pandas as pd


def explore_data(filename):
    data = pd.read_csv(filename)

    total_students = len(data)
    Subject = ['Math', 'Science', 'English']
    math_avg = data['Math'].mean()
    max_math_score = data['Math'].max()
    highest_math_student = data.loc[data['Math'] == max_math_score, 'Name'].values[0]

    return {
        'total_students': total_students,
        'Subject': Subject,
        'math_avg': math_avg,
        'highest_math_student': highest_math_student
    }