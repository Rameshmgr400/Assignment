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

#Count Vovels

str1 = input("Please Enter Your String : ")
vowels = 0
 
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
       or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
      print("Number of Vowels in this String = ")

#Slipt & Join

a = "I am ramesh magar"
b = a.split()
c = a.split('m')
print(b)
print(c)

str1 = "Iamrameshmagar"
a = "-".join(str1)
print(a)
