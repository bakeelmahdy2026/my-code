import random
rock_ascii = """
     _____
  --  ____)
      (____)
      (_____)
      (____)
  --__(___)
"""
paper_ascii = """
    ______
---   ____)__
       ______)_
        _______)
        ______)
   --- ______)
"""
scissors_ascii = """
    _____
---   ___)___
       ______)_
        _______)
       (___)
  ---__(___)
"""

print("\nWelcome to the Rock, Scissors game: ")
confirm = input("Press Enter to continue or type (Help) for the rules ").lower()
if confirm == "help":
    print("\n      ⁕⁕⁕⁕⁕⁕⁕ RULES ⁕⁕⁕⁕⁕⁕⁕")
    print("      1) You choose and the computer chooses")
    print("      2) Rock smashes Scissors -> Rock wins")
    print("      3) Scissors cut paper -> Scissors win")
    print("      4) Paper covers Rock -> Paper wins")
user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choise. Please run the program again and choose rock, paper, or scissors.")
else:
    if user_choice == "rock":
        print(f"\nYou chose:\n{rock_ascii}")
    elif user_choice == "paper":
        print(f"\nYou choce:\n{paper_ascii}")
    else:
        print(f"\nYou choce:\n{scissors_ascii}")




    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    if computer_choice == "rock":
        print(f"\ncomputer chose:\n{rock_ascii}")
    elif computer_choice == "paper":
        print(f"\ncomputer choce:\n{paper_ascii}")
    else:
        print(f"\ncomputer choce:\n{scissors_ascii}")


if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors")
     or
    (user_choice == "paper" and computer_choice == "rock")
     or
    (user_choice == "scissors" and computer_choice == "paper")
    ):
    print(f"You win! {user_choice} beats {computer_choice}.")
else:
    print(f"You lose! {computer_choice} beats {user_choice}.")
