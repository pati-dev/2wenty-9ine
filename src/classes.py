import random
import constants

class Card:
    """Class for each card in the deck.
    """
    def __init__(self, suit: str, value: 'str', points: int, order: int) -> None:
        """Constructor for the class Card.

        Args:
            suit (str): Suit of the card.
            value (str): Value of the card.
            points (int): Number of points the card is worth.
            order (int): Rank of the card as compared to other cards.
        """
        self.suit = suit
        self.value = value
        self.points = points
        self.order = order
        
    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    """Class for the deck of cards.
    """
    def __init__(self, shuffle: bool = False) -> list:
        """Constructor method for building a deck of cards.

        Args:
            shuffle (bool, optional): Whether to shuffle the cards or not. Defaults to False.

        Returns:
            list: Ordered deck of cards.
        """
        self.cards = list(constants.CARDS)
        if shuffle:
            random.shuffle(self.cards)
    
    def deal(self):
        dealt = self.cards[:4]
        self.cards = self.cards[4:]
        return dealt


class Player():
    """A class to define the behaviour of each of the 4 players playing the game.
    """
    def __init__(self, team: str, name: str) -> None:
        """Constructor to define a player.

        Args:
            team (int): Unique key for player's team.
            name (str): Name of the player.
        """
        self.team = team
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.extend(deck.deal())
        return self
    
    def bid(self, max_bid):
        points = int(input("Make your bid. Should be greater than {}:".format(max_bid)))
        return points
    
    def play_card(self):
        for idx, card in enumerate(self.hand):
            print(idx, ":", constants.CARDS[card]['name'])
        card_loc = int(input("Choose a card to play:"))
        self.hand.pop(card_loc)
