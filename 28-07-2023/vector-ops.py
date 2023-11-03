import math

class Vector:
    def __init__(self,
        x: float = 0,
        y: float = 0,
        z: float = 0
    ) -> None: # Constructor
        self.__x = x
        self.__y = y
        self.__z = z
    
    def __str__(self) -> str: 
        '''Returns string representation of the object'''
        return f'{self.__x}i + {self.__y}j + {self.__z}k'

    def __getitem__(self, item: int) -> float:
        '''Getter'''
        if item == 0:
            return self.__x
        elif item == 1:
            return self.__y
        elif item == 2:
            return self.__z
        else:
            raise IndexError('There are only 3 elements in the vector')

    def __add__(self, other):
        '''Operator overloading (Addition)'''
        return Vector(
            self.__x + other[0],
            self.__y + other[1],
            self.__z + other[2]
        )

    def __sub__(self, other):
        '''Operator overloading (Subtraction)'''
        return Vector(
            self.__x - other[0],
            self.__y - other[1],
            self.__z - other[2]
        )

    def __mul__(self, other):
        '''Operator overloading (Multiplication)'''
        if isinstance(other, Vector):
            '''
            Dot product
            '''
            return Vector(
                self.__x * other[0],
                self.__y * other[1],
                self.__z * other[2]
            )

        elif isinstance(other, (int, float)):
            '''
            Scalar product
            '''
            return Vector(
                self.__x * other,
                self.__y * other,
                self.__z * other
            )

        else:
            raise TypeError("Operand must be Vector, int of float")

    def __truediv__(self, other):
        '''Operator overloading (Division)'''
        if isinstance(other, (int, float)):
            try:
                return Vector(
                    self.__x / other,
                    self.__y / other,
                    self.__z / other
                )
            except ZeroDivisionError as e:
                print(e)
            
        else:
            raise TypeError("Operand must be int or float")

    def get_magnitude(self) -> float:
        '''Return 2-Norm magnitude of the vector'''
        return math.sqrt(
            self.__x ** 2 + self.__y ** 2 + self.__z ** 2
        )

    def normalize(self):
        '''Convert the vector into a unit vector'''
        magnitude = self.get_magnitude()
        return Vector(
            self.__x / magnitude,
            self.__y / magnitude,
            self.__z / magnitude
        )
    
    def __gt__(self, other) -> bool:
        '''Operator overloading (Greater than)'''
        if isinstance(other, Vector):
            return self.get_magnitude() > other.get_magnitude()
        raise TypeError("Operand must be a Vector")

    def __lt__(self, other) -> bool:
        '''Operator overloading (Less than)'''
        if isinstance(other, Vector):
            return self.get_magnitude() < other.get_magnitude()
        raise TypeError("Operand must be a Vector")
    
    def __ge__(self, other) -> bool:
        '''Operator overloading (Greater than or equal to)'''
        if isinstance(other, Vector):
            return self.get_magnitude() >= other.get_magnitude()
        raise TypeError("Operand must be a Vector")

    def __le__(self, other) -> bool:
        '''Operator overloading (Less than or equal to)'''
        if isinstance(other, Vector):
            return self.get_magnitude() <= other.get_magnitude()
        raise TypeError("Operand must be a Vector")

    def __eq__(self, other) -> bool:
        '''Operator overloading (Equal to)'''
        if isinstance(other, Vector):
            return (
                self.__x == other[0] and
                self.__y == other[1] and
                self.__z == other[2]
            )
        raise TypeError("Operand must be a Vector") 

    def __ne__(self, other) -> bool:
        '''Operator overloading (Not equal to)'''
        if isinstance(other, Vector):
            return (
                self.__x != other[0] and
                self.__y != other[1] and
                self.__z != other[2]
            )
        raise TypeError("Operand must be a Vector")

if __name__ == '__main__':
    v1 = Vector(2, 2, 2)
    v2 = Vector(1, 0, 0)

    print(v1 + v2)
    print(v1 - v2)
    print(v1 * v2)
    print(v1 * 5)
    print(v1 / 2)
    print(v1.normalize())
    print(v1.get_magnitude())
    print(v1 / v2)
