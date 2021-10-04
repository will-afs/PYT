import math

class Vector2D():
    """ 2D Vector, with x and y coordinates as floats
    """
    def __init__(self, x, y):
        self._x = x
        self.__y = y

    def norm(self):
        """ This method returns the norm of the vector

        >>> Vector2D(2,3).norm()
        3.6055512754639891
        """
        return math.sqrt(self._x**2 + self.__y**2)

if __name__ == "__main__":
    vector = Vector2D(2,3)
    print('Defined a Vector2D with _x and __y values as 2 and 3')
    print()
    print('vector norm should be equal to 3.605551275463989')
    print('vector norm : ' + str(vector.norm()))
    print()

    print('Vector2D attributes and methods list:')
    print(dir(vector))
    print()

    print('Setting vector.x to 10 should not update the norm')
    vector.x = 10
    print('vector norm : ' + str(vector.norm()))
    print()

    print('Setting vector._x to 10 should now update the norm')
    vector._x = 10
    print('vector norm should now be equal to 10.44030650891055')
    print('vector norm : ' + str(vector.norm()))
    print()

    print('Setting vector.y to 0 should not update the norm')
    vector.y = 0
    print('vector norm : ' + str(vector.norm()))
    print()

    print('Setting vector._y to 0 should not update the norm')
    vector._y = 0
    print('vector norm : ' + str(vector.norm()))
    print()

    print('Setting vector._Vector2D__y to 0 should now update the norm')
    vector._Vector2D__y = 0
    print('vector norm should now be equal to 10')
    print('vector norm : ' + str(vector.norm()))
    print()