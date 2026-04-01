import pandas as pd


def compare_averages(filename):
     data = pd.read_csv(filename)

     mean_math = data['Math'].mean()
     mean_science = data['Science'].mean()
     mean_english = data['English'].mean()

     best_subject = max(mean_math, mean_science, mean_english)
     worst_subject = min(mean_math, mean_science, mean_english)
        
     return {
          mean_math: 'Math',
          mean_science: 'Science',
          mean_english: 'English',
          best_subject: 'Best Subject',
          worst_subject: 'Worst Subject'
    }


# }