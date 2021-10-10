import random
import constants
from abc import ABC

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
    def __init__(self, shuffle: bool = False):
        """Constructor method for building a deck of cards.

        Args:
            shuffle (bool, optional): Whether to shuffle the cards or not. Defaults to False.

        Returns:
            list: Ordered deck of cards.
        """
        self.cards = list(constants.CARDS)
        if shuffle:
            random.shuffle(self.cards)
        self.trump = None
    
    def deal(self):
        dealt = self.cards[:4]
        self.cards = self.cards[4:]
        return dealt

    def set_trump(self, trump):
        self.trump = constants.TRUMPS[trump]


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
        self.show_hand()
    
    def show_hand(self):
        for idx, card in enumerate(self.hand):
            print(idx, ":", constants.CARDS[card]['name'])
    
    def bid(self, points):
        return points
    
    def play_card(self):
        self.show_hand()
        card_loc = int(input("Choose a card to play:"))
        self.hand.pop(card_loc)

    def set_trump(self, deck):
        trump = int(input("Choose the trump for this game:\n{}\n".format(constants.TRUMPS)))
        deck.set_trump(trump)


class Game:
    """Core class for the game engine.
    """
    def __init__(self, n):
        self.games = n
        self.current_game = 0
        self.playing = False
        self.state = None
        self.teams = {1: 'Team 1', 2: 'Team 2'}
        self.players = {}
        self.dealer = None

    def create_teams(self):
        self.teams[1] = str(input("Name for team 1:"))
        self.teams[2] = str(input("Name for team 2:"))
        self.assign_players()

    def assign_players(self):
       self.players = {team: input("Player {} for team {}:".format(idx, team)) for idx, team in self.teams.items()}

    def start_game(self):
        self.current_game += 1
        assert (self.playing == False) & (self.validate_kickoff())
        self.playing = True
        self.state = DealCards(self)

    def validate_kickoff(self):
        return self.current_game <= self.games


class States(ABC):
    """Superclass for states of the game 29.
    """
    def __init__(self, game):
        raise NotImplementedError


class DealCards(States):
    def __init__(self, game):
        if not(game.dealer):
            game.
