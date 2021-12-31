import random
game_won = False
try_counter = 0
number = random.randint(1, 10)

player_name = input("Hello, what is your name?"'\n')
print("Okay", player_name, "I am thinking of a number between 1 and 10. Can you guess it?"'\n')

while game_won == False:
    try:
        player_guess = int(input())
    except ValueError:
        print("You need to enter a number silly. Why don't you try again.")
        try_counter += 1
        continue

    if player_guess < number:
        print("The number I'm thinking of is greater than", player_guess, "...")
        try_counter += 1

    elif player_guess > number:
        print("The number I'm thinking of is less than",player_guess, "...")
        try_counter += 1

    elif player_guess == number:
        print("Congratulations", player_name, "you won! My number was", number)
        try_counter  += 1
        print("It took you", try_counter, "tries. See if you can beat your score next time!")
        game_won = True
