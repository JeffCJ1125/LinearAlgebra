from PlaneModule import Plane
from LinesysModule import LinearSystem
from VectorModule import Vector

p0 = Plane(Vector([1, 1, 1]), 1)
p1 = Plane(Vector([0, 1, 0]), 2)
p2 = Plane(Vector([1, 1, -1]), 3)
p3 = Plane(Vector([1, 0, -2]), 2)

s = LinearSystem([p0, p1, p2, p3])
# print("org s:",s)
s.swap_rows(0, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print("test case 1 failed")
# print("test1 s:",s)
s.swap_rows(1, 3)
if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print("test case 2 failed")
# print("test2 s:",s)

s.swap_rows(3, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print("test case 3 failed")
# print("test3 s:",s)

s.multiply_coefficient_and_row(1, 0)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print("test case 4 failed")
# print("test4 s:",s)

s.multiply_coefficient_and_row(-1, 2)
if not (
    s[0] == p1 and s[1] == p0 and s[2] == Plane(Vector([-1, -1, 1]), -3) and s[3] == p3
):
    print("test case 5 failed")
# print("test5 s:",s)

s.multiply_coefficient_and_row(10, 1)
if not (
    s[0] == p1
    and s[1] == Plane(Vector([10, 10, 10]), 10)
    and s[2] == Plane(Vector([-1, -1, 1]), -3)
    and s[3] == p3
):
    print("test case 6 failed")
# print("test6 s:",s)

s.add_multiple_times_row_to_row(0, 0, 1)
if not (
    s[0] == p1
    and s[1] == Plane(Vector([10, 10, 10]), 10)
    and s[2] == Plane(Vector([-1, -1, 1]), -3)
    and s[3] == p3
):
    print("test case 7 failed")
# print("test7 s:",s)

s.add_multiple_times_row_to_row(1, 0, 1)
if not (
    s[0] == p1
    and s[1] == Plane(Vector([10, 11, 10]), 12)
    and s[2] == Plane(Vector([-1, -1, 1]), -3)
    and s[3] == p3
):
    print("test case 8 failed")
# print("test8 s:",s)

s.add_multiple_times_row_to_row(-1, 1, 0)
if not (
    s[0] == Plane(Vector([-10, -10, -10]), -10)
    and s[1] == Plane(Vector([10, 11, 10]), 12)
    and s[2] == Plane(Vector([-1, -1, 1]), -3)
    and s[3] == p3
):
    print("test case 9 failed")
# print("test9:", s)
