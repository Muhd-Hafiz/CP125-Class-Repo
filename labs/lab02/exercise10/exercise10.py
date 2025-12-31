
def calculate_base_usage(distance):
    base_usage  = (distance / 10) * 1.5
    return base_usage


def apply_mode_bonus(usage, is_sport_mode):
    if is_sport_mode:
        usage = 1.5 * 50 / 100 + usage
    return usage

def has_enough_battery(distance, current_battery, is_sport_mode):
    """
    Calculates if there is enough battery for a round trip (distance * 2).
    """
    base_usage = calculate_base_usage(distance * 2)
    total_usage = apply_mode_bonus(base_usage, is_sport_mode)
    
    if total_usage <= current_battery:
        return True
    
    return False