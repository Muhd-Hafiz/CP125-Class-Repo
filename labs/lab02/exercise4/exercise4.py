def get_hourly_rate(vehicle_type, hour_24):
    # TODO: Implement this function
    # Return hourly rate based on vehicle and time
    if vehicle_type == "Electric":
        charge = 2
    elif vehicle_type == "Hybrid" and hour_24 >= 22 or hour_24 <= 6:
        charge = 2
    elif vehicle_type == "Hybrid":
        charge = 5
    else:
        charge = 5

    return charge

        


# Test your code here
print("Testing Dynamic Parking Rate...")
