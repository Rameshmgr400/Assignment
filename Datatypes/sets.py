#Iterate Over

Set = set("pythpn")

for val in Set:
	print(val)

#Maximum and Minimum

def max_min(sets):
	return (max(sets), min(sets))
	
s = set([7, 26, 2, 1, 30, 3, 40, 65, 75])
print(max_min(s))

#Common

def common_ele(a, b):
	a_set = set(a)
	b_set = set(b)
	if len(a_set.intersection(b_set)) > 0:
		return(True)
	return(False)

a = [9, 10, 11, 12, 13]
b = [1, 2, 3, 4, 5]
print(common_ele(a, b))

#Convert Set to string

set = {1, 5, 6, 9, 1, 26}
print(set)
print(type(set))

s = str(set)
print(str)
print(type(s))


#Set To Tuple And Tuple To Set


s1 = {'1', '2', '3', '4', '5'}
print(s1)
print(type(s1))
tpl = tuple(s1)

print(tpl)
print(type(tpl))

t1 = ('a', 'b', 'c')
print(t1)
print(type(t1))

s1 = set(tpl)
print(s1)
print(type(s1))


