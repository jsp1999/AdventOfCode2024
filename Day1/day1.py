from functools import reduce

left_column = []
right_column = []

with open('data.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())
        left_column.append(left)
        right_column.append(right)

left_column.sort()
right_column.sort()

result = reduce(lambda acc, pair: acc + abs(pair[0] - pair[1]), zip(left_column, right_column), 0)
similarity = reduce(lambda acc, i: acc + i * right_column.count(i), left_column, 0)

print(result)
print(similarity)
