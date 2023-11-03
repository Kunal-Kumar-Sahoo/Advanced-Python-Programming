from functools import reduce

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x ** 2, array))
print(squares)

odds = list(filter(lambda x: x % 2 == 1, array))
print(odds)

product = reduce(lambda x, y: x * y, array)
print(product)