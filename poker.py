def poker(hands):
    """
    ([hand, hand, habd, ...])->hand
    
    Return the best hand from list of hand
    >>> sf = ['JC','TC','9C','8C','7C']
    >>> fk = ['5S','5H','5D','5C','KS']
    >>> poker([sf, fk])
    ['JC', 'TC', '9C', '8C', '7C']
    """
    return max(hands, key=hand_rank)

def gen_card():
    """
    generate cards (52 cards)
    """
    rank = '23456789TJQKA'
    suits = []
    for i in rank:
        for j in 'CDHS':
            suits.append(i+j)
    return suits

def compare_card(card):
    """
    (card) -> int
    """
    rank = '23456789TJQKA'
    suits = []
    for i in rank:
        for j in 'CDHS':
            suits.append(i+j)
    return suits.index(card)

def hand_rank(hand):
    """
    (hand) -> int
    
    Return the hand rank of a hand

    >>> sf = ['JC','TC','9C','8C','7C']
    >>> hand_rank(sf)
    8
    >>> fk = ['5S','5H','5D','5C','KS']
    >>> hand_rank(fk)
    7
    """

    if straight_flush(hand):
        return 8
    elif four_of_a_kind(hand):
        return 7
    elif full_house(hand):
        return 6
    elif flush(hand):
        return 5
    elif straight(hand):
        return 4
    elif three_of_a_kind(hand):
        return 3
    elif two_pair(hand):
        return 3
    elif one_pair(hand):
        return 2
    elif high_card(hand):
        return 1
    else:
        return 0
def straight_flush(hand):
    """
    (hand) -> Bool

    Return True if hand is straight_flush,
    Flase otherwise

    >>> sf = ['JC','TC','9C','8C','7C']
    >>> straight_flush(sf)
    True
    >>> fk = ['5S','5H','5D','5C','KS']
    >>> straight_flush(fk)
    False
    """
    if straight(hand) and flush(hand):
        return True
    return False
    
def straight(hand):
    """
    (hand) -> Bool

    Return True if hand is straight,
    Flase otherwise

    >>> sf = ['JC','TC','9C','8C','7C']
    >>> straight(sf)
    True
    >>> fk = ['5S','5H','5D','5C','KS']
    >>> straight(fk)
    False
    """

    ranks_temp = []
    for card in hand:
        ranks_temp.append(card[0])
    rank = []
    for  i in ranks_temp:
        if i == 'T':
            rank.append(10)
        elif i == 'J':
            rank.append(11)
        elif i == 'Q':
            rank.append(12)
        elif i == 'K':
            rank.append(13)
        elif i == 'A':
            rank.append(14)
        else:
            rank.append(int(i))
    
    if max(rank)-min(rank) == 4 and len(set(rank)) == 5:
        return True
    return False
    
def flush(hand):
    """
    (hand) -> Bool

    Return True if hand is flush,
    Flase otherwise
    
    >>> sf = ['JC','TC','9C','8C','7C']
    >>> flush(sf)
    True
    >>> fk = ['5S','5H','5D','5C','KS']
    >>> flush(fk)
    False
    """
        
    #suits = []
    #for card in hand:
    #    suits.append(card[1])

    suits = [s for r,s in hand]

    if suits.count(suits[0]) == 5:
        return True
    return False

def four_of_a_kind(hand):
    """
    (hand) -> Bool

    Return True if hand is four_of_a_kind,
    Flase otherwise

    >>> sf = ['JC','TC','9C','8C','7C']
    >>> four_of_a_kind(sf)
    False
    >>> fk = ['5S','5H','5D','5C','KS']
    >>> four_of_a_kind(fk)
    True
    """
    suits = [r for r,s in hand]
    for card in suits:
        if suits.count(card) == 4:
            return True
    return False

def full_house(hand):
    """
    (hand) -> Bool

    Return True if hand is full_house,
    Flase otherwise

    >>> sf = ['JC','TC','9C','8C','7C']
    >>> full_house(sf)
    False
    >>> fk = ['5S','5H','5D','6C','6S']
    >>> full_house(fk)
    True
    """
    if three_of_a_kind(hand) and one_pair(hand):
        return True
    return False

def three_of_a_kind(hand):
    """
    (hand) -> Bool

    Return True if hand is three_of_a_kind,
    Flase otherwise

    >>> sf = ['JC','TC','9C','8C','7C']
    >>> three_of_a_kind(sf)
    False
    >>> fk = ['5S','5H','5D','6C','KS']
    >>> three_of_a_kind(fk)
    True
    """
    suits = [r for r,s in hand]
    for card in suits:
        if suits.count(card) == 3:
            return True
    return False

def two_pair(hand):
    """
    (hand) -> Bool

    Return True if hand is two_pair,
    Flase otherwise

    >>> sf = ['JC','TC','9C','8C','7C']
    >>> two_pair(sf)
    False
    >>> fk = ['5S','5H','2D','2C','KS']
    >>> two_pair(fk)
    True
    """
    suits = [r for r,s in hand]
    pair = {}
    for card in suits:
        if card in pair:
            pair[card] += 1
        else:
            pair[card] = 1
    if pair.values().count(2) == 2:
        return True
    return False

def one_pair(hand):
    """
    (hand) -> Bool

    Return True if hand is one_pair,
    Flase otherwise

    >>> sf = ['JC','TC','9C','8C','7C']
    >>> one_pair(sf)
    False
    >>> fk = ['5S','5H','3D','2C','KS']
    >>> one_pair(fk)
    True
    """
    suits = [r for r,s in hand]
    pair = {}
    for card in suits:
        if card in pair:
            pair[card] += 1
        else:
            pair[card] = 1
    if pair.values().count(2) == 1:
        return True
    return False

def high_card(hand):
    check_suits = gen_card()
    suits = gen_card()
    
import doctest
print doctest.testmod()
