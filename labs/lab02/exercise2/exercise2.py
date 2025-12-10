import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    cost_tents = math.ceil(participants / tent_capacity) * tent_price
    total_budget = cost_tents + (meal_price * participants)
    return total_budget
# Test your code here
print("Testing Camping Logistics...")
