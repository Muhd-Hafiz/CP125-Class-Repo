
def find_largest_drop(readings):
    largest_drop = 0.0
    for i in range(1, len(readings)):
        drop = readings[i - 1] - readings[i]
        if drop > largest_drop:
            largest_drop = drop
    return largest_drop

    

# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
