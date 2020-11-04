import itertools as it
from typing import Iterable


'''def print_iterable(iterable: Iterable, end: str = ' '):  # Function for a comfortably output
    for item in iterable:
        print(item, end=end)


# count
event_numbers = it.count(0, 2)
print(list(next(event_numbers) for _ in range(10)))  # Output -> numbers from 0 with step = 2 and 10 times in output

# repeat
print_iterable(it.repeat(1, 10))  # Output -> 1 write 10 times
for _ in it.repeat(None, 100):  # Works faster than construction with range!
    pass

# cycle
numbers = it.cycle([1, -1])  # PS: We can give a big array
print('')
print(list(next(numbers) for _ in it.repeat(None, 10)))  # Output -> array with alternate 1 and -1

# islice
print(list(it.islice(it.count(1, 4), 5)))  # Output -> array with 5 elements

# permutations
pin = (1, 2, 3, 4)
print(list(it.permutations(pin)))  # Output -> all combinations with this values

# accumulate
arr = range(1, 11)
print(list(it.accumulate(arr, lambda x, y: x*y)))  # Output -> array, where all values was multiply to next value

# filterfalse
arr = range(1, 11)
print(list(it.filterfalse(lambda x: x > 5, arr)))  # Output -> values < 6 in arr

# zip_longest
names = ['Zak', 'Jhon', 'Bob']
ratings = [100, 0]
dct = dict(it.zip_longest(names, ratings, fillvalue=10))  # Output -> dict where Bob has rating 10
print(dct)
'''
