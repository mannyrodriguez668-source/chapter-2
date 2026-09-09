# Name: [Manny A. Rodruguez]
# Section: [Baet 2101]
# Task 1: Change Calculator

amount = int(input("Enter amount in pesos: "))

count_100 = amount // 100
remaining = amount % 100

count_20 = remaining // 20
remaining = remaining % 20

count_5 = remaining // 5
remaining = remaining % 5

count_1 = remaining

print(f"100 pesos: {count_100}")
print(f"20 pesos: {count_20}")
print(f"5 pesos: {count_5}")
print(f"1 peso: {count_1}")
