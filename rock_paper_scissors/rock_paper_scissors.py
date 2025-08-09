import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
option = [rock, paper, scissors]

playerA = input("Select \"rock\", \"paper\" or \"scissor\":\n").lower()

if playerA == "rock":
    playerA_selection = 0
    print(f"Player A:\n{option[playerA_selection]}")
elif playerA == "paper":
    playerA_selection = 1
    print(f"Player A:\n{option[playerA_selection]}")
elif playerA == "scissor":
    playerA_selection = 2
    print(f"Player A:\n{option[playerA_selection]}")
else:
    print("Error: Invalid selection")
    exit()

playerB_selection = random.randint(0,2)
print(f"Player B:\n{option[playerB_selection]}")

if (playerA_selection == 0) and (playerB_selection == 1):
    print("You lose")
elif (playerA_selection == 0) and (playerB_selection == 2):
    print("You won")
elif (playerA_selection == 1) and (playerB_selection == 0):
    print("You won")
elif (playerA_selection == 1) and (playerB_selection == 2):
    print("You lose")
elif (playerA_selection == 2) and (playerB_selection == 0):
    print("You lose")
elif (playerA_selection == 2) and (playerB_selection == 1):
    print("You won")
else:
    print("its a draw")