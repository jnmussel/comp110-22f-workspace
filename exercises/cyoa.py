"""Choose your own adventure exercise."""

__author__ = "730471672"


points: int = 0
player: str
NAMED_CONSTANT: str = ("\U0001FA99")
MONEY_BAG: str = ("\U0001F4B0")


def greet() -> None:
    """Greets player and gets name."""
    global player
    player = input("Welcome to the coin flipping game! What is your name? ")
    print(f"Welcome {player}! \n This is a game in which you will try to guess if a coin lands on heads or tails. \n The objective is to guess as many right as possible in a row! \n For each guessed correctly, a point will be added to your score. ")
    print("To guess heads, enter 'H' to guess tails, enter 'T', to quit the game, enter 'Q'. ")
    print("Let's start! ")


def coin_points(player_points: int) -> int:
    """Adds points to the global score."""
    global points
    points += player_points
    return points


def coin_flip_correct(player_int: int) -> bool:
    """Coin flip procedure."""
    from random import randint
    result: int = randint(0, 1)
    if player_int == result:
        return True
    else:
        return False
        

def main() -> None:
    """Main function call and game loop."""
    greet()
    
    playing = True
    while playing:
        playing_input: str = input(f"Flipping coin! Go ahead and call it! \n {MONEY_BAG} \n {NAMED_CONSTANT} \n {NAMED_CONSTANT} \n {NAMED_CONSTANT} \n")

        if playing_input == "H" and coin_flip_correct(0) is True:
            print("You guessed correctly! ")
            print(f"Total points: {coin_points(2)}")

        elif playing_input == "T" and coin_flip_correct(1) is True:
            print("You guessed correctly! ")
            print(f"Total points: {coin_points(2)}")
        
        elif playing_input == "Q":
            print("Thanks for playing!")
            print(f"Total points : {coin_points(0)}")
            exit()
        
        elif playing_input != "T" and playing_input != "H" and playing_input != "Q": 
            print("Not valid input.")

        else:
            print("Sorry! You guessed wrong. Game over.")
            print(f"Total points: {coin_points(1)}")
            playing = False

        
if __name__ == "__main__":
    main()