#Size Of Tuple

import sys

A = ("X", 1, "Y", 2, "Z", 3)

print("Size of A: " + str(sys.getsizeof(A)) + "bytes")


#Sum Of Tuple Elements

Tuple = (5, 9, 11, 1, 23, 70)

res = sum(Tuple)

print("The Sum Of Tuple Elements : " + str(res))

#Distinct Or Not

Tpl= (1, 4, 5,6)

print("The original tuple is : " + str(Tpl))

res = len(set(Tpl)) == len(Tpl)

print("Is tuple distinct or not? : " + str(res))