import csv


def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function

    
    products_file = open("labs/lab08/exercise3/data/products.csv", "r", newline="")
    reader1 = csv.reader(products_file)
    products = {}
    for row in reader1:
        product_id, product_name, price = row
    products_file.close()

    order_file = open("labs/lab08/exercise3/data/order.csv", "r", newline="")
    reader2 = csv.reader(order_file)

    total_cost = []
    for item in reader2:
        product_id, quantity = item
        if product_id in products:
            cost = price * quantity
            total_cost.append(cost)
    order_file.close()

    output_file = open("labs/lab08/exercise3/data/total.csv", "w", newline="")
    writer = csv.writer(output_file)
    writer.writerow([f"total_cost:.2f"])
    output_file.close()
    return total_cost
# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${str(result:.2f)}")
