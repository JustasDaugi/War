import random
from constants import ranks, suits
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []

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

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


    def show_cards(self, card1, card2):
        print(f"Player 1 card: {card1} - Player 2 card: {card2}")

    def play_round(self):
        if not self.player1 or not self.player2:
            return

        card1 = self.player1.pop(0)
        card2 = self.player2.pop(0)
        cards_in_play = [card1, card2]

        rank1 = ranks.index(card1.rank)
        rank2 = ranks.index(card2.rank)

        self.show_cards(card1, card2)

        if rank1 > rank2:
            check_win = "Player 1 wins this round"
            self.player1.append(cards_in_play)
            print(check_win)
            return check_win
        elif rank2 > rank1:
            check_win = "Player 2 wins this round"
            self.player2.append(cards_in_play)
            print(check_win)    
            return check_win
        else:
            tie = f"{card1} and {card2} are equal. It's a tie!"
            print(tie)
            return tie
    
    def play_game(self):
        rounds = 0
        while rounds <= 20:
            if rounds == 5:
                if len(self.player1) > len(self.player2):
                    print("Player 1 wins!")
                    break
                else:
                    print("Player 2 wins")
                    break
                
            self.play_round()
            next_round = input("Press enter to play the next round or 'q' to quit: ")
            rounds += 1

            

            



            



    def start_game():
        deck = Deck()
        deck.shuffle()

        player = Player(deck)
        player.split_deck()

        game = Game(player.player1, player.player2)
        game.play_game()

Game.start_game()