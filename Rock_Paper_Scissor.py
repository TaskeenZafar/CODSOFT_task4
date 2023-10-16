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

# Write your code below this line 👇
image = [rock, paper, scissors]

while True:
    choose = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
    print(image[choose])
    computer_choice = random.randint(0, 2)
    print(f"computer choose {computer_choice}")

    print(image[computer_choice])
    if choose >= 3 or choose < 0:
        print("This is invalid input, you lose!")
    elif choose == 0 or computer_choice == 2:
        print("you win!")
    elif choose == 2 or computer_choice == 0:
        print("you lose!")
    elif choose > computer_choice:
        print("you win!")
    elif choose < computer_choice:
        print("You lose!")
    else:
        print("It's draw!")
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break


