# Exercise: Fuel Consumption Calculation (Beecrowd 1017)
# Logic: Time (h) * Average Speed (km/h) / Efficiency (12 km/l)

travel_time = int(input())
average_speed = int(input())

distance = travel_time * average_speed

liters_needed = distance / 12

print(f"{liters_needed:.3f}")