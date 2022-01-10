#Sort Dictinary

dict = {1: 10, 3: 20, 5: 60, 4: 40, 9: 6, 8: 55, 3: 22}

for i in sorted(dict.keys()):
    print(i, end = " ")
print()

#Sum Of Dictinary


def dictsum(dict):
	sum = 0
	for i in dict.values():
		sum = sum + i
	
	return sum
d = {'x': 65, 'y':20, 'z':69}
print("Sum :", dictsum(d))
