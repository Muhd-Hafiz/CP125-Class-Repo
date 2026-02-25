def compare_prices(store_a, store_b):
    # TODO: Your code here
    result = {
        "only_a": [],
        "a_cheaper": [],
        "b_cheaper": []
    }

    for product, price_a in store_a.items():
        if product not in store_b:
            result["only_a"].append(product)
        else:
            price_b = store_b[product]
            if price_a < price_b:
                result["a_cheaper"].append(product)
            elif price_a > price_b:
                result["b_cheaper"].append(product)

    for key in result:
        result[key].sort()

    return result
    



store_a = {"milk": 3.50, "bread": 2.00, "eggs": 5.00, "butter": 4.50}
store_b = {"milk": 3.00, "bread": 2.50, "eggs": 5.00, "coffee": 8.00}
result = compare_prices(store_a, store_b)
print(result["only_a"])
print(result["a_cheaper"])
print(result["b_cheaper"])
