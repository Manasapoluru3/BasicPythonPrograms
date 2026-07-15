numbers = [10, 45, 3, 78, 22]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)