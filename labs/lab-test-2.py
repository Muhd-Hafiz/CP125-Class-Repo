def determine_number():
    number = []

    for i in range(5):
        num = int(input("enter your number {}: ".format(i+1)))
        number.append(num)

    number.sort()

    sum_num = sum(number)
    highest = max(number)

    return (sum_num, highest, number)

result = determine_number()

print ("Sum: {}, Highest: {}, Sorted Numbers: {}".format(result[0], result[1], result[2]))


   

