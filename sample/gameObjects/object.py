class Object:
    def __init__(self, x, y, width, height, color, vel):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._vel = vel

    def __getX(self):
        return self._x

    def __setX(self, x):
        self._x = x

    def __getY(self):
        return self._y

    def __setY(self, y):
        self._y = y

    def __getWidth(self):
        return self._width

    def __setWidth(self, width):
        self._width = width

    def __getHeight(self):
        return self._height

    def __setHeight(self, height):
        self._height = height

    def __getVel(self):
        return self._vel

    def __setVel(self, vel):
        self._vel = vel

    def __getColor(self):
        return self._color

    def __setColor(self, color):
        self._color = color


    x = property(__getX, __setX)
    y = property(__getY, __setY)
    width = property(__getWidth, __setWidth)
    height = property(__getHeight, __setHeight)
    color = property(__getColor, __setColor)
    vel = property(__getVel, __setVel)
