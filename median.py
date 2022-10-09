"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(f'your list {numbers}')
length_of_list = len(numbers)
median = 0

numbers.sort()

if length_of_list % 2 == 0:
    number1,number2 = numbers[length_of_list//2],numbers[(length_of_list//2)-1]
    median = (number1+number2) / 2
else:
    median = numbers[length_of_list//2]

print(f'median: {median}')
