# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file 'Hi-score.txt' which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-
# score whenever the game() function breaks the Hi-score.
import random

def game():
    print("You are playing the game...")
    return random.randint(1, 62)

# Read the current high score
with open("Hi-score.txt", "r") as f:
    highscore_str = f.read()
    
# Get current game score
score = game()

# Convert high score if file is not empty
if highscore_str != "":
    highscore = int(highscore_str)
else:
    highscore = 0

print(f"Your score: {score}")

# Update high score if current score is higher
if score > highscore:
    print("Congratulations! New high score!")
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))