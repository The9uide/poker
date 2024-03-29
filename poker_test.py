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
		expected = 8.07
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
		sf = ['JC','TC','9C','8C','QC']
		actual = poker.hand_rank(sf)
		expected = 8.10
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
		expected = 7.03
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
		expected = 6.03
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
		expected = 2.0412
		self.assertEqual(actual,expected)

	def test_poker_example_19(self):
		fh = ['7S','QH','AD','6C','6S']
		actual = poker.one_pair(fh)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_20(self):
		tk = ['5S','5H','5D','6C','AS']
		actual = poker.hand_rank(tk)
		expected = 3.03
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
		expected = 3.0411
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

	def test_poker_example_26(self):
		fk = ['4S','4H','4D','4C','KS']
		actual = poker.three_of_a_kind(fk)
		expected = False
		self.assertEqual(actual,expected)

	def test_poker_example_27(self):
		tk = ['3S','3H','3D','4C','KS']
		actual = poker.three_of_a_kind(tk)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_28(self):
		tp = ['5S','5H','6D','6C','KS']
		actual = poker.three_of_a_kind(tp)
		expected = False
		self.assertEqual(actual,expected)

	def test_poker_example_29(self):
		op = ['AS','5H','TD','6C','6S']
		actual = poker.three_of_a_kind(op)
		expected = False
		self.assertEqual(actual,expected)

	def test_poker_example_30(self):
		tk = ['5S','5H','5D','6C','KS']
		actual = poker.three_of_a_kind(tk)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_31(self):
		tp = ['5S','5H','8D','8C','KS']
		actual = poker.two_pair(tp)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_32(self):
		tp = ['5S','5H','7D','7C','KS']
		actual = poker.two_pair(tp)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_33(self):
		tp = ['5S','5H','6D','6C','KS']
		actual = poker.two_pair(tp)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_34(self):
		op = ['5S','5H','7D','6C','KS']
		actual = poker.one_pair(op)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_35(self):
		tp = ['5S','5H','6D','6C','KS']
		actual = poker.one_pair(tp)
		expected = False
		self.assertEqual(actual,expected)

	def test_poker_example_36(self):
		tp = ['5S','4H','6D','6C','7S']
		actual = poker.one_pair(tp)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_37(self):
		hc = ['AS','5H','TD','6C','8S']
		ot = ['5S','5Y','3F','6C','KS']
		actual = poker.poker([hc,ot])
		expected = ['AS','5H','TD','6C','8S']
		self.assertEqual(actual, expected)

	def test_poker_example_38(self):
		hc = ['5S','4H','2D','9C','7S']
		actual = poker.check_card(hc)
		expected = False
		self.assertEqual(actual,expected)

	def test_poker_example_39(self):
		ot = ['5S','5Y','3F','6C','KS']
		actual = poker.check_card(ot)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_40(self):
		tk = ['6S','5H','5D','5C','KS']
		actual = poker.three_of_a_kind(tk)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_41(self):
		tk = ['6S','KH','5D','5C','5S']
		actual = poker.three_of_a_kind(tk)
		expected = True
		self.assertEqual(actual,expected)

	def test_poker_example_42(self):
		fk = ['KS','5H','5D','5C','5S']
		actual = poker.hand_rank(fk)
		expected = 7.03
		self.assertEqual(actual,expected)

	def test_poker_example_43(self):
		fk1 = ['KS','5H','5D','5C','5S']
		fk2 = ['KS','5H','5D','5C','5S']
		fk3 = ['KS','5H','5D','5C','5S']
		hc1 = ['5S','4H','2D','9C','7S']
		actual = poker.multi_winner([fk1,fk2,fk3,hc1])
		expected = [ ['KS','5H','5D','5C','5S'], ['KS','5H','5D','5C','5S'],['KS','5H','5D','5C','5S']]
		self.assertEqual(actual,expected)

	def test_poker_example_44(self):
		fk1 = ['KS','5H','5D','5C','5S']
		fk2 = ['KH','5H','5C','5C','5D']
		fk3 = ['KS','5H','5D','5C','5S']
		actual = poker.multi_winner([fk1,fk2,fk3])
		expected = [ ['KS','5H','5D','5C','5S'], ['KH','5H','5C','5C','5D'],['KS','5H','5D','5C','5S']]
		self.assertEqual(actual,expected)

	def test_poker_example_45(self):
		hc1 = ['5S','4H','2D','9C','7S']
		hc2 = ['5S','4H','2D','9C','7S']
		hc3 = ['5S','4H','2D','9C','7S']
		actual = poker.multi_winner([hc1,hc2,hc3])
		expected = [ ['5S','4H','2D','9C','7S'], ['5S','4H','2D','9C','7S'], ['5S','4H','2D','9C','7S']]
		self.assertEqual(actual,expected)

	def test_poker_example_46(self):
		hc1 = ['5S','4H','2D','9C','7S']
		hc2 = ['5S','4H','2D','9C','8S']
		hc3 = ['5S','8H','2D','9C','7S']
		ot1 = ['5S','5Y','3F','6C','KS']
		actual = poker.multi_winner([hc1,hc2,hc3,ot1])
		expected = [ ['5S','4H','2D','9C','7S'], ['5S','4H','2D','9C','8S'], ['5S','8H','2D','9C','7S']]
		self.assertEqual(actual,expected)

	def test_poker_example_47(self):
		hc1 = ['5S','4H','2D','TC','7S']
		hc2 = ['5S','4H','2D','9C','8S']
		hc3 = ['5S','8H','2D','9C','7S']
		ot1 = ['5S','5Y','3F','6C','KS']
		actual = poker.multi_winner([hc1,hc2,hc3,ot1])
		expected = [['5S','4H','2D','TC','7S']]
		self.assertEqual(actual,expected)

	def test_poker_example_48(self):
		fk1 = ['AS','5H','5D','5C','5S']
		fk2 = ['QS','4H','4D','4C','4S']
		fk3 = ['JS','3H','3D','3C','3S']
		actual = poker.multi_winner([fk1,fk2,fk3])
		expected = [['AS','5H','5D','5C','5S']]
		self.assertEqual(actual,expected)

	def test_poker_example_49(self):
		fk = ['AS','5H','5D','5C','5S']
		actual = poker.compare_card(fk)
		expected = [0.12,0.03,0.03,0.03,0.03]
		self.assertEqual(actual,expected)

	def test_poker_example_50(self):
		sf = ['2C','3C','4C','5C','6C']
		actual = poker.compare_card(sf)
		expected = [0.0,0.01,0.02,0.03,0.04]
		self.assertEqual(actual,expected)

	def test_poker_example_51(self):
		sf1 = ['5C','6C','9C','8C','7C']
		sf2 = ['TC','6C','9C','8C','7C']
		fk1 = ['5S','5H','5D','5C','AS']
		fk2 = ['5S','5H','5D','5C','KS']
		actual = poker.multi_winner([sf1,sf2,fk1,fk2])
		expected = [['TC','6C','9C','8C','7C']]
		self.assertEqual(actual, expected)
	
	def test_poker_example_52(self):
		sf1 = ['TC','JC','QC','KC','AC']
		sf2 = ['TS','JS','QS','KS','AS']
		sf3 = ['TD','JD','QD','KD','AD']
		actual = poker.multi_winner([sf1,sf2,sf3])
		expected = [['TC','JC','QC','KC','AC'],['TS','JS','QS','KS','AS'],['TD','JD','QD','KD','AD']]
		self.assertEqual(actual,expected)

	def test_poker_example_53(self):
		sf1 = ['TC','6C','9C','8C','7C']
		sf2 = ['6S','TS','9S','8S','7S']
		actual = poker.multi_winner([sf1,sf2])
		expected = [['TC','6C','9C','8C','7C'],['6S','TS','9S','8S','7S']]
		self.assertEqual(actual,expected)

	def test_poker_example_54(self):
		sf1 = ['TC','6C','9C','8C','7C']
		sf2 = ['6S','TS','9S','8S','7S']
		sf3 = ['JD','TD','9D','8D','QD']
		actual = poker.multi_winner([sf1,sf2,sf3])
		expected = [['JD','TD','9D','8D','QD']]
		self.assertEqual(actual,expected)

	def test_poker_example_55(self):
		sf1 = ['5C','6C','9C','8C','7C']
		sf2 = ['6S','TS','9S','8S','7S']
		fk1 = ['5S','5H'',5D','5C','KS']
		fk2 = ['6S','6H','6D','6C','QS']
		actual = poker.multi_winner([sf1,sf2,fk1,fk2])
		expected = [['6S','TS','9S','8S','7S']]
		self.assertEqual(actual,expected)

	def test_poker_example_56(self):
		fh1 = ['6S','6H','6D','3C','3S']
		fh2 = ['5S','5H','5D','7C','7S']
		actual = poker.multi_winner([fh1,fh2])
		expected = [['6S','6H','6D','3C','3S']]
		self.assertEqual(actual,expected)

	def test_poker_example_57(self):
		fh = ['5S','5H','5D','7C','7S']
		actual = poker.max_three_of_a_kind(fh)
		expected = ['5H']
		self.assertEqual(actual,expected)

	def test_poker_example_58(self):
		fk1 = ['KS','JH','JD','JC','JS']
		fk2 = ['QS','QH','QD','QC','2S']
		tk1 = ['6S','KH','5D','5C','5S']
		actual = poker.multi_winner([fk1,fk2,tk1])
		expected = [['QS','QH','QD','QC','2S']]
		self.assertEqual(actual,expected)

	def test_poker_example_59(self):
		fk1 = ['KS','JH','JD','JC','JS']
		actual = poker.max_four_of_a_kind(fk1)
		expected = ['JH']
		self.assertEqual(actual,expected)

	def test_poker_example_60(self):
		tk1 = ['6S','KH','5D','5C','5S']
		tk2 = ['4S','AH','4D','4C','5S']
		op = ['5S','5H','7D','6C','KS']
		actual = poker.multi_winner([tk1,tk2,op])
		expected = [['6S','KH','5D','5C','5S']]
		self.assertEqual(actual,expected)

	def test_poker_example_61(self):
		tk1 = ['6S','KH','5D','5C','5S']
		actual = poker.max_three_of_a_kind(tk1)
		expected = ['5H']
		self.assertEqual(actual,expected)

	def test_poker_example_62(self):
		tp1 = ['5S','5H','6D','6C','AS']
		tp2 = ['7S','7H','6S','6H','8S']
		op = ['5S','5H','7D','6C','KS']
		actual = poker.multi_winner([tp1,tp2,op])
		expected = [['7S','7H','6S','6H','8S']]
		self.assertEqual(actual,expected)

	def test_poker_example_63(self):
		tp1 = ['7S','7H','6S','6H','8S']
		actual = poker.max_two_pair(tp1)
		expected = ['7H','6H']
		self.assertEqual(actual,expected)

	def test_poker_example_64(self):
		tp1 = ['5S','5H','6D','6C','AS']
		tp2 = ['5S','5H','6S','6H','8S']
		op = ['5S','5H','7D','6C','KS']
		actual = poker.multi_winner([tp1,tp2,op])
		expected = [['5S','5H','6D','6C','AS']]
		self.assertEqual(actual,expected)

	def test_poker_example_65(self):
		tp1 = ['7S','7H','6S','6H','8S']
		actual = poker.max_two_pair(tp1,True)
		expected = ['8H']
		self.assertEqual(actual,expected)

	def test_poker_example_66(self):
		op1 = ['AS','AH','6D','9C','5S']
		op2 = ['3S','6H','AS','AD','KS']
		hc = ['5S','2H','7D','6C','KS']
		actual = poker.multi_winner([op1,op2,hc])
		expected = [['3S','6H','AS','AD','KS']]
		self.assertEqual(actual,expected)

	def test_poker_example_67(self):
		op1 = ['3S','2H','6D','6C','AS']
		op2 = ['3S','6H','6S','2D','8S']
		hc = ['5S','2H','7D','6C','KS']
		actual = poker.multi_winner([op1,op2,hc])
		expected = [['3S','2H','6D','6C','AS']]
		self.assertEqual(actual,expected)

if __name__ == '__main__':
	unittest.main(exit=False)
