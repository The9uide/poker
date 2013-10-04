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
	else:
		return 0

def straight_flush(hand):
	"""
		(hand) -> bool
	Return True if hand is straight_flush,Flase otherwise 
	"""
	if straight(hand) and flush(hand):
		return True
	return False

def straight(hand):
	"""
		(hand) -> Bool
	Return True if hand is straight,Flase otherwise
	"""
	suits = [r for r,s in hand]
	suits.sort()
	suit = "".join(suits)
	print suit,"+++++++"
	if suit in "1234A123456789TJQKA":
		return True
	return False

def flush(hand):
	"""
		(hand) -> bool
	Return True if hand is flush,Flase otherwise 
	"""
	suits = [s for r,s in hand]
	if suits.count(suits[0]) == 5:
		return True
	return False




