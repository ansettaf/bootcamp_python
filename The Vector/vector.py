class Vector:
    def __init__(self, data):
        # Case 1: list of lists
        if isinstance(data, list):
            if all(isinstance(v, list) and all(isinstance(x, float) for x in v) for v in data):
                self.values = data
                if all(len(v) == 1 for v in data):
                    self.shape = (len(data), 1)  # column
                elif len(data) == 1:
                    self.shape = (1, len(data[0]))  # row
                else:
                    raise ValueError("Invalid list of lists for a vector")
            else:
                raise TypeError("Values must be list of lists of floats")

        # Case 2: integer -> size
        elif isinstance(data, int):
            if data <= 0:
                raise ValueError("Size must be a positive integer")
            self.values = [[float(i)] for i in range(data)]
            self.shape = (data, 1)

        # Case 3: tuple (a,b) -> range
        elif isinstance(data, tuple) and len(data) == 2:
            a, b = data
            if a > b:
                raise ValueError(f"Invalid range: start {a} > end {b}")
            self.values = [[float(i)] for i in range(a, b)]
            self.shape = (b - a, 1)

        else:
            raise TypeError("Vector must be initialized with list of lists, int, or tuple")

    # Transpose
    def T(self):
        if self.shape[0] == 1:  # row -> column
            return Vector([[v] for v in self.values[0]])
        else:  # column -> row
            return Vector([[v[0] for v in self.values]])

    # Dot product
    def dot(self, other):
        if self.shape != other.shape:
            raise ValueError("Vectors must have the same shape for dot product")
        if self.shape[0] == 1:  # row vector
            return sum(a * b for a, b in zip(self.values[0], other.values[0]))
        else:  # column vector
            return sum(a[0] * b[0] for a, b in zip(self.values, other.values))

    # String representation
    def __repr__(self):
        return f"Vector({self.values})"
    __str__ = __repr__

    # Addition
    def __add__(self, other):
        if not isinstance(other, Vector) or self.shape != other.shape:
            raise ValueError("Addition requires vectors of the same shape")
        if self.shape[0] == 1:
            return Vector([[a + b for a, b in zip(self.values[0], other.values[0])]])
        else:
            return Vector([[a[0] + b[0]] for a, b in zip(self.values, other.values)])
    __radd__ = __add__

    # Subtraction
    def __sub__(self, other):
        if not isinstance(other, Vector) or self.shape != other.shape:
            raise ValueError("Subtraction requires vectors of the same shape")
        if self.shape[0] == 1:
            return Vector([[a - b for a, b in zip(self.values[0], other.values[0])]])
        else:
            return Vector([[a[0] - b[0]] for a, b in zip(self.values, other.values)])

    def __rsub__(self, other):
        if not isinstance(other, Vector) or self.shape != other.shape:
            raise ValueError("Subtraction requires vectors of the same shape")
        return other - self

    # Multiplication by scalar
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply a Vector by a scalar")
        if self.shape[0] == 1:
            return Vector([[a * scalar for a in self.values[0]]])
        else:
            return Vector([[a[0] * scalar] for a in self.values])
    __rmul__ = __mul__

    # Division by scalar
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only divide a Vector by a scalar")
        if scalar == 0:
            raise ZeroDivisionError("division by zero")
        if self.shape[0] == 1:
            return Vector([[a / scalar for a in self.values[0]]])
        else:
            return Vector([[a[0] / scalar] for a in self.values])

    # Scalar / Vector not allowed
    def __rtruediv__(self, scalar):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here")
