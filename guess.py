from random import randint

def generator():
    return randint(1, 10)

def rand_guess():
    randomnumber = generator()
    guess_left = 3
    flag = 0
    while guess_left > 0:
        guess = int(input("Pick your number to "
                          "enter the lucky draw\n"))
        if guess == randomnumber:
            flag = 1
            break
        else:
            print("Sorry You Are Wrong!!")
        guess_left -= 1
    if flag is 1:
        return True
    else:
        return False

result = rand_guess()

if result is True:
  print("Congrats!! You Won.")
else:
  print("Sorry, Better Luck Next Time!")