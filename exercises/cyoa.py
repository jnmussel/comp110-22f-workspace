"""Choose your own adventure exercise."""

__author__ = "730471672"

player: str = input("Welcome to the coin flipping game! What is your name? ")

def greet() -> None:
    global player
    print(f"Welcome {player}! This is a game in which you will try to guess if a coin lands on heads or tails. The objective is to guess as many right as possible in a row! For each guessed correctly, a point will be added to your score. ")
    print("To guess heads, enter 'H', to guess tails, enter 'T', to quit the game, enter 'Q', and to begin a new game, enter 'N'. ")


POINTS: int = 0

def coin_points(player_points: int) -> int:
    """Adds points to the global score. """
    global POINTS
    POINTS += player_points
    return POINTS


def coin_flip_correct(player_int: int) -> bool:
    from random import randint
    result: int = randint(0, 1)
    if player_int == result:
        return True
    else:
        return False
        


def main() -> None:
    greet()
    print("Let's start! ")
    playing = True
    while playing == True:
        playing_input: str = "Flipping coin! Go ahead and call it! "
        if playing_input == "H":
            if coin_flip_correct(0) == True:
                print("You guessed correctly! ")
                print(f"Total points: {coin_points(1)}")
            else:
                print("Sorry! You guessed wrong. Game over.")
                print(f"Total points: {coin_points(0)}")
                playing = False
        elif playing_input == "T":
            if coin_flip_correct(1) == True:
                print("You guessed correctly! ")
                print(f"Total points: {coin_points(1)}")
            else:
                print("Sorry! You guessed wrong. Game over.")
                print(f"Total points: {coin_points(0)}")
                playing = False
        elif playing_input == "N":
            main()
        elif playing_input == "Q":
            exit()
        else:
            print("Not valid input.")
    
    print(f"Thanks for playing! Your score: {POINTS}")

if __name__ == "__main__":
  main()
        



    

