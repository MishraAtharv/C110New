# Import the random module
import random

# Define a function to draw a dice face using symbols
def draw_dice_face(n):
  # Define the symbols for the top, bottom, left, right and dot
  top = "-"
  bottom = "-"
  left = "["
  right = "]"
  dot = "0"

  # Define the patterns for each number from 1 to 6
  patterns = {
    1: f" {top * 5} \n{left}  {dot}  {right}\n {bottom * 5} ",
    2: f" {top * 5} \n{left} {dot}   {right}\n{left}   {dot} {right}\n {bottom * 5} ",
    3: f" {top * 5} \n{left} {dot}   {right}\n{left}  {dot}  {right}\n{left}   {dot} {right}\n {bottom * 5} ",
    4: f" {top * 5} \n{left} {dot} {dot} {right}\n{left} {dot} {dot} {right}\n {bottom * 5} ",
    5: f" {top * 5} \n{left} {dot} {dot} {right}\n{left}  {dot}  {right}\n{left} {dot} {dot} {right}\n {bottom * 5} ",
    6: f" {top * 5} \n{left} {dot} {dot} {right}\n{left} {dot} {dot} {right}\n{left} {dot} {dot} {right}\n {bottom * 5} "
  }

  # Return the pattern for the given number
  return patterns[n]

# Ask the user to enter the number of players
num_players = int(input("Enter the number of players: "))

# Create a list to store the players' names
players = []

# Create a dictionary to store the players' numbers
numbers = {}

# Loop through the number of players
for i in range(num_players):
  # Ask the user to enter the name of each player
  name = input(f"Enter the name of player {i + 1}: ")
  # Add the name to the list
  players.append(name)
  # Initialize the number to zero
  numbers[name] = 0

# Define a flag to control the loop
keep_rolling = True

# Loop until the user wants to stop
while keep_rolling:
  # Loop through the players
  for player in players:
    # Print the player's name
    print(f"It's {player}'s turn.")
    # Generate a random number from 1 to 6
    n = random.randint(1, 6)
    # Print the dice face
    print(draw_dice_face(n))
    # Update the number for the player
    numbers[player] = n
    # Ask the user if they want to roll again or check the numbers
    answer = input("Do you want to roll again (y), check the numbers (c) or stop the game (n)? ")
    # Check the answer
    if answer.lower() == "y":
      # Continue the loop
      keep_rolling = True
    elif answer.lower() == "c":
      # Print the numbers for each player
      print("The numbers for each player are:")
      for name, number in numbers.items():
        print(f"{name}: {number}")
    elif answer.lower() == "n":
      # Break the loop
      keep_rolling = False
      print("Thank you for playing!")
      break
    else:
      # Invalid input
      print("Please enter y, c or n.")
