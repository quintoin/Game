import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

class Card(object):

    card_values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit.capitalize()
        self.points = self.card_values[rank]


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.points = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.points = self.points + card.points
        if card.rank == 'Ace':
            self.aces = self.aces + 1

    def adjust_for_ace(self):
        if self.aces > 0 and self.points > 21:
            self.points = self.points - 10
            self.aces -= 1