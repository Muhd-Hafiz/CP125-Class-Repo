
def analyze_performance(lap_times):
    lap = len(lap_times)
    if lap < 2:
        return False 
    
    midpoint = lap // 2
    first_half = lap_times[:midpoint]
    second_half = lap_times[midpoint:]

    avg_first = sum(first_half) / len(first_half)
    avg_second = sum(second_half) / len(second_half)

    return avg_second > avg_first

# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
