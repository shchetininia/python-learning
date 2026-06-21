import math_utils
distances = [1, 2, 3, 4, 5]
print(distances[0], distances[-1])
print(len(distances))
distances.append(6)

for distance in distances:
    print(distance**2)

squares = math_utils.sum_of_squares(distances)
print(squares)
