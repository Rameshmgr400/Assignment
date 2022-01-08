#Check Positive, Negative Numbers

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

#Oddeven Number

def oddeven() :
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
x= 3

# Find The Largest Number

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: ")) 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
print("The largest number is",largest)

# Subjects Marks

English=int(input("Enter marks of the first subject: "))
Math=int(input("Enter marks of the second subject: "))
Nepali=int(input("Enter marks of the third subject: "))
Science=int(input("Enter marks of the fourth subject: "))
Social=int(input("Enter marks of the fifth subject: "))
avg=(English+Math+Nepali+Science+Social)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")

# Sum Of Natural Numbers

num = int(input('Enter a number: '))
sum = 0
x = 1
while x <= num:
 sum += x 
 x += 1
print('The sum of natural number =', sum)


#Simple Calculator

def add(x, y):
    return(x+y)
def subtract(x, y):
    return(x-y)
def multiply(x, y):
    return(x*y)
def devition(x, y):
    return(x/y)

x=6
y=10

#Caldendar Display Fucation

import calendar
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  

print(calendar.month(yy,mm))