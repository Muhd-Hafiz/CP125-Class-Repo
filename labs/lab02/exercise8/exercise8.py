def calculate_bounce_height(current_height):
    bounce_height = current_height * 0.8
    return bounce_height

def is_ball_stopped(height):
    if height < 1:
        return True
    else:
        return False
    

def simulate_bouncing_ball(start_height):
    current_height = start_height
    bounce_count = 0
    total_distance = 0

    while not is_ball_stopped(current_height):
        bounce_count += 1
        total_distance += current_height * 2
        current_height = calculate_bounce_height(current_height)

    return bounce_count, total_distance

print("Testing Bouncing Ball Simulation...")
