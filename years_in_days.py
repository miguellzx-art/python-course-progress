total_days = int(input())
years = total_days // 365
remaining_days = total_days % 365
months = remaining_days // 30
days = remaining_days % 30
print(f"{years} year(s)")
print(f"{months} month(s)")
print(f"{days} day(s)")