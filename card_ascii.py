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

def print_hidden_card(pc, npc):
    print(10*'\n')
    print('NPC Cards\n')
    print(ascii_version_of_hidden_card(*npc.cards))
    print('Your Cards: \n')
    print(ascii_version_of_card(*pc.cards))
    print('Your total points: {}'.format(pc.points))

def print_card(pc,npc):
    print(10 * '\n')
    print('NPC cards:\n')
    print(ascii_version_of_card(*npc.cards))
    print('NPC total points: {}'.format(npc.points))
    print('Your cards:\n')
    print(ascii_version_of_card(*pc.cards))
    print('Your total points: {}'.format(pc.points))