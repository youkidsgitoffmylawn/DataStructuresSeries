import random

# creating array of random ints
numbers = [int(random.random() * 20) for _ in range(100)]

# printing array so we know what were looking at
print(numbers)

# selection sort
def selectionSort(numbers):
    # your code

# test and print out the result
selectionSort(numbers)
print(numbers)