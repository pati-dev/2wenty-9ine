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
    """Class 
    """

class Player():
    """A class to define the behaviour of each of the 4 players playing the game.
    """
    def __init__(self, uid: int, dealer: bool = False) -> None:
        uid = uid
        dealer = dealer
