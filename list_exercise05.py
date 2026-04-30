people = list()
person_data = list()
total_adults = total_minors = 0

for c in range(0, 3):
    person_data.append(input("Name: "))
    person_data.append(int(input("Age: ")))
    people.append(person_data[:])
    person_data.clear()

for person in people:
    if person[1] >= 21:
        print(f"{person[0]} is of legal age.")
        total_adults += 1
    else:
        print(f"{person[0]} is under age.")
        total_minors += 1

print("-" * 30)
print(f"We have {total_adults} adults and {total_minors} minors.")