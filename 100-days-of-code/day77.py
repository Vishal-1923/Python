# ***************************************** Operator Overloading *******************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/77-Day-77-Operator-Overloading/.tutorial/Tutorial.md

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return (f"X dimension: {self.i}, Y dimension: {self.j} and Z dimension: {self.k}")

    def __add__(self, vec):
        return Vector(self.i + vec.i, self.j + vec.j, self.k + vec.k)

x1 = Vector(1, 2, 3)
print(x1)
x2 = Vector(4, 5, 6)
print(x2)

print(x1+x2) #TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector' as + is not defined on Vector datatype
print(type(x1+x2))