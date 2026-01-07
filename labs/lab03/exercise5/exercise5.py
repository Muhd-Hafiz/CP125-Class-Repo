def get_position(cars, car_number):
    for i in range(len(cars)):
        if cars[i] == car_number:
            return i
    return None

def has_overtaken(before, after, car1, car2):
    car1_before = get_position(before, car1)
    car2_before = get_position(before, car2)            
    car1_after = get_position(after, car1)  
    car2_after = get_position(after, car2)        
    if car1_before is None or car2_before is None or car1_after is None or car2_after is None:
        return False
    return car1_before > car2_before and car1_after < car2_after    
