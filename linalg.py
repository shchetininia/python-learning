import numpy as np

a = np.array([2, 5, 1])
b = np.array([3, 0, 4])

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

dot = np.dot(a,b)
dot2 = np.dot(A,B)

product = a @ b
product2 = A @ B

product_other = A * B

print(f"scalar (a,b) = {dot}, scalar (A,B) = \n {dot2}")
print(f"product a @ b = {product}, product A @ B = \n {product2}, \n another product A * B = \n {product_other}")


