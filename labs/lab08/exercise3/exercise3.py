import csv

def calculate_order_total(products_file, order_file, output_file):
    prices = {}
    products_file = open("labs/lab08/exercise3/data/products.csv", 'r',newline='')
    reader = csv.DictReader(products_file)

    for row in reader:
        prices[row['product_id']] = float(row['price'])

    products_file.close()

    grand_total = 0

    order_file = open("labs/lab08/exercise3/data/order.csv", 'r',newline='')
    reader = csv.DictReader(order_file)

    output_file = open("labs/lab08/exercise3/data/total.csv", 'w', newline='')
    writer = csv.writer(output_file)

    writer.writerow(['product_id', 'total_cost'])

    for row in reader:
        product_id = row['product_id']
        quantity = int(row['quantity'])

        price = prices[product_id]
        total_cost = price * quantity

        writer.writerow([product_id, "{:.2f}".format(total_cost)])

        grand_total += total_cost

    order_file.close()
    output_file.close()

    return grand_total
# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
