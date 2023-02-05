import random
actions = ["rock", "paper", "scissor"]

computer_score = 0
player_score = 0

total_rounds = input("How many want to rounds:  ")
round_counter = 0

while True :
  round_counter += 1
  print(f"Round number: {round_counter}")

  computer_choice = random.choice(actions)
  player_choice = input("What is your choice:  ")

  print(f"Player choice is :  {player_choice}")
  print(f"Computer choice is :  {computer_choice}")


  if computer_choice == player_choice:
    print("Tie! Both players choose the same actions.")

  elif computer_choice== "paper" and player_choice== "rock":
    computer_score += 1
    print("COMPUTER WON!")

  elif computer_choice== "rock" and player_choice== "paper":
    player_score += 1
    print("PLAYER WON!")

  elif computer_choice== "rock" and player_choice== "scissor":
    computer_score += 1
    print("COMPUTER WON!")
    
  elif computer_choice== "scissor" and player_choice== "rock":
    player_score += 1
    print("PLAYER WON!")

  elif computer_choice== "scissor" and player_choice== "paper":
    computer_score += 1
    print("COMPUTER WON!")

  elif computer_choice== "paper" and player_choice== "scissor":
    player_score += 1
    print("PLAYER WON!")
  

  if round_counter == int(total_rounds):
    print("GAME IS OVER!")
    if computer_score == player_score:
      print("There is no winner, tie.")
    elif computer_score >= player_score:
      print(f"Winner is computer with score {computer_score} : {player_score}")
    else:
      print(f"winer is player with score {player_score} : {computer_score}")
    break




