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

if __name__ == '__main__':
    unittest.main(exit=False)