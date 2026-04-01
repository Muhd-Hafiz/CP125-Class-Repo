import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(data):
    data = pd.read_csv("labs\lab09\data\students.csv")

    science_scores = data['Science']

    plt.hist(science_scores, bins=10)
    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
    plt.title("Science Score Distribution")
    plt.show()

    return len(data)

count = show_science_distribution("labs\lab09\data\students.csv")
# Chart window appears showing Science score distribution
print(count)  # 25