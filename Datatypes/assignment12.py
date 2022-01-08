   #reverse a string
s = input("Enter a string: ")
words = s.split(' ')
string =[]
for word in words:
	string.insert(0, word)
print("Reversed String:")
print(" ".join(string))

# Length of a string
a = 'Python programming'
b = 'r a m e s h magar'
print(len(a))
print(len(b))

