class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        if not isinstance(point, Point):
            raise Exception("Point must be of type Point")

        return (point.x - self.x)**2 + (point.y - self.y)**2 < self.radius**2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    c = Circle(10, 10, 15)
    p = Point(5, 8)
    print(c.contains(p))
