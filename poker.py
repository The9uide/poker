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


