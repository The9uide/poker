def poker(hands):
	"""
		([hand, hand, habd, ...])->hand
	Return the best hand from list of hand
	"""
	return max(hands, key=hand_rank)

def hand_rank(hand):
	"""
		(hand) -> int
	Return rank of hand
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
	else:
		return 0

def straight_flush(hand):
	"""
		(hand) -> bool
	Return True if hand is straight_flush,Flase otherwise 
	"""
	return straight(hand) and flush(hand)
		

def straight(hand):
	"""
		(hand) -> Bool
	Return True if hand is straight,Flase otherwise
	"""
	suits = [r for r,s in hand]
	suits.sort()
	suit = "".join(suits)
	if suit in "2345A123456789T789JT89JQT9JKQTAJKQT":return True

	return False

def flush(hand):
	"""
		(hand) -> bool
	Return True if hand is flush,Flase otherwise 
	"""
	suits = [s for r,s in hand]
	if suits.count(suits[0]) == 5:return True
	return False

def four_of_a_kind(hand):
	"""
		(hand) -> Bool
	Return True if hand is four_of_a_kind,Flase otherwise
	"""
	suits = [r for r,s in hand]
	for card in suits:
		if suits.count(card) == 4:return True
	return False

def full_house(hand):
	"""
		(hand) -> Bool
	Return True if hand is full_house,Flase otherwise
	"""
	return three_of_a_kind(hand) and one_pair(hand)

def three_of_a_kind(hand):
	"""
	(hand) -> Bool
	Return True if hand is three_of_a_kind,Flase otherwise
	"""
	suits = [r for r,s in hand]
	for card in suits:
		if suits.count(card) == 3:return True
	return False

def one_pair(hand):
	"""
		(hand) -> Bool
	Return True if hand is one_pair,Flase otherwise
	"""
	suits = [r for r,s in hand]
	pair = {}
	for card in suits:
		if card in pair:pair[card] += 1
		else:
			pair[card] = 1
	if pair.values().count(2) == 1:return True
	return False

def two_pair(hand):
	"""
		(hand) -> Bool
	Return True if hand is two_pair,Flase otherwise
	"""
	suits = [r for r,s in hand]
	pair = {}
	for card in suits:
		if card in pair :pair[card] += 1
		else:
			pair[card] = 1
	if pair.values().count(2) == 2:return True
	return False
