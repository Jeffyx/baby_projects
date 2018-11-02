import random
user_input = ("X")
while user_input != ("EXIT"):
    correct_input = False
    bag_dice = {
        "A": 5,
        "B": 7,
        "C": 13,
        "D": 21
    }
    user_input = input("Type A, B, C, or D for a 4, 6, 12 or 20 sided die. Please type exit to quit: ")
    user_input = user_input.upper()
    if user_input == "EXIT":
      print ("shutting down app")
      correct_input = True

    for x in bag_dice.keys():
        if user_input == x:
            print (random.randrange(1, bag_dice[user_input]))
            correct_input =True
            break
    if correct_input == False:
        print ("Your input is wrong!")