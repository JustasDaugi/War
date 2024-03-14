import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck_str = '.'.join([str(card) for card in self.cards])
        return f"Deck: [{deck_str}]"



class Player:
    def __init__(self, deck):
        self.deck = deck
        self.player1 = []
        self.player2 = []

    def split_deck(self):
        self.player1 = self.deck.cards[:26]
        self.player2 = self.deck.cards[26:]

    def __str__(self):
        player1_cards = ', '.join(str(card) for card in self.player1)
        player2_cards = ', '.join(str(card) for card in self.player2)
        return f"Player1: [{player1_cards}]\nPlayer2: [{player2_cards}]"

deck = Deck()
deck.shuffle()
player = Player(deck)
player.split_deck()
print(player)