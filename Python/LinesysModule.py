from decimal import Decimal, getcontext
from copy import deepcopy

from VectorModule import Vector
from PlaneModule import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = (
        "All planes in the system should live in the same dimension"
    )
    NO_SOLUTIONS_MSG = "No solutions"
    INF_SOLUTIONS_MSG = "Infinitely many solutions"

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def swap_rows(self, row1, row2):
        tmp_row = self.planes[row1]
        self.planes[row1] = self.planes[row2]
        self.planes[row2] = tmp_row
        return self  # add your code here

    def multiply_coefficient_and_row(self, coefficient, row):
        n = self.planes[row].normal_vector
        new_n = n.times_scalar(coefficient)
        c = self.planes[row].constant_term
        new_c = coefficient * self.planes[row].constant_term
        self.planes[row] = Plane(new_n, new_c)
        return self  # add your code here

    def add_multiple_times_row_to_row(
        self, coefficient, row_to_add, row_to_be_added_to
    ):
        multiple_normal_vector = self.planes[row_to_add].normal_vector.times_scalar(
            coefficient
        )
        multiple_constant = coefficient * self.planes[row_to_add].constant_term
        n = self.planes[row_to_be_added_to].normal_vector
        c = self.planes[row_to_be_added_to].constant_term
        self.planes[row_to_be_added_to] = Plane(
            multiple_normal_vector.plus(n), c + multiple_constant
        )

        return self  # add your code here

    def swap_underneath_row_to_find_nozero_coef_in_col(self, row, col):
        for i in range(row + 1, len(self)):
            if not self.planes[i].normal_vector.coordinates[col].is_zero():
                self.swap_rows(row, i)
                return True
        return False

    def clear_coefficient_in_below(self, row, col):
        for row_to_be_added_to in range(row + 1, len(self)):
            n1 = self.planes[row].normal_vector.coordinates[col]
            n2 = self.planes[row_to_be_added_to].normal_vector.coordinates[col]
            scalar = -n2 / n1
            self.add_multiple_times_row_to_row(scalar, row, row_to_be_added_to)

    def clear_coefficient_on_above(self, row, col):
        for row_to_be_added_to in range(row - 1, -1, -1):
            n1 = self.planes[row].normal_vector.coordinates[col]
            n2 = self.planes[row_to_be_added_to].normal_vector.coordinates[col]
            scalar = -n2 / n1
            self.add_multiple_times_row_to_row(scalar, row, row_to_be_added_to)

    def compute_triangular_form(self):
        system = self
        num_of_equation = len(system)
        num_of_dimension = system.dimension
        j = 0
        for i in range(0, num_of_equation):
            while j < num_of_dimension:
                if system.planes[i].normal_vector.coordinates[j].is_zero():
                    if not system.swap_underneath_row_to_find_nozero_coef_in_col(i, j):
                        j += 1
                else:
                    system.clear_coefficient_in_below(i, j)
                    j += 1
                    break
        return system

    def compute_rref(self):
        tri_self = self.compute_triangular_form()
        pivot_list = tri_self.indices_of_first_nonzero_terms_in_each_row()
        for row in range(len(tri_self) - 1, -1, -1):
            pivot_value = pivot_list[row]
            if pivot_value < 0:
                continue
            n1 = 1
            n2 = tri_self.planes[row].normal_vector.coordinates[pivot_value]
            scalar_to_coefficient_one = n1 / n2
            tri_self.multiply_coefficient_and_row(scalar_to_coefficient_one, row)
            tri_self.clear_coefficient_on_above(row, pivot_value)
        return tri_self

    def get_solution(self):
        try:
            return self.do_gaussian_elimination_and_parametrize_solution()
        except Exception as e:
            if (
                str(e) == self.NO_SOLUTIONS_MSG
                or str(e)
                and str(e) == self.INF_SOLUTIONS_MSG
            ):
                return str(e)
            else:
                raise e

    def get_parametrize_solution_base_point(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        base_point = [0] * self.dimension
        for i, p in enumerate(self.planes):
            pivot_variable = pivot_indices[i]
            if pivot_variable < 0:
                break
            base_point[pivot_variable] = p.constant_term
        return Vector(base_point)

    def get_parametrize_solution_direction_vectors(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        free_variable_indices = set((range(num_variables))) - set(pivot_indices)
        # print("set((range(num_variables)))",set((range(num_variables))))
        # print("pivot_indices",set(pivot_indices))
        # print("free_variable_indices",free_variable_indices)
        direction_vectors = []
        for free_variable in free_variable_indices:
            vector = [0] * num_variables
            vector[free_variable] = 1
            for i, p in enumerate(self.planes):
                pivot_variable = pivot_indices[i]
                if pivot_variable < 0:
                    break
                vector[pivot_variable] = -p.normal_vector.coordinates[free_variable]
            # print(vector)
            direction_vectors.append(Vector(vector))

        return direction_vectors

    def do_gaussian_elimination_and_parametrize_solution(self):
        rref = self.compute_rref()
        # print(rref)
        rref.raise_exception_if_contradictory_equation()
        # rref.raise_exception_if_too_few_pivots()
        # num_variables = rref.dimension
        # solution_coordinates = [
        #     rref.planes[i].constant_term for i in range(num_variables)
        # ]
        # return Vector(solution_coordinates)

        direction_vector = rref.get_parametrize_solution_direction_vectors()
        base_point = rref.get_parametrize_solution_base_point()
        # print(base_point.dimension)
        return Parametrization(base_point, direction_vector)

    def raise_exception_if_contradictory_equation(self):
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == "No nonzero elements found":
                    constant_term = MyDecimal(p.constant_term)
                    if not constant_term.is_near_zero():
                        raise Exception(self.NO_SOLUTIONS_MSG)
                else:
                    raise e

    def raise_exception_if_too_few_pivots(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index >= 0 else 0 for index in pivot_indices])
        num_varaibles = self.dimension
        if num_pivots < num_varaibles:
            raise Exception(self.INF_SOLUTIONS_MSG)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i, p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = "Linear System:\n"
        temp = ["Equation {}: {}".format(i + 1, p) for i, p in enumerate(self.planes)]
        ret += "\n".join(temp)
        return ret


class Parametrization(object):

    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM = (
        "The basepoint and direction vectors should all live in the same " "dimension"
    )

    def __init__(self, basepoint, direction_vectors):

        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                # print(v.dimension,self.dimension)
                assert v.dimension == self.dimension

        except AssertionError:
            raise Exception(self.BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM)

    def __str__(self):

        output = ""
        for coord in range(self.dimension):
            output += "x_{} = {} ".format(
                coord + 1, round(self.basepoint.coordinates[coord], 3)
            )
            for free_var, vector in enumerate(self.direction_vectors):
                output += "+ {} t_{}".format(
                    round(vector.coordinates[coord], 3), free_var + 1
                )
            output += "\n"
        return output


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
