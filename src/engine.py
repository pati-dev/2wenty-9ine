"""Main file to test run the game.
"""
from players import Player

NUM_OF_MATCHES = 1
MATCH_NUM = 0


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
    player_names = ["P1", "P2", "P3", "P4"]
    players = {player: Player(num) for num, player in enumerate(player_names, start=1)}
    while MATCH_NUM <= NUM_OF_MATCHES:
        score, team = play_match()
        update_scoreboard(score, team)
    return


if __name__ == '__main__':
    main()