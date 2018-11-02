import random

user_points = 0
user_input = 15
while user_input != "EXIT":
    random_numer = random.randrange(1,11)
    while random_numer != user_input:
        user_input = input("Guess a number between 1 and 10 bitch! type Exit to give up: ")
        user_input = user_input.upper()
        if user_input == "EXIT":
            print ("Bye bye")
            print (user_points)
            break
        else:
            try:
                user_input = int(user_input)
                if user_input == random_numer:
                    print ("You guessd it right!")
                    user_points += 1
                elif user_input > random_numer:
                    print ("Too high, try again")
                elif user_input < random_numer:
                    print ("Too low, try again")
                else:
                    print ("only type a number between 1 and 10")
            except ValueError:
                print("wrong input idiot")
            except TypeError:
                print("this code should never be seen")
        
