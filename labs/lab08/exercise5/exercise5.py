# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv
def summarize_sales(input_file, output_file):
    """
    Calculate sales statistics: total, average, highest, and lowest revenue.

    Args:
        input_file: path to sales CSV (product,quantity,price)
        output_file: path to output text file

    Returns:
        tuple: (total, average, highest, lowest)
    """
    # TODO: Implement this function
    input_file = open("labs/lab08/exercise5/data/sales.csv", 'r', newline='')
    reader = csv.DictReader(input_file)
    total = 0
    count = 0
    revenues = []
    for row in reader:
        quantity = int(row['quantity'])
        price = float(row['price'])
        revenue = quantity * price
        total += revenue
        count += 1
        revenues.append(revenue)
    average = total / count if count > 0 else 0
    highest = max(revenues) if revenues else 0
    lowest = min(revenues) if revenues else 0

    input_file.close()
    
    output_file = open("labs/lab08/exercise5/data/summary.txt", 'w')
    for row in [('Total', total), ('Average', average), ('Highest', highest), ('Lowest', lowest)]:
        output_file.write(f"{row[0]}: ${row[1]:.2f}\n")
    output_file.close()
    
    return total, average, highest, lowest
# Test your code here
result = summarize_sales("data/sales.csv", "data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
