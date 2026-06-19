import random
print("*----- welcome to rock paper scissors game -----*")
choices =["rock","paper","scissors"] 
user_score = 0
comp_score = 0
while True:
    user_choice = input("Enter you choice(Rock, Paper, Scissors): ").lower()
    comp_choice = random.choice(choices)
    if user_choice not in choices:
        print("invalid choices")
        continue
    if user_choice == comp_choice:
        print("It's a tie!")

    elif (
        (user_choice == "rock" and comp_choice == "scissors") or
        (user_choice == "paper" and comp_choice == "rock") or
        (user_choice == "scissors" and comp_choice == "paper")
    ):
        print(f"computer choice is {comp_choice}")
        print("You win!")
        user_score += 1

    else:
        print(f"computer choice is {comp_choice}")
        print("Computer wins!")
        comp_score += 1

    
        
    new_game = input("Do you want to play again(yes/no): ").lower()
    if new_game == "yes":
        continue
    elif new_game == "no":
        print (f"your score is : {user_score}")
        print (f"computer score is : {comp_score}")
        if user_score > comp_score:
            print("you are the winner!!!")
        elif user_score < comp_score:
            print("computer is the winner!!!")
        elif user_score == comp_score:
            print("game is draw!!")
        break