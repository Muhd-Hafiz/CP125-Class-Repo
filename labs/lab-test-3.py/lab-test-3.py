import csv

def read_bmi(open_file):
    open_file = open("labs\lab-test-3.py\bmi.csv","r",newline="")
    reader = csv.reader(open_file)

    next(reader)

    total_height = 0
    count = 0

    for row in reader:
        print(row)

        height = float(row[1])
        total_height += height
        count += 1

        average = total_height / count
        print("Average Height:",average)
        open_file.close()


def add_new_data(new_file):

    Gender = input("Enter Your Gender:")
    Height = input("Enter Your Height:")
    Weight = input("Enter Your Weight:")
    Bmi_index = input("Enter Your BMI Index:")

    new_file = open("labs\lab-test-3.py\bmi.csv","a",newline="")
    writer = csv.writer(new_file)
    writer.writerow([Gender, Height, Weight, Bmi_index])
    new_file.close()

    print("\nUpdated File Content:")

    f = open("labs\lab-test-3.py\bmi.csv","r",newline="")
    reader = csv.reader(f)

    for row in reader:
        print(row)
    
    f.close()



average = read_bmi(open_file="")
new_data = add_new_data(new_file="")

print(average)
print(new_data)