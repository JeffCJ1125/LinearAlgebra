import math as math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            # self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be nonempty")

        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        result = []
        for i in range(len(self.coordinates)):
            result.append(self.coordinates[i] + v.coordinates[i])
        return Vector(result)

    def minus(self, v):
        result = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(result)

    def times_scalar(self, constant):
        result = [Decimal(constant) * x for x in self.coordinates]
        return Vector(result)

    def magnitude(self):
        square_list = [x**2 for x in self.coordinates]
        # for i in range(len(self.coordinates)):
        #     sum += self.coordinates[i] * self.coordinates[i]
        result = Decimal(math.sqrt(sum(square_list)))
        return result

    def normalize(self):
        try:
            dis = self.magnitude()
            return self.times_scalar(Decimal(1.0) / dis)
        except ZeroDivisionError:
            raise Exception("can not be zero vector")

    def dot_product(self, v):
        multipy_list = [Decimal(x * y) for x, y in zip(self.coordinates, v.coordinates)]
        return Decimal(sum(multipy_list))

    def get_angle(self, v, isDegree=False):
        dot_prod = round(self.normalize().dot_product(v.normalize()), 3)
        if isDegree == False:
            return math.acos(dot_prod)
        else:
            return math.acos(dot_prod) * 180 / math.pi

    def is_zero_vector(self, tolerance=1e-10):
        return math.fabs(sum(self.coordinates)) <= tolerance

    def is_orthogonal(self, v, tolerance=1e-10):
        return math.fabs(self.dot_product(v)) <= tolerance

    def is_parallel(self, v, tolerance=1e-10):
        if self.is_zero_vector():
            return True
        if v.is_zero_vector():
            return True
        # print(math.fabs(self.get_angle(v)),(math.fabs(self.get_angle(v)) - math.pi))
        if (
            math.fabs(self.get_angle(v)) <= tolerance
            or math.fabs(self.get_angle(v)) == math.pi
        ):
            return True
        return False

    def get_projected_vector(self, v):
        return v.normalize().times_scalar(self.dot_product(v.normalize()))

    def get_orthogonal_vector(self, v):
        self_p = self.get_projected_vector(v)
        return self.minus(self_p)

    def cross_product(self, v):
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
        result = [
            theVector.coordinates[1] * theVector2.coordinates[2]
            - theVector.coordinates[2] * theVector2.coordinates[1],
            Decimal(-1.0)
            * (
                theVector.coordinates[0] * theVector2.coordinates[2]
                - theVector.coordinates[2] * theVector2.coordinates[0]
            ),
            theVector.coordinates[0] * theVector2.coordinates[1]
            - theVector.coordinates[1] * theVector2.coordinates[0],
        ]
        return Vector(result)

    def area_parallelogram(self, v):
        cpresult = self.cross_product(v)
        # area = self.magnitude() * v.magnitude() * math.sin(get_angle)
        return cpresult.magnitude()

    def area_triangle(self, v):
        return self.area_parallelogram(v) /2
