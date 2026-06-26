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

options = [rock, paper, scissors]

computers_index = random.randint(0, 2)

users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if users_choice <= 2:
    print(options[users_choice])

    print(f"Computer chose:\n{options[computers_index]}")

    if computers_index == 2 and users_choice == 0:
        print("You win!")
    elif computers_index == 0 and users_choice == 2:
        print("Your lose!")
    elif users_choice > computers_index:
        print("You win!")
    elif users_choice < computers_index:
        print("Your lose!")
    elif users_choice == computers_index:
        print("It's a draw!")

else:
    print("Select a valid option.")