import math

def calculate_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    return fuel

with open("day01input.txt", 'r') as mass_data:
    mass_data_raw = mass_data.read()
mass_data_list = mass_data_raw.split()
for i, mass in enumerate(mass_data_list):
    mass_data_list[i] = int(mass)
print(mass_data_list)

fuel_required_list = []
for mass in mass_data_list:
    fuel_required_list.append(calculate_fuel(mass))

print(sum(fuel_required_list))
#calculate_fuel tests below
# print(calculate_fuel(12))
# print(calculate_fuel(14))
# print(calculate_fuel(1969))
# print(calculate_fuel(100756))