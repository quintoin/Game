import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

suits_symbols = '♠', '♦', '♥', '♣'

class Card(object):

    card_values = {
        'Ace': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

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



class chips:

    def __init__(self):
        self.amount = 100
        self.min = 0

    def win_bet(self, amount):
        self.amount = self.amount + int(amount)

    def lose_bet(self, amount):
        self. amount = self.amount - int(amount)


def player_bet(cash_you_have):
    while True:
        bet = input('Please place your bet\n')

        try:
            if int(bet) > cash_you_have:
                print('Not enough cash')
                continue

        except:
            print('Please type a number')
            continue

        return bet


def ascii_version_of_card(*cards, return_string=True):

    suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suits_symbols = ['♠', '♦', '♥', '♣']

    lines = [[] for i in range(9)]

    for index, card in enumerate(cards):
        if card.rank == '10':
            rank = card.rank
            space = ''
        else:
            rank = card.rank[0]
            space = ' '

        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    if return_string:
        return '\n'.join(result)
    else:
        return result


def ascii_version_of_hidden_card(*cards):

    lines = [['┌─────────┐'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['│░░░░░░░░░│'], ['└─────────┘']]

    cards_except_first = ascii_version_of_card(*cards[1:], return_string=False)
    for index, line in enumerate(cards_except_first):
        lines[index].append(line)

    for index, line in enumerate(lines):
        lines[index] = ''.join(line)

    return '\n'.join(lines)


# GAME START
ask = input('Game is about to start, are you ready? y/n\n')
if ask == 'y' or ask == 'yes' or ask == 'Yes' or ask == 'YES':
    pass
else:
    print('Game exited')
    exit()

#initialize chips amount
player = chips()
print("You have 100 chips\n")

while player.amount > 0:
    new_deck = Deck()
    new_deck.shuffle()


    #First turn, place your bets
    bet = player_bet(player.amount)

    # initialize computer hand
    computer_hand = Hand()
    computer_hand.add_card(new_deck.deal())
    print('NPC Cards')
    computer_hand.add_card(new_deck.deal())
    print(ascii_version_of_hidden_card(*computer_hand.cards))

    #part for player game
    player_hand = Hand()
    player_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())
    print('\nYour Cards: ')
    print(ascii_version_of_card(*player_hand.cards))
    print('Your total points: {}'.format(player_hand.points))

    # player turn
    while player_hand.points <= 21:
        chose = input('Hit or stand?\n')
        if chose.lower() == 'hit':
            player_hand.add_card(new_deck.deal())
            player_hand.adjust_for_ace()
            print('NPC cards:\n')
            print(ascii_version_of_hidden_card(*computer_hand.cards))
            print('Your cards:\n')
            print(ascii_version_of_card(*player_hand.cards))
            print('Your total points: {}'.format(player_hand.points))

        elif chose.lower() == 'stand':
            break
        else:
            print("Please write either 'hit' or 'stand'\n")
            continue
    #player turn end
    #check if he busted, if not - call computer
    if player_hand.points > 21:
        print('BUSTED')
        player.lose_bet(bet)
        print('You have {} chips left'.format(player.amount))
        continue
    # end check



    #start computer game
    while player_hand.points > computer_hand.points:
        computer_hand.add_card(new_deck.deal())
        time.sleep(4)
        print('NPC cards:\n')
        print(ascii_version_of_card(*computer_hand.cards))
        print('NPC total points: {}'.format(computer_hand.points))
        time.sleep(1)
        print('Your cards:\n')
        print(ascii_version_of_card(*player_hand.cards))
        print('Your total points: {}'.format(player_hand.points))
    #end computer game
    #check who wins
    if computer_hand.points > 21:
        player.win_bet(bet)
        print('Computer bust! Congratulations, now you have {} chips!'.format(player.amount))
    else:
        print('Computer won! You lost {} chips'.format(bet))
        player.lose_bet(bet)
        print('You have {} chips left'.format(player.amount))

print('Vi proebalis')

