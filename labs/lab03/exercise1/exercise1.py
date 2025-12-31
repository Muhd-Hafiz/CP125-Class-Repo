pixels = [100, 120, 200, 150, 180, 160, 140]

def count_bright_spots(pixels):
    bright_spots = 0
    for i in range(1, len(pixels) - 1):
        if pixels[i] > pixels[i - 1] and pixels[i] > pixels[i + 1]:
            bright_spots += 1

    return bright_spots
print(count_bright_spots(pixels))  
