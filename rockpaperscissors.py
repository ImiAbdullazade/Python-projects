import random

def play_game():
    while True:
        print("rock,paper,scissors")
        print("enter your choice")
        print("1 rock")
        print("2 paper")
        print("3 scissors")

        user_choice = int(input("ur t:  "))
        while user_choice < 1 or user_choice > 3:
            user_choice = int(input("inv inp pls wite gain betwn 1 3 !!111!:  "))

        if user_choice == 1:
            user_choice_name = "rock"
        elif user_choice == 2:
            user_choice_name = "paper"
        else:
            user_choice_name = "scissors"
        
        computer_choice = random.randint(1, 3)

        if computer_choice == 1:
            computer_choice_name = "rock"
        elif computer_choice == 2:
            computer_choice_name = "paper"
        else:
            computer_choice_name = "scissors"

        print("you chosed ", user_choice_name)
        print("computer chosed", computer_choice_name)

        if user_choice == computer_choice:
            print('tie!1!!1!1!1111')
        elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
            print('congrats!11!1111!1!!!!!111 u wiiiiiiiin!111!1!1!1!1')
        else:
            print('u are gazbalon')

play_game() 