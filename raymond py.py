count = 0
guess = 6
while count < 3:
    input_one = int(input("enter a number: "))
    if input_one == guess:
        print("you guess right")
    if input_one > guess:
        print("number enter is greater than guess")
    elif input_one < guess:
        print("number enter is lesser than guess")



    count = count + 1

