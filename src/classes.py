import random
import constants
import enum
import uuid
@enum.unique
class Suit(enum.Enum):
    HEARTS = 1
    SPADES = 2
    DIAMONDS = 3
    CLUBS = 4


@enum.unique
class CardType(enum.IntEnum):
    JACK = 8
    NINE = 7
    ACE = 6
    TEN = 5
    KING = 4
    QUEEN = 3
    EIGHT = 2
    SEVEN = 1

    def points(self) -> int:
        if self.name == "JACK":
            return 3
        elif self.name == "NINE":
            return 2
        elif self.name == "ACE" or self.name == "TEN":
            return 1
        else:
            return 0

class TrumpType(enum.Enum):
    
    NORMAL_HEARTS = ("NORMAL", Suit.HEARTS)
    NORMAL_SPADES = ("NORMAL", Suit.SPADES)
    NORMAL_DIAMONDS = ("NORMAL", Suit.DIAMONDS)
    NORMAL_CLUBS = ("NORMAL", Suit.CLUBS)
    REVERSE_HEARTS = ("REVERSE", Suit.HEARTS)
    REVERSE_SPADES = ("REVERSE", Suit.SPADES)
    REVERSE_DIAMONDS = ("REVERSE", Suit.DIAMONDS)
    REVERSE_CLUBS = ("REVERSE", Suit.CLUBS)
    NO_TRUMP = "NO_TRUMP"
    REVERSE_NO_TRUMP = "REVERSE_NO_TRUMP"

    def __init__(self, value, suit=None):
        self.suit = suit
        self.type = value
    
class Card:
    """Class for each card in the deck.
    """
    def __init__(self, suit: Suit, card_type: CardType):
        """Constructor for the class Card.

        Args:
            suit (Suit): Suit of the card. Represented by Enum
            card_type (CardType): Type of the Card. Also encodes its points. Represented by IntEnum
        """
        self.suit = suit
        self.card_type = card_type
        
    def show(self):
        print("{} of {}".format(self.card_type.name, self.suit.name))

    def key(self):
        return f"{self.suit.name}_{self.card_type.name}"

    # def __lt__(self, other):
    #     if self.suit == other.suit:
    #         pass

    def __eq__(self, other) -> bool:
        if self.suit == other.suit and self.card_type == other.card_type:
            return True
        return False

class Deck:
    """ Class for the deck of cards.
       
        Attrs:
            cards (list): A list of Card objects.
    """
    def __init__(self, shuffle: bool = True):
        """Constructor method for building a deck of cards. 

        Args:
            shuffle (bool, optional): Whether to shuffle the cards or not. Defaults to True.

        """
        cards = []
        for _, s in Suit.__members__.items():
            for _, ct in CardType.__members__.items():
                card = Card(suit=s, card_type=ct)
                cards.append(card)

        self.cards = cards 
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
        # Is it necessary to store information of the team with player object?
        # self.team = team
        self.name = name
        self.id = uuid.uuid4()
        # Should we rename this? Because according to our readme, a hand is 1 round of 4 cards
        # played by all 4 players with determined winner of the hand
        self.hand = []

    def draw(self, deck):
        self.hand.extend(deck.deal())
        return self
    
    def show_hand(self):
        for idx, card in enumerate(self.hand):
            print(idx, ":", constants.CARDS[card]['name'])
    
    def bid(self, max_bid):
        points = int(input("Make your bid. Should be greater than {}:".format(max_bid)))
        return points
    
    def play_card(self):
        self.show_hand()
        card_loc = int(input("Choose a card to play:"))
        self.hand.pop(card_loc)
