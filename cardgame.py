'''
Program     : Uno Card Game Simulator
Filename    : cardgame.py
Author      : Yoganand Kodali
Description :
    A minimal Uno card game simulator built in Python.
    Implements deck creation, card dealing, drawing, discarding,
    matching, and a full game loop using functional design.

    Each card is a 2-character string: digit (1-9) + color (r/g/b/y)
    Example: '5r' = five red, '9y' = nine yellow
'''

from random import shuffle


def makeDeck():
    '''
    Creates and returns a 36-card Uno deck.
    9 numbers (1-9) across 4 colors (r, g, b, y) = 36 unique cards.
    The deck is returned in order, not shuffled.
    '''
    colors = list('rgby')
    numbers = list(range(1, 10))
    deck = []
    for color in colors:
        for number in numbers:
            deck.append(f'{number}{color}')
    return deck


def deal(deck, players=2, cards=7):
    '''
    Deals cards to players in round-robin order and starts the discard pile.
    Removes (players * cards + 1) cards from the deck.

    Returns:
        hands (list of lists): one hand per player
        pile  (list):          the initial discard card
    '''
    hands = [[] for _ in range(players)]
    pile = []

    for i in range(cards):
        for player in range(players):
            card = deck.pop()
            hands[player].append(card)

    pile.append(deck.pop())
    return hands, pile


def draw(deck, playerHand):
    '''
    Draws the top card from the deck into the player's hand.
    Returns the card drawn, or None if the deck is empty.
    '''
    if len(deck) > 0:
        cardAdded = deck.pop()
        playerHand.append(cardAdded)
        return cardAdded
    else:
        print('The deck is empty. No cards can be drawn.')
        return None


def discard(pile, playerHand, playerCard):
    '''
    Moves a card from the player's hand to the top of the discard pile.
    Does nothing if the card is not in the player's hand.
    '''
    if playerCard in playerHand:
        playerHand.remove(playerCard)
        pile.append(playerCard)
    else:
        print(f'Card {playerCard} not found in hand.')


def match(pile, playerHand):
    '''
    Finds a card in the player's hand that matches the top of the discard pile
    by either value (digit) or color.
    Returns the first matching card found, or None if no match exists.
    '''
    top_card = pile[-1]
    matching_cards = [
        card for card in playerHand
        if card[0] == top_card[0] or card[1] == top_card[1]
    ]
    return matching_cards[0] if matching_cards else None


def play(deck, pile, playerHand):
    '''
    Runs one turn for a single player.
    If a matching card exists, discards it. Otherwise draws from the deck.
    Returns True if the player wins (hand is now empty), False otherwise.
    '''
    matching_card = match(pile, playerHand)

    if matching_card:
        discard(pile, playerHand, matching_card)
    else:
        draw(deck, playerHand)

    return len(playerHand) == 0


def supervisor(deck, pile, hands, pause=True):
    '''
    Runs the full game loop in round-robin order until one player wins.
    If pause=True, waits for Enter between each move.
    Returns the index of the winning player.
    '''
    while True:
        for i, hand in enumerate(hands):
            print(f'PLAYER #{i}:\n\thand= {hand}')
            print(f'\ttop of pile: {pile[-3:]}')
            print(f'\tend of deck: {deck[-4:]}', end='')
            if pause:
                input(' ...\n')
            if play(deck, pile, hand):
                print(f'\nPlayer #{i} wins!')
                return i
            print(f'\n#{i}: end of round hand= {hand}')
            print(f'          top of pile= {pile[-1]}\n')


def initialize(nPlayers, nCards):
    '''
    Sets up a game from scratch: creates the deck, shuffles it,
    deals hands, and starts the discard pile.

    Returns:
        deck  (list): remaining cards
        pile  (list): starting discard pile
        hands (list): one hand per player
    '''
    deck = makeDeck()
    shuffle(deck)
    hands, pile = deal(deck, nPlayers, nCards)
    return deck, pile, hands


if __name__ == '__main__':

    # --- Uncomment to run a game simulation ---
    # deck, pile, hands = initialize(2, 3)
    # print(f'{hands= }')
    # print(f'{pile= }\n')
    # winner = supervisor(deck, pile, hands, pause=False)
    # print(f'\nWinning hand is #{winner}!\n')
    # for i, hand in enumerate(hands):
    #     print(f'player #{i}: {hand= } {"WINNER!" if not hand else ""}')

    # --- Built-in tests ---
    deck = makeDeck()
    s = 'makeDeck() failed!'
    _c = list(map(lambda x: x[-1], deck))
    _n = list(map(lambda x: x[0], deck))
    assert len(deck) == 36, f'{s} deck not 36 cards long.'
    assert _c.count('r') == _c.count('g') == _c.count('b') == _c.count('y') == 9, f'{s} bad color'
    assert _n.count('1') == _n.count('2') == _n.count('3') == 4, f'{s} bad digit 1..3'
    assert _n.count('4') == _n.count('5') == _n.count('6') == 4, f'{s} bad digit 4..6'
    assert _n.count('7') == _n.count('8') == _n.count('9') == 4, f'{s} bad digit 7..9'
    print('makeDeck() tests passed!\n')

    s = 'deal() failed!'
    deck = ['xx', '4z', '4y', '4x', '3z', '3y', '3x', '2z', '2y', '2x', '1z', '1y', '1x']
    [hx, hy, hz], pile = deal(deck, 3, 4)
    assert deck == [], f'{s} bad deck'
    assert set(hx) == {'1x', '2x', '3x', '4x'}, f'{s} bad hand #1'
    assert set(hy) == {'1y', '2y', '3y', '4y'}, f'{s} bad hand #2'
    assert set(hz) == {'1z', '2z', '3z', '4z'}, f'{s} bad hand #3'
    assert pile == ['xx'], f'{s} bad pile'
    print('deal() tests passed!\n')

    s = 'match() failed!'
    pile, hand = ['6g', '2r'], ['3b', '2y']
    assert match(pile, hand) == '2y', f'Number {s}'
    pile, hand = ['6g', '2r'], ['3r', '4y']
    assert match(pile, hand) == '3r', f'Color {s}'
    pile, hand = ['6g', '2r'], ['6g', '7y']
    assert match(pile, hand) is None, f'{s}'
    print('match() tests passed!\n')

    s = 'discard() failed!'
    pile, hand, card = ['6g', '2r'], ['7r', '2y', '3b'], '2y'
    result = discard(pile, hand, card)
    assert pile == ['6g', '2r', '2y'], f'{s} bad pile'
    assert set(hand) == {'7r', '3b'}, f'{s} bad hand'
    assert result is None, f'{s} bad return value'
    print('discard() tests passed!\n')

    s = 'draw() failed!'
    deck, hand = ['6g', '2r', '1y'], ['7r', '3b']
    result = draw(deck, hand)
    assert deck == ['6g', '2r'], f'{s} bad deck'
    assert set(hand) == {'7r', '3b', '1y'}, f'{s} bad hand'
    assert result == '1y', f'{s} bad return value'
    print('draw() tests passed!\n')

    s = 'play() failed!'
    deck, pile, hand = ['6g', '2r', '1y'], ['1r', '3b'], ['7r', '2b', '9y']
    result = play(deck, pile, hand)
    assert deck == ['6g', '2r', '1y'], f'{s} bad deck'
    assert pile == ['1r', '3b', '2b'], f'{s} bad pile'
    assert set(hand) == {'7r', '9y'}, f'{s} bad hand'
    assert result is False, f'{s} bad result'

    deck, pile, hand = ['6g', '2r', '1y'], ['1r', '3b'], ['2b']
    result = play(deck, pile, hand)
    assert pile == ['1r', '3b', '2b'], f'{s} bad pile'
    assert hand == [], f'{s} bad hand'
    assert result is True, f'{s} bad result'
    print('play() tests passed!\n')

    print('All tests passed!')
