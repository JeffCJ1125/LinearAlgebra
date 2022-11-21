from PlaneModule import Plane

plane1 = Plane([-0.412, 3.806, 0.728], -3.46)
plane2 = Plane([1.03, -9.515, -1.82], 8.65)

print(
    "Quiz1 problem1 parallel: ",
    plane1.is_parallel(plane2),
    " equal: ",
    plane1 == plane2,
)

plane1 = Plane([2.611, 5.528, 0.283], 4.6)
plane2 = Plane([7.715, 8.306, 5.342], 3.76)

print(
    "Quiz1 problem2 parallel: ",
    plane1.is_parallel(plane2),
    " equal: ",
    plane1 == plane2,
)

plane1 = Plane([-7.926, 8.625, -7.212], -7.952)
plane2 = Plane([-2.642, 2.875, -2.404], -2.443)

print(
    "Quiz1 problem3 parallel: ",
    plane1.is_parallel(plane2),
    " equal: ",
    plane1 == plane2,
)
