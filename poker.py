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
	if check_card(hand):
		return 0
	elif straight_flush(hand):
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
		return 1

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
	return suit in "2345A123456789T789JT89JQT9JKQTAJKQT"

def flush(hand):
	"""
		(hand) -> bool
	Return True if hand is flush,Flase otherwise 
	"""
	suits = [s for r,s in hand]
	return suits.count(suits[0]) == 5

def four_of_a_kind(hand):
	"""
		(hand) -> Bool
	Return True if hand is four_of_a_kind,Flase otherwise
	"""
	suits = [r for r,s in hand]
	return suits.count(suits[0]) == 4 or suits.count(suits[1]) == 4 

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
	return suits.count(suits[0]) == 3 or suits.count(suits[1]) == 3 or suits.count(suits[2]) == 3

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
	return pair.values().count(2) == 1

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
	return pair.values().count(2) == 2

def check_card(hand):
	"""
		(hand) -> Bool
	Return True if card in hand is in gen_card,Flase otherwise
	"""	
	really = False
	for card in hand:
		if not card in gen_card():
			really = True
	return really
	
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

