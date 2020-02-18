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
        bet = input('\nPlease place your bet\n')

        try:
            if int(bet) > cash_you_have:
                print('Not enough cash')
                continue

        except:
            print('Please type a number')
            continue

        return bet

