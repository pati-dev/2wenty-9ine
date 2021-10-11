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
    def __init__(self, team: str, name: str):
        """Constructor to define a player.

        Args:
            team (str): Unique name for player's team.
            name (str): Name of the player.
        """
        self.team = team
        self.name = name
        self.hand = []

    def draw(self, deck: Deck):
        self.hand.extend(deck.deal())
    
    def show_hand(self):
        for idx, card in enumerate(self.hand):
            print(idx, ":", constants.CARDS[card]['name'])
    
    def bid(self, points: int):
        return points
    
    def play_card(self):
        self.show_hand()
        card_loc = int(input("Choose a card to play:"))
        self.hand.pop(card_loc)

    def set_trump(self, deck: Deck):
        trump = int(input("Choose the trump for this game:\n{}\n".format(constants.TRUMPS)))
        deck.set_trump(trump)


class Game:
    """Core class for the game engine.
    """
    def __init__(self):
        self.deck = Deck(shuffle=True)
        self.playing = False
        self.state = None
        self.players = None
        self.active_player = None

    def create_players(self):
        team1 = str(input("Name for team 1:"))
        team2 = str(input("Name for team 2:"))
        t1p1 = input("Player {} for team {}:".format(1, team1))
        t1p2 = input("Player {} for team {}:".format(2, team1))
        t2p1 = input("Player {} for team {}:".format(1, team2))
        t2p2 = input("Player {} for team {}:".format(2, team2))

        P1 = Player(team1, t1p1)
        P2 = Player(team1, t1p2)
        P3 = Player(team2, t2p1)
        P4 = Player(team2, t2p2)
        return [P1, P2, P3, P4]

    def start_game(self):
        self.playing = True
        self.players = self.create_players()
        self.activate_player(self.players[0])
        DealCards(self, self.players).action()

    def validate_kickoff(self):
        return True

    def activate_player(self, player: Player):
        self.active_player = player


class States(ABC):
    """Superclass for states of the game 29.
    """
    def __init__(self, game: Game, player: Player):
        raise NotImplementedError


class DealCards(States):
    def __init__(self, game: Game, players: list):
        self.game = game
        self.players = players

    def action(self):
        for player in self.players:
            player.draw(self.game.deck)
