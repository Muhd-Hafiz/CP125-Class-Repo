import math
def filter_query_times(times):
  if len(times) == 0:
    return []
  
  mean = sum(times ) / len(times)
  variance = sum((i - mean) ** 2 for i in times) / len(times)
  std_dev = math.sqrt(variance)
  upper_limit = mean + std_dev

  filter_query_times = []
  for i in times:
        if i <= upper_limit:
            filter_query_times.append(i)
            
  filter_query_times.sort()
  return filter_query_times


# Test
query_times = [45, 52, 48, 180, 51, 47, 50, 12]
result = filter_query_times(query_times)
print(f"Filtered Times: {result}")  
# Expected: [12, 45, 47, 48, 50, 51, 52]
