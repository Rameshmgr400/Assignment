import random
min_num = 1
max_num = 8
roll =  "yes"
while roll == "Yes" or roll == "y":
    print("Keep Rolling...")
    print("The Values Are :")
    print(random.randint(min_num, max_num))
    print(random.randint(min_num, max_num))
    roll - input("Can i roll again the dice? (yes/no) : ")
    a = (random.randint(min_num, max_num))
    b = (random.randint(min_num, max_num))
    print(a)
    print(b)
    roll - input("Can i roll again the dice? (yes/no) : ")
    if roll == "no" or roll == "n":
        print("Thank for playing, can play again!")
        break