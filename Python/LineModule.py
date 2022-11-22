from decimal import Decimal, getcontext

from VectorModule import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = "No nonzero elements found"

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ["0"] * self.dimension
            normal_vector = Vector(all_zeros)
        if not type(normal_vector) == type(Vector([1,1,1])):
            normal_vector = Vector(normal_vector)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal("0")
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector
            # print(n,type(n))
            c = self.constant_term
            # print("c = ", c,type(c))
            basepoint_coords = ["0"] * self.dimension
            # print(basepoint_coords)
            initial_index = Line.first_nonzero_index(n.coordinates)
            # print(initial_index)
            initial_coefficient = n.coordinates[initial_index]
            # print( n[initial_index],type( n[initial_index]))
            # print(initial_coefficient,type(initial_coefficient))
            # print(c / initial_coefficient)
            basepoint_coords[initial_index] = c / initial_coefficient
            # print(basepoint_coords[initial_index])
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ""

            if coefficient < 0:
                output += "-"
            if coefficient > 0 and not is_initial_term:
                output += "+"

            if not is_initial_term:
                output += " "

            if abs(coefficient) != 1:
                output += "{}".format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n.coordinates)
            terms = [
                write_coefficient(
                    n.coordinates[i], is_initial_term=(i == initial_index)
                )
                + "x_{}".format(i + 1)
                for i in range(self.dimension)
                if round(n.coordinates[i], num_decimal_places) != 0
            ]
            output = " ".join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = "0"
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += " = {}".format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)

    def is_parallel(self, line):
        return self.normal_vector.is_parallel(line.normal_vector)

    def __eq__(self, line):
        if self.normal_vector.is_zero_vector():
            if not line.normal_vector.is_zero_vector():
                return False
            else:
                diff = self.constant_term - line.constant_term
                return MyDecimal(diff).is_near_zero()
        elif line.normal_vector.is_zero_vector():
            return False

        if self.is_parallel(line) == False:
            return False

        return self.normal_vector.is_orthogonal(self.basepoint.minus(line.basepoint))

    def getIntersection(self, line):
        A = self.normal_vector.coordinates[0]
        B = self.normal_vector.coordinates[1]
        k1 = self.constant_term
        C = line.normal_vector.coordinates[0]
        D = line.normal_vector.coordinates[1]
        k2 = line.constant_term
        denom = A * D - B * C
        if MyDecimal(denom).is_near_zero():
            if self == line:
                return self
            else:
                return None

        return Vector(
            [
                (D * k1 - B * k2) / denom,
                (-1 * C * k1 + A * k2) / denom,
            ]
        )


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
