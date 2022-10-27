import random

list_of_numbers = []
for i in range(30):
    list_of_numbers.append(random.randint(1, 100))
print(max(list_of_numbers))

