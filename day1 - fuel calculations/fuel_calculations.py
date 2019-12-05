"""
Reads an input file containing a list of module weights separated by newlines
Then calculates the total fuel required.
The fuel required per module is floor(weight/3) - 2
"""
import math

with open("module_weights.txt", "r") as fin:
    module_weights = fin.readlines()
    module_weights = [int(x.strip()) for x in module_weights]


def calculate_fuel_for_weight(weight):
    return max(0, int(math.floor(weight / 3) - 2))


def calculate_total_fuel_for_module(module_weight):
    fuel = calculate_fuel_for_weight(module_weight)
    total_fuel = fuel
    # print("Fuel to carry module weight: %s" % fuel)
    while fuel > 0:
        fuel = calculate_fuel_for_weight(fuel)
        # print("Fuel to carry fuel weight: %s" % fuel)
        total_fuel += fuel

    return total_fuel

assert calculate_fuel_for_weight(14) == 2
assert calculate_total_fuel_for_module(14) == 2
assert calculate_fuel_for_weight(1969) == 654
assert calculate_total_fuel_for_module(1969) == 966
assert calculate_fuel_for_weight(100756) == 33583
assert calculate_total_fuel_for_module(100756) == 50346

fuel_per_module = [calculate_fuel_for_weight(x) for x in module_weights]
print("If fuel is weightless: %s" % sum(fuel_per_module))

fuel_per_module = [calculate_total_fuel_for_module(x) for x in module_weights]
print("Fuel isn't weightless: %s" % sum(fuel_per_module))
