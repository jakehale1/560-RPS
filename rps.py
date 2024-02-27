import random  

def get_user_choice():
    user_choice = input("Choose (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def det_win(user_choice, c_c):
    if user_choice == c_c:
        return "U tied!"
    elif (user_choice == "rock" and c_c == "scissors") or \
         (user_choice == "paper" and c_c == "rock") or \
         (user_choice == "scissors" and c_c == "paper"):
        return "U win!"
    else:
        return "U lose!"

def play_game():
    print("Let's play rock, paper, scissors!")

    while True:
        user_choice = get_user_choice()  
        c_c = get_computer_choice()  

        print(f"U chose {user_choice}.")
        print(f"C chose {c_c}.")

        result = det_win(user_choice, c_c)  
        print(result)

        play_again = input("Play again? (y/n): ").lower()  
        if play_again != 'y':
            print("Thanks. Bye!")
            break

if __name__ == "__main__":
    play_game()
