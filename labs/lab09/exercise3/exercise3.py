import pandas as pd
import matplotlib.pyplot as plt


def show_math_trend(data):
    data = pd.read_csv("labs\lab09\data\students.csv")

    Math_scores = data['Math']

    plt.plot(data.index, Math_scores)   
    plt.ylabel("Math Score")
    plt.xlabel("Student Index")
    plt.title("Math Score Trends")
    plt.show()

    return len(data)

count = show_math_trend("labs\lab09\data\students.csv")
print(count)  # 25