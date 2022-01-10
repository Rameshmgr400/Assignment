#interchange first and last elements in a list

def interchgange(myList):
	
	myList[0], myList[-1] = myList[-1], myList[0]

	return myList

myList = [0, 200, 75, 5, 22]
print(interchgange(myList))


#Swap Elements

def swapPositions(list, p1, p2):
	
	list[p1], list[p2] = list[p2], list[p1]
	return list
List = [10, 80, 100, 2, 6, 9]
p1, p2 = 0, 2

print(swapPositions(List, p1, p2))



# Sum Of List

list = [1, 50, 28, 18, 2]
total = sum(list)
print("Sum of elements in list: ", total)

#Grateset Number

list = [50, 24, 2, 56, 20, 70]

list.sort()
result2 = max(list)

print("Largest element is:", list[-1])
print("Largest element is:", result2)


#Count Occurrences

def countX(list, x):
    result = list.count(x)
    return result

list = [4, 6, 7, 12, 8, 5, 0, 5, 5]
a = 5
result = countX(list, a)
print(result)


