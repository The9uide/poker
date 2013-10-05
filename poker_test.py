import unittest
import poker

class TestPoker(unittest.TestCase):
	'''Example unittest test methods for poker'''

	def test_poker_example_1(self):
		sf = ['5C','6C','9C','8C','7C']
		fk = ['5S','5H','5D','5C','KS']
		actual = poker.poker([sf,fk])
		expected = ['5C','6C','9C','8C','7C']
		self.assertEqual(actual, expected)
	
	def test_poker_example_2(self):
		sf = ['6C','5C','9C','8C','7C']
		actual = poker.hand_rank(sf)
		expected = 8
		self.assertEqual(actual, expected)

	def test_poker_example_3(self):
		sf = ['6C','5C','9C','8C','7C']
		actual = poker.straight(sf)
		expected = True
		self.assertEqual(actual, expected)

	def test_poker_example_4(self):
		sf = ['6C','5C','9C','8C','7C']
		actual = poker.flush(sf)
		expected = True
		self.assertEqual(actual, expected)
	
	def test_poker_example_5(self):
		sf = ['JC','TC','9C','8C','QC']
		fk = ['5S','5H','5D','5C','KS']
		actual = poker.poker([sf,fk])
		expected = ['JC','TC','9C','8C','QC']
		self.assertEqual(actual, expected)

	def test_poker_example_6(self):
		sf = ['JC','TC','9C','8C','7C']
		actual = poker.hand_rank(sf)
		expected = 8
		self.assertEqual(actual, expected)
	
	def test_poker_example_7(self):
		sf = ['JC','TC','9C','KC','QC']
		actual = poker.straight(sf)
		expected = True
		self.assertEqual(actual, expected)
	
	def test_poker_example_8(self):
		sf = ['JC','TC','AC','KC','QC']
		actual = poker.straight(sf)
		expected = True
		self.assertEqual(actual, expected)

	def test_poker_example_9(self):
		sf = ['6C','TC','9C','8C','7C']
		actual = poker.straight(sf)
		expected = True
		self.assertEqual(actual, expected)
	
	def test_poker_example_10(self):
		sf = ['AC','2C','3C','4C','5C']
 		actual = poker.straight(sf)
		expected = True
		self.assertEqual(actual,expected)
	
	def test_poker_example_11(self):
		fk = ['5S','5H','5D','5C','KS']
		fh = ['5S','5H','5D','6C','6S']
		actual = poker.poker([fk,fh])
		expected = ['5S','5H','5D','5C','KS']
		self.assertEqual(actual, expected)

	def test_poker_example_12(self):
		fk = ['2H','2C','2D','2S','5C']
		actual = poker.four_of_a_kind(fk)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_13(self):
		fk = ['5S','5H','5D','5C','KS']
		actual = poker.hand_rank(fk)
		expected = 7
		self.assertEqual(actual,expected)

	def test_poker_example_14(self):
		fh = ['5S','5H','5D','6C','6S']
		tk = ['5S','5H','5D','6C','AS']
		actual = poker.poker([fh,tk])
		expected = ['5S','5H','5D','6C','6S']
		self.assertEqual(actual, expected)

	def test_poker_example_15(self):
		fh = ['5S','5H','5D','6C','6S']
		actual = poker.hand_rank(fh)
		expected = 6
		self.assertEqual(actual,expected)

	def test_poker_example_16(self):
		sf = ['JC','TC','9C','8C','7C']
		actual = poker.full_house(sf)
		expected = False
		self.assertEqual(actual,expected)

	def test_poker_example_17(self):
		fh = ['5S','5H','5D','6C','6S']
		actual = poker.full_house(fh)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_18(self):
		op = ['AS','5H','TD','6C','6S']
		actual = poker.hand_rank(op)
		expected = 2
		self.assertEqual(actual,expected)

	def test_poker_example_19(self):
		fh = ['7S','QH','AD','6C','6S']
		actual = poker.one_pair(fh)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_20(self):
		tk = ['5S','5H','5D','6C','AS']
		actual = poker.hand_rank(tk)
		expected = 3
		self.assertEqual(actual,expected)

	def test_poker_example_21(self):
		fk = ['5S','5H','5D','5C','KS']
		actual = poker.three_of_a_kind(fk)
		expected = False
		self.assertEqual(actual,expected)

	def test_poker_example_22(self):
		op = ['AS','5H','TD','6C','6S']
		tp = ['5S','5H','6D','6C','KS']
		actual = poker.poker([tp,op])
		expected = ['5S','5H','6D','6C','KS']
		self.assertEqual(actual, expected)

	def test_poker_example_23(self):
		tp = ['5S','5H','6D','6C','KS']
		actual = poker.hand_rank(tp)
		expected = 3
		self.assertEqual(actual,expected)

	def test_poker_example_24(self):
		fk = ['5S','5H','5D','5C','KS']
		actual = poker.two_pair(fk)
		expected = False
		self.assertEqual(actual,expected)

	def test_poker_example_25(self):
		tp = ['5S','5H','6D','6C','KS']
		actual = poker.two_pair(tp)
		expected = True
		self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main(exit=False)
