"""Main file to test run the game.
"""
from players import Player

NUM_OF_MATCHES = 1


def main():
    """
    Begin series:
        Define stopping condition (num of matches)
        Initialize players
        Initialize scoreboard
    Begin match:
        Identify dealer
        Shuffle and deal 4 cards
        Identify kholu and color of trump
        Deal remaining 4 cards
    Begin hand:
        Identify color for the hand
        Identify active player
        ...
    """
    
    players = {
        'P1': Player(1, True),  # TODO: Randomly choose dealer instead of the first player
        'P2': Player(2),
        'P3': Player(3),
        'P4': Player(4)
    }
    
    return


if __name__ == '__main__':
    main()