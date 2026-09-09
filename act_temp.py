# Name: [Manny A. Rodriguez]
# Section: [Baet 2101]
# Task 4: Temperature Check

celsius = float(input("Enter temperature in °C: "))
fahrenheit = celsius * 9/5 + 32
in_range = 20 <= celsius <= 30

print(f"Fahrenheit: {fahrenheit}")
print(f"Between 20 and 30 °C: {in_range}")


