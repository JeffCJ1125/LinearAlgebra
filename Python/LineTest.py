from LineModule import Line

line1 = Line([4.046,2.836],1.21)
line2 = Line([10.115,7.09],3.025)

print("Quiz1 problem1 get intersection: ", line1.getIntersection(line2))

line1 = Line([7.204,3.182],8.68)
line2 = Line([8.172,4.114],9.883)

print("Quiz1 problem2 get intersection: ", line1.getIntersection(line2))


line1 = Line([1.182,5.562],6.744)
line2 = Line([1.773,8.343],9.525)

print("Quiz1 problem3 get intersection: ", line1.getIntersection(line2))