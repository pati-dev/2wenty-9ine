"""Main file to test run the game.
"""
from os import name
from classes import Card, Deck, Player

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
    players = instantiate_players()
    deck = Deck(shuffle=True)
    deal_cards(deck, players)
    kholu, goal = bid(players)
    deal_cards(deck, players)
    players[0].play_card()
    return


def instantiate_players():
    P1 = Player(team="420", name="Khiladi")
    P2 = Player(team="420", name="Anari")
    P3 = Player(team="69", name="Harry")
    P4 = Player(team="69", name="Potter")
    players = [P1, P3, P2, P4]  # might want to define a function to allow users to decide the order
    return players


def deal_cards(deck, players) -> None:
    for player in players:
        player.draw(deck)
    return


def bid(players):
    P1, P2, P3, P4 = players
    return P2, 20


if __name__ == '__main__':
    main()