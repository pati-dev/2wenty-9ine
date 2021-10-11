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
        card_loc = int(input("Choose a card to play: "))
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
        team1 = str(input("Name for team 1: ") or "Team 1")
        team2 = str(input("Name for team 2: ") or "Team 2")
        t1p1 = input("Player {} for team {}: ".format(1, team1) or "Player 1 Team 1")
        t1p2 = input("Player {} for team {}: ".format(2, team1) or "Player 2 Team 1")
        t2p1 = input("Player {} for team {}: ".format(1, team2) or "Player 1 Team 2")
        t2p2 = input("Player {} for team {}: ".format(2, team2) or "Player 2 Team 2")

        P1 = Player(team1, t1p1)
        P2 = Player(team1, t1p2)
        P3 = Player(team2, t2p1)
        P4 = Player(team2, t2p2)
        return [P1, P2, P3, P4]

    def start_game(self):
        self.playing = True
        self.players = self.create_players()
        self.activate_player(self.players[0])
        DealCards(self).action(self.players)
        
        self.activate_player(self.players[1])
        BidPoints(self).action()

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
    def __init__(self, game: Game):
        self.game = game
        self.player = self.game.active_player

    def action(self, players: list):
        for player in players:
            player.draw(self.game.deck)


class BidPoints(States):
    def __init__(self, game: Game):
        self.game = game
        self.player = self.game.active_player
        self.max_bid = 17
        self.kholu = None

    def action(self):
        bid = int(input("Highest bid: {} | Enter bid amount: (0 to pass)").format(self.max_bid))
        if not(bid):
            return 
        self.validate_bid(bid)

    def validate_bid(self, bid):
        if self.player == self.kholu:
            return bid >= self.max_bid
        else:
            return bid > self.max_bid
