import random
import art

ATTEMPTS_EASY = 10
ATTEMPTS_HARD = 5

def set_difficulty():
    """Set the number of attempts based on difficulty"""
    level = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    
    if level == "easy":
        return ATTEMPTS_EASY
    
    return ATTEMPTS_HARD
    

def get_guess():
    """Get the user's guess"""
    return int(input("Make a guess: "))

def compare_guess(answer, guess):
    """Compare the random number and user guess"""
    if answer == guess:
        print(f"You got it! The answer was {answer}.")
        return True
    if answer > guess:
        print("Too low.")
    else:
        print("Too high.")
    return False

def play_game():
    """Main game logic"""
    print(art.logo)

    # Generate the secret number for the game
    random_num = random.randint(1,100)
    #print(random_num)      # for debugging/testing

    # Set number of attempts based on difficulty
    attempts = set_difficulty()

    while attempts > 0:
        guess = get_guess()
        attempts -= 1
        
        if compare_guess(random_num, guess):
            return
        
        if attempts > 0:
            print("Guess again.")
            print(f"You have {attempts} attempts remaining.\n")
    
    print("You've run out of guesses. You lose.")

play_game()
