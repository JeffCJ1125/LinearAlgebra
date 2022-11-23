from decimal import Decimal, getcontext
from HyperPlaneModule import HyperPlane
from LinesysModule import LinearSystem
from VectorModule import Vector

p1 = HyperPlane(normal_vector=[0.786, 0.786], constant_term=-0.714)
p2 = HyperPlane(normal_vector=Vector([-0.131, -0.131]), constant_term=0.319)
s = LinearSystem([p1, p2])
r = s.get_solution()
print(r)

p1 = HyperPlane(normal_vector=Vector([2.102, 7.489, -0.786]), constant_term=-5.113)
p2 = HyperPlane(normal_vector=Vector([-1.131, 8.318, -1.209]), constant_term=-6.775)
p3 = HyperPlane(normal_vector=Vector([9.015, 5.873, -1.105]), constant_term=-0.831)
s = LinearSystem([p1, p2, p3])
r = s.get_solution()
print(r)

p1 = HyperPlane(
    normal_vector=Vector([0.786, 0.786, 8.123, 1.111, -8.363]), constant_term=-6.955
)
p2 = HyperPlane(
    normal_vector=Vector([0.131, -0.131, 7.05, -2.813, 1.19]), constant_term=-1.991
)
p3 = HyperPlane(
    normal_vector=Vector([9.015, -5.873, -1.105, 2.013, -2.802]), constant_term=-3.982
)
s = LinearSystem([p1, p2, p3])
r = s.get_solution()
print(r)
