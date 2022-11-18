import math as math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be nonempty")

        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        result = []
        for i in range(len(self.coordinates)):
            result.append(self.coordinates[i] + v.coordinates[i])
        return Vector(result)

    def minus(self, v):
        result = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(result)

    def scalar(self, constant):
        result = [constant * x for x in self.coordinates]
        return Vector(result)

    def magnitude(self):
        square_list = [x**2 for x in self.coordinates]
        # for i in range(len(self.coordinates)):
        #     sum += self.coordinates[i] * self.coordinates[i]
        result = math.sqrt(sum(square_list))
        return result

    def normalization(self):
        try:
            dis = self.magnitude()
            return self.scalar(1 / dis)
        except ZeroDivisionError:
            raise Exception("can not be zero vector")

    def DotProduct(self, v):
        multipy_list = [x * y for x, y in zip(self.coordinates, v.coordinates)]
        return sum(multipy_list)

    def Angle(self, v, isDegree=False):
        denominator = self.magnitude() * v.magnitude()
        if isDegree == False:
            return math.acos(self.DotProduct(v) / denominator)
        else:
            return math.acos(self.DotProduct(v) / denominator) * 180 / math.pi

    def isZeroVector(self, tolerance=1e-10):
        return math.fabs(sum(self.coordinates)) <= tolerance

    def isOrthogonal(self, v, tolerance=1e-10):
        return math.fabs(self.DotProduct(v)) <= tolerance

    def isParallel(self, v, tolerance=1e-10):
        if self.isZeroVector():
            return True
        if v.isZeroVector():
            return True
        # print(math.fabs(self.Angle(v)),(math.fabs(self.Angle(v)) - math.pi))
        if math.fabs(self.Angle(v)) <= tolerance or math.fabs(self.Angle(v)) == math.pi:
            return True
        return False

    def getParallel(self, v):
        return v.normalization().scalar(self.DotProduct(v.normalization()))

    def getOrthogonal(self, v):
        self_p = self.getParallel(v)
        return self.minus(self_p)

    def crossProducts(self, v):
        if self.dimension == 3:
            theVector = Vector(self.coordinates)
        else:
            newlist = list(self.coordinates)
            newlist.append(0)
            theVector = Vector(newlist)
        if v.dimension == 3:
            theVector2 = Vector(v.coordinates)
        else:
            newlist = list(v.coordinates)
            newlist.append(0)
            theVector2 = Vector(newlist)
        # print(theVector2)
        result = []
        result.append(
            theVector.coordinates[1] * theVector2.coordinates[2]
            - theVector.coordinates[2] * theVector2.coordinates[1]
        )
        result.append(
            -1.0
            * (
                theVector.coordinates[0] * theVector2.coordinates[2]
                - theVector.coordinates[2] * theVector2.coordinates[0]
            )
        )
        result.append(
            theVector.coordinates[0] * theVector2.coordinates[1]
            - theVector.coordinates[1] * theVector2.coordinates[0]
        )
        return Vector(result)

    def ParallelogramArea(self, v):
        cpresult = self.crossProducts(v)
        # area = self.magnitude() * v.magnitude() * math.sin(angle)
        return cpresult.magnitude()

    def TriangleArea(self, v):
        return self.ParallelogramArea(v) * 0.5