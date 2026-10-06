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

art = [rock, paper, scissors]
randomchoice = ["rock", "paper", "scissors"]
random_ = random.randint(0, 2) # Chạy 1 lần duy nhất ở dòng này sau đó đưa kết quả vào art[random] và randomchoice[random]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n")

if user_choice == "0":
    print(f"You choose:{rock}")
    print("Computer choose:") 
    print(art[random_])
    if randomchoice[random_] == "rock":
        print("It's a draw")  
    elif randomchoice[random_] == "paper":
        print("You lose")
    else:
        print("You win")            

if user_choice == "1":
    print(f"You choose: {paper}")
    print("Computer choose:")
    print(art[random_])
    if randomchoice[random_] == "rock":
            print("You win")  
    elif randomchoice[random_] == "paper":
            print("It's a draw")
    else:
            print("You lose") 

if user_choice == "2":
    print(f"You choose: {scissors}")
    print("Computer choose:")
    print(art[random_])
    if randomchoice[random_] == "rock":
        print("You lose")  
    elif randomchoice[random_] == "paper":
        print("You win")
    else:
        print("It's a draw")
         