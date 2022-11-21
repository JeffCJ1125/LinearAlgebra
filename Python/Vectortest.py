from VectorModule import Vector

v = Vector(["8.218", "-9.341"])
w = Vector(["-1.129", "2.111"])
print("Quiz1 problem1 addition: ", v.plus(w))

v = Vector([7.119, 8.215])
w = Vector([-8.223, 0.878])
print("Quiz1 problem2 subtraction: ", v.minus(w))

v = Vector([1.671, -1.012, -0.318])
print("Quiz1 problem3 scalar multiplication: ", v.times_scalar(7.41))

print("*****************")

v = Vector([-0.221, 7.437])
print("Quiz2 problem1 magintude: ", round(v.magnitude(), 3))

v = Vector([8.813, -1.331, -6.247])
print("Quiz2 problem2 magintude: ", round(v.magnitude(), 3))

v = Vector([5.581, -2.136])
first_normalization = v.normalize()
print("Quiz2 problem3 normalize: ", v.normalize())

v = Vector([1.996, 3.108, -4.554])
print("Quiz2 problem4 normalize: ", v.normalize())

print("*****************")

v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])
print("Quiz3 problem1 dot_product: ", round(v.dot_product(w), 3))

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
print("Quiz3 problem2 dot_product: ", round(v.dot_product(w), 3))

print("*****************")

v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319])
print("Quiz3 problem3 angle_rads: ", v.get_angle(w))

v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])
print("Quiz3 problem4 angle_degree: ", round(v.get_angle(w, True), 3))

print("*****************")

v = Vector([-7.579, -7.88])
w = Vector([22.737, 23.64])

print(
    "Quiz4 problem1 parallel: ", v.is_parallel(w), ", orthogonal: ", v.is_orthogonal(w)
)

v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])
print(
    "Quiz4 problem2 parallel: ", v.is_parallel(w), ", orthogonal: ", v.is_orthogonal(w)
)

v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])
print(
    "Quiz4 problem3 parallel: ", v.is_parallel(w), ", orthogonal: ", v.is_orthogonal(w)
)

v = Vector([2.118, 4.827])
w = Vector([0, 0])
print(
    "Quiz4 problem4 parallel: ", v.is_parallel(w), ", orthogonal: ", v.is_orthogonal(w)
)

print("*****************")

v = Vector([3.039, 1.879])
w = Vector([0.825, 2.036])
print("Quiz5 problem1 projected_vector:", v.get_projected_vector(w))

v = Vector([-9.88, -3.264, -8.159])
w = Vector([-2.155, -9.353, -9.473])
print("Quiz5 problem2 orthogonal_vector:", v.get_orthogonal_vector(w))


v = Vector([3.009, -6.172, 3.692, -2.51])
w = Vector([6.404, -9.144, 2.759, 8.718])
print("Quiz5 problem3 projected_vector:", v.get_projected_vector(w))
print("Quiz5 problem3 orthogonal_vector:", v.get_orthogonal_vector(w))

print("*****************")

v = Vector([8.462, 7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])
print("Quiz6 problem1 cross_product:", v.cross_product(w))

v = Vector([-8.987, -9.838, 5.031])
w = Vector([-4.268, -1.861, -8.866])
print("Quiz6 problem2 area_parallelogram:", v.area_parallelogram(w))

v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])
print("Quiz6 problem3 area_parallelogram:", v.area_triangle(w))
