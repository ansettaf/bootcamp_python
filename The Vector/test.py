from vector import Vector

# Initialize vectors
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
v3 = Vector(3)
v4 = Vector((10, 16))

# Test addition
print(v1 + v2)  # Column vector addition
print(v3 + Vector([[0.0], [1.0], [2.0]]))  # Addition using size init

# Test subtraction
print(v2 - v1)

# Test scalar multiplication
print(v1 * 5)
print(5 * v1)

# Test division
print(v1 / 2.0)

# Uncomment to see rtruediv exception
# print(2.0 / v1)

# Test transpose
print(v1.T())
print(Vector([[1.0, 2.0]]).T())

# Test dot product
print(v1.dot(v2))
print(Vector([[1.0, 3.0]]).dot(Vector([[2.0, 4.0]])))

# Test invalid range
try:
    Vector((5, 2))
except ValueError as e:
    print(e)
