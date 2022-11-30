# Based on testing harness dated 2017-06-02.

# STUDENTS: TO USE:
#
# The following command will test all test cases on your file:
#
#   python3 <thisfile.py> <your_one_file.py>
#
#
# You can also limit the tester to only the functions you want tested.
# Just add as many functions as you want tested on to the command line at the end.
# Example: to only run tests associated with func1 and func2, run this command:
#
#   python3 <thisfile.py> <your_one_file.py> func1 func2
#
# You really don't need to read the file any further, except that when
# a specific test fails, you'll get a line number - and it's certainly
# worth looking at those areas for details on what's being checked. This would
# all be the indented block of code starting with "class AllTests".


# INSTRUCTOR: TO PREPARE:
#  - add test cases to class AllTests. The test case functions' names must
# be precise - to test a function named foobar, the test must be named "test_foobar_#"
# where # may be any digits at the end, such as "test_foobar_13".
# - any extra-credit tests must be named "test_extra_credit_foobar_#"
#
# - name all required definitions in REQUIRED_DEFNS, and all extra credit functions
#   in EXTRA_CREDIT_DEFNS. Do not include any unofficial helper functions. If you want
#   to make helper definitions to use while testing, those can also be added there for
#   clarity.
#
# - to run on either a single file or all .py files in a folder (recursively):
#   python3 <thisfile.py> <your_one_file.py>
#   python3 <thisfile.py> <dir_of_files>
#   python3 <thisfile.py> .                    # current directory
#
# A work in progress by Mark Snyder, Oct. 2015.
#  Edited by Yutao Zhong, Spring 2016.
#  Edited by Raven Russell, Spring 2017.
#  Edited by Mark Snyder, June 2017.


import unittest
import shutil
import sys
import os
import time

############################################################################
############################################################################
# BEGIN SPECIALIZATION SECTION (the only part you need to modify beyond
# adding new test cases).

# name all expected definitions; if present, their definition (with correct
# number of arguments) will be used; if not, a decoy complainer function
# will be used, and all tests on that function should fail.

REQUIRED_DEFNS = ['squarify','expand','mashup','apply']

# add weight property to function
# experimental feature
class weight(object):
	def __init__(self, val):
		self.val = val
	def __call__(self, func):
		func.__weight__ = self.val
		return func

# for method names in classes that will be tested
SUB_DEFNS = []

# definitions that are used for extra credit
EXTRA_CREDIT_DEFNS = []

# how many points are test cases worth?
weight_required = 1
weight_extra_credit = 0

# don't count extra credit; usually 100% if this is graded entirely by tests.
# it's up to you the instructor to do the math and add this up!
# TODO: auto-calculate this based on all possible tests.
total_points_from_tests = 54

# how many seconds to wait between batch-mode gradings?
# ideally we could enforce python to wait to open or import
# files when the system is ready but we've got a communication
# gap going on.
DELAY_OF_SHAME = 1


# set it to true when you run batch mode...
CURRENTLY_GRADING = False



# what temporary file name should be used for the student?
# This can't be changed without hardcoding imports below, sorry.
# That's kind of the whole gimmick here that lets us import from
# the command-line argument without having to qualify the names.
RENAMED_FILE = "student"

# END SPECIALIZATION SECTION
############################################################################
############################################################################


# enter batch mode by giving a directory to work on as the only argument.
BATCH_MODE = len(sys.argv)==2 and (sys.argv[1] in ["."] or os.path.isdir(sys.argv[1]))

# This class contains multiple "unit tests" that each check
# various inputs to specific functions, checking that we get
# the correct behavior (output value) from completing the call.
class AllTests (unittest.TestCase):

	############################################################################

	#mashup tests

	def test_mashup_1(self):
		'''mashup([2, 'abc', 1, 'def']) == 'abd' '''
		self.assertEqual(mashup([2, 'abc', 1, 'def']), 'abd')

	def test_mashup_2(self):
		'''mashup([3, 'rate', 2, 'inside', 1, 'goat']) == 'rating' '''
		self.assertEqual(mashup([3, 'rate', 2, 'inside', 1, 'goat']), 'rating')

	def test_mashup_3(self):
		'''mashup([1,'aaa',2, 'aaa',3,'aaa',4,'aaaaa']) == 'aaaaaaaaaa' '''
		self.assertEqual(mashup([1,'aaa',2, 'aaa',3,'aaa',4,'aaaaa']), 'aaaaaaaaaa')

	def test_mashup_4(self):
		'''mashup([]) == 'aababc' '''
		self.assertEqual(mashup([0,'abc',1,'abc',2,'abc',3,'abc']), 'aababc')

	def test_mashup_5(self):
		'''mashup([3, '', 1, 'QHnwq', 5, 'UgJoSwnkq']) == 'QUgJoS' '''
		self.assertEqual(mashup([3, '', 1, 'QHnwq', 5, 'UgJoSwnkq']), 'QUgJoS')

	def test_mashup_6(self):
		'''mashup([2, 'SPKhVb', 1, 'RZ', 7, 'IKMJTEkR']) == 'SPIKMJTEk' '''
		self.assertEqual(mashup([2, 'SPKhVb', -1, 'RZ', 7, 'IKMJTEkR']), 'SPIKMJTEk')

	def test_mashup_7(self):
		'''mashup([1, 'iOR', 1, 'tX']) == 'it' '''
		self.assertEqual(mashup([1, 'iOR', 1, 'tX']), 'it')

	def test_mashup_8(self):
		'''mashup([5, 'rHEmMWqcy', 3, 'hJvx', 2, 'CTH']) == 'rHEmMhJvCT' '''
		self.assertEqual(mashup([5, 'rHEmMWqcy', 3, 'hJvx', 2, 'CTH']), 'rHEmMhJvCT')

	def test_mashup_9(self):
		'''inspect the tester file to view this test'''
		self.assertEqual(mashup([6, 'fHTVcnMJw', 5, 'XAnRlDhXnLq', 5, 'tjolhA', 6, 'ZXBWMQhkKpnwTU', 9, 'XXLLslGpbOmr', 9, 'nFNpojwLCS']), 'fHTVcnXAnRltjolhZXBWMQXXLLslGpbnFNpojwLC')

	def test_mashup_10(self):
		'''inspect the tester file to view this test'''
		self.assertEqual(mashup([9, 'LoptSlAFuDnUT', 8, 'EhzbtHQNgSWlZ', 5, 'qMLNKkNDfJOazE', 13, 'fYDiJmVXpMEuTsq', 12, 'YJdcjbeiqnbRwC', 0, 'CwiWFjV']), 'LoptSlAFuEhzbtHQNqMLNKfYDiJmVXpMEuTYJdcjbeiqnbR')

	def test_mashup_11(self):
		'''inspect the tester file to view this test'''
		self.assertEqual(mashup([6, 'cVrZQBl', 8, 'hubCXYhnU', 5, 'VmYWdvIjc', 8, 'XgqoLwuuWnxYR', 5, 'ZYmyfImXjGAw', 6, 'CKwOYLdiERPIZ']), 'cVrZQBhubCXYhnVmYWdXgqoLwuuZYmyfCKwOYL')

	def test_mashup_12(self):
		'''inspect the tester file to view this test'''
		self.assertEqual(mashup([7, 'EzioGXYNEP', 10, 'XlVnxIXzbH', 8, 'bNJejipOdmaKf', 12, 'zfLsZRyiehVlGD', 14, 'dIHktAnxErYpSQ', 10, 'beSBNigIRJyHU']), 'EzioGXYXlVnxIXzbHbNJejipOzfLsZRyiehVldIHktAnxErYpSQbeSBNigIRJ')

	def test_mashup_13(self):
		'''inspect the tester file to view this test'''
		self.assertEqual(mashup([11, 'FLUYYDBwQiFjNL', 8, 'QASamZhFGzOzL', 6, 'ZSKzYWfEFEk', 11, 'uwxqNjLYIrc', 10, 'hdzEPlUjIoBgyu', 10, 'wfhkHTKbumS']), 'FLUYYDBwQiFQASamZhFZSKzYWuwxqNjLYIrchdzEPlUjIowfhkHTKbum')

	def test_mashup_14(self):
		'''inspect the tester file to view this test'''
		self.assertEqual(mashup([12, 'ATgqpyuCXNhWk', 14, 'wuNpVTwUFszJBZC', 8, 'jPaNDWdoYNgJ', 8, 'VilEVZYUHNfQb', 13, 'YRCDtSOThacxUr', 8, 'FrgMrJUnKu']), 'ATgqpyuCXNhWwuNpVTwUFszJBZjPaNDWdoVilEVZYUYRCDtSOThacxUFrgMrJUn')

	def test_mashup_15(self):
		'''inspect the tester file to view this test'''
		self.assertEqual(mashup([8, 'cYoEmXSwnseHU', 11, 'eoLbtlDZqKpy', 10, 'OoTiAZDswnx', 10, 'ZPfUNBuytKtkBcR', 25, 'bJoWBSOhuNQwZEe', 6, 'KNSdDEbMWjU']), 'cYoEmXSweoLbtlDZqKpOoTiAZDswnZPfUNBuytKKNSdDE')

	def test_mashup_16(self):
		'''inspect the tester file to view this test'''
		self.assertEqual(mashup([11, 'WTwGtMSEqJyFL', 17, 'cKWPDmGJsYX', 11, 'afnkGDHqFpv', 13, 'bmsdNrKqHPJFThU', 12, 'kYcCSuzrMTDi', 6, 'GlytQBbcahT']), 'WTwGtMSEqJyafnkGDHqFpvbmsdNrKqHPJFTkYcCSuzrMTDiGlytQB')
	
	# expand tests
	def test_expand_1(self):
		'''expand([1], 1) changes list to [0,1,0]'''
		ls = [1]
		res = expand(ls, 1)
		self.assertEqual(res, None, 'you should not return anything')
		self.assertEqual(ls, [0,1,0])

	def test_expand_2(self):
		'''expand([1,2,3], 1) changes list to [0,1,0,2,0,3,0]'''
		ls = [1,2,3]
		res = expand(ls, 1)
		self.assertEqual(res, None, 'you should not return anything')
		self.assertEqual(ls, [0,1,0,2,0,3,0])

	def test_expand_3(self):
		'''expand([1.876,2.234], 2) changes list to [0,0,1.876,0,0,2.234,0,0]'''
		ls = [1.876,2.234]
		expand(ls, 2)
		self.assertEqual(ls,[0,0,1.876,0,0,2.234,0,0])

	def test_expand_4(self):
		'''expand([0,1,2], 3) changes list to [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0]'''
		ls = list(range(3))
		expand(ls, 3)
		self.assertEqual(ls,[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0])

	def test_expand_5(self):
		ls = list(range(1,8,2))
		expand(ls, 0)
		self.assertEqual(ls,[1,3,5,7])
	
	def test_expand_6(self):
		ls = list(range(-10,10,3))
		expand(ls, 4)
		self.assertEqual(ls,[0, 0, 0, 0, -10, 0, 0, 0, 0, -7, 0, 0, 0, 0, -4, 0, 0, 0, 0, -1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 5, 0, 0, 0, 0, 8, 0, 0, 0, 0])

	def test_expand_7(self):
		ls = [5,2,8,6,3,9,6,6,6,3,2,1]
		expand(ls, 5)
		self.assertEqual(ls,[0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])

	def test_expand_8(self):
		ls = [-6,-9,5,5,0,1]
		expand(ls, 10)
		self.assertEqual(ls,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	
	def test_expand_9(self):
		ls = [1]
		expand(ls, 100)
		self.assertEqual(ls,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

	#squarify tests

	def deepAssertListIsNot(self, a, b):
			"""tests to ensure that two 2D lists (a, b) are in different memory locations"""
			
			self.assertIsNot(a, b, msg="The outer lists are aliases for the same memory location. "
									"Run your code in the visualizer to understand why.")

			# make sure every row in the copy is different from every row in the original
			for elementA in a:
				for elementB in b:
					self.assertIsNot(elementA, elementB, msg="One or more of the inner lists in "
															"the copy is an alias for one of the original inner lists!"
															" Run your code in the visualizer to understand why.")

	def test_squarify_1(self):
		ls = [[1]]
		new_ls = squarify(ls)
		self.assertEqual(new_ls, [[1]])
		self.deepAssertListIsNot(ls, new_ls)

	def test_squarify_3(self):
		ls = [[1,2,3],[4,5,6]]
		new_ls = squarify(ls)
		self.assertEqual(new_ls, [[1,2],[4,5]])

	def test_squarify_4(self):
		ls = [[1,2],[3,4],[5,6]]
		new_ls = squarify(ls)
		self.assertEqual(new_ls, [[1,2],[3,4]])

	def test_squarify_5(self):
		ls = [[1,2,3],[4,5,6],[7,8,9]]
		new_ls = squarify(ls)
		self.assertEqual(new_ls, [[1,2,3],[4,5,6],[7,8,9]])

	def test_squarify_6(self):
		ls = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
		new_ls = squarify(ls)
		self.assertEqual(new_ls, [[0,0,0],[0,0,0],[0,0,0]])

	def test_squarify_7(self):
		ls = [[-3,6,3,7,9,10,1,1,2], [7,8,9,11,2,-4,5,6,7],[-4,2,0,15,-8,5,4,4,7],[9,5,-3,4,12,-10,-3,9,7]]
		new_ls = squarify(ls)
		self.assertEqual(new_ls, [[-3, 6, 3, 7], [7, 8, 9, 11], [-4, 2, 0, 15], [9, 5, -3, 4]])

	def test_squarify_8(self):
		ls = [[18, -11, 17, 20, -5, -3, -9, 20, 20, 17], [-5, 12, 8, 20, -3, -9, 7, -17, 5, 0], [-19, -3, -9, -5, -16, -10, 2, -6, -16, 11], [-11, 3, -14, 7, -8, 6, -14, 5, -10, 18], [2, -18, 9, 20, -18, -19, 6, 3, 17, 1]]
		new_ls = squarify(ls)
		self.assertEqual(new_ls, [[18, -11, 17, 20, -5], [-5, 12, 8, 20, -3], [-19, -3, -9, -5, -16], [-11, 3, -14, 7, -8], [2, -18, 9, 20, -18]])

	def test_squarify_9(self):
		ls = [[-32, -43, 45, -29, -41], [39, 2, -23, 47, 43], [42, 29, -1, -43, 25], [40, 13, -28, -19, -27], [-14, 29, -6, 20, -19], [-29, 14, -3, 47, 48], [-38, -26, 22, 41, 29], [28, -30, -41, -50, -47], [-30, 39, -48, 18, 15], [-24, -49, 38, -11, 29], [38, -31, -40, 13, -21], [-7, -49, -14, 31, -24], [-26, -24, -19, -31, 26], [-41, -34, 14, -48, 10], [-45, -43, -16, 27, -47]]
		new_ls = squarify(ls)
		self.assertEqual(new_ls, [[-32, -43, 45, -29, -41], [39, 2, -23, 47, 43], [42, 29, -1, -43, 25], [40, 13, -28, -19, -27], [-14, 29, -6, 20, -19]])

	def test_squarify_10(self):
		ls = [[38, 32, -6, -42, 34, 35, -9, -42, 18, 48], [-18, -47, 37, 47, 50, 6, -22, -7, 47, -43], [-23, 19, 31, -11, -6, 2, -43, -13, 4, 19], [16, 40, 16, 44, 25, 50, -37, -46, -8, 45], [-50, 29, 13, 44, -46, 14, -28, -14, -30, 27], [21, -22, -11, -35, -12, 5, 33, -17, 11, 3], [-4, -9, 28, 11, 37, 2, 43, -47, -2, -15], [45, 24, 43, -42, -46, -39, 8, -24, -37, 16], [-39, -21, -25, 40, -37, -26, 27, -35, 14, 4], [48, -46, -33, 43, -44, 18, -5, -5, -44, 20]]
		new_ls = squarify(ls)
		self.assertEqual(new_ls, ls)

	# apply tests
	def test_apply_1(self):
		test_ls = [[1]]
		test_mask = [[1,1],[1,1]]
		res = apply(test_mask, test_ls)
		self.assertEqual(res, None, "your function should make in place changes; it should have no return value")
		self.assertEqual(test_ls, [[2]])

	def test_apply_3(self):
		test_ls =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		test_mask = [[1,1],[1,1]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[2, 3, 4], [5, 6, 7], [8, 9, 10]])

	def test_apply_4(self):
		test_ls =   [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
		test_mask = [[1,0],[0,1]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[2, 2, 4], [4, 6, 6], [8, 8, 10], [10, 12, 12]])

	def test_apply_5(self):
		test_ls =   [[5, -2, -2, -1], [-2, -4, 0, -2]]
		test_mask = [[1,2],[3,4]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[6, 0, -1, 1], [1, 0, 3, 2]])

	def test_apply_6(self):
		test_ls =   [[5, -2, -2, -1], [-2, -4, 0, -2]]
		test_mask = [[-1,-2],[-3,-4]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[4, -4, -3, -3], [-5, -8, -3, -6]])

	def test_apply_7(self):
		test_ls =   [[-5, 1, 3, 2], [-2, 3, -4, 4], [4, 1, 2, 3], [1, 3, 3, 0]]
		test_mask = [[5,5],[0,0]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[0, 6, 8, 7], [-2, 3, -4, 4], [9, 6, 7, 8], [1, 3, 3, 0]])

	def test_apply_8(self):
		test_ls =   [[-5, 1, 3, 2], [-2, 3, -4, 4], [4, 1, 2, 3], [1, 3, 3, 0]]
		test_mask = [[0,0],[4,4]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[-5, 1, 3, 2], [2, 7, 0, 8], [4, 1, 2, 3], [5, 7, 7, 4]])

	def test_apply_9(self):
		test_ls =   [[-5, 1, 3, 2], [-2, 3, -4, 4], [4, 1, 2, 3], [1, 3, 3, 0]]
		test_mask = [[1,2],[1,2]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[-4, 3, 4, 4], [-1, 5, -3, 6], [5, 3, 3, 5], [2, 5, 4, 2]])

	def test_apply_10(self):
		test_ls =   [[-3, 2, 5, 5], [-2, 4, 3, -2], [0, 1, 1, -3], [5, 2, 5, 0], [-5, -1, 3, -4]]
		test_mask = [[0,1],[-1,0]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[-3, 3, 5, 6], [-3, 4, 2, -2], [0, 2, 1, -2], [4, 2, 4, 0], [-5, 0, 3, -3]])

	def test_apply_11(self):
		test_ls =   [[-3, 2, 5, 5], [-2, 4, 3, -2], [0, 1, 1, -3], [5, 2, 5, 0], [-5, -1, 3, -4]]
		test_mask = [[-5,10],[10,-5]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[-8, 12, 0, 15], [8, -1, 13, -7], [-5, 11, -4, 7], [15, -3, 15, -5], [-10, 9, -2, 6]])

	def test_apply_12(self):
		test_ls =   [[3, -2, 5, 0, -2], [3, 4, 3, -4, -2], [4, -4, 2, -5, -5], [5, 1, 0, 4, -5]]
		test_mask = [[6,5],[4,3]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[9, 3, 11, 5, 4], [7, 7, 7, -1, 2], [10, 1, 8, 0, 1], [9, 4, 4, 7, -1]])

	def test_apply_13(self):
		test_ls =   [[3, -2, 5, 0, -2], [3, 4, 3, -4, -2], [4, -4, 2, -5, -5], [5, 1, 0, 4, -5]]
		test_mask = [[-1,-1],[-1,-1]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[2, -3, 4, -1, -3], [2, 3, 2, -5, -3], [3, -5, 1, -6, -6], [4, 0, -1, 3, -6]])

	def test_apply_14(self):
		test_ls =   [[2, 5, -8, 2, -8], [-2, 10, -7, 7, 4], [-10, 7, 6, 2, 0], [8, 9, 4, 1, 0], [4, -1, -7, -7, 10]]
		test_mask = [[7,7],[-7,-7]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[9, 12, -1, 9, -1], [-9, 3, -14, 0, -3], [-3, 14, 13, 9, 7], [1, 2, -3, -6, -7], [11, 6, 0, 0, 17]])

	def test_apply_15(self):
		test_ls =   [[2, 5, -8, 2, -8], [-2, 10, -7, 7, 4], [-10, 7, 6, 2, 0], [8, 9, 4, 1, 0], [4, -1, -7, -7, 10]]
		test_mask = [[5,0],[0,-5]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[7, 5, -3, 2, -3], [-2, 5, -7, 2, 4], [-5, 7, 11, 2, 5], [8, 4, 4, -4, 0], [9, -1, -2, -7, 15]])

	def test_apply_16(self):
		test_ls =   [[2, 5, -8, 2, -8], [-2, 10, -7, 7, 4], [-10, 7, 6, 2, 0], [8, 9, 4, 1, 0], [4, -1, -7, -7, 10]]
		test_mask = [[0,5],[-5,0]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[2, 10, -8, 7, -8], [-7, 10, -12, 7, -1], [-10, 12, 6, 7, 0], [3, 9, -1, 1, -5], [4, 4, -7, -2, 10]])

	def test_apply_17(self):
		test_ls =   [[3, 4, -3, -7, 8, -9], [-5, 1, -9, -5, -5, 10], [-3, 2, 8, -7, 10, 4], [10, 9, -7, 9, 4, 7], [-6, 8, 1, 3, 3, -1], [7, -5, 5, -6, 3, 7]]
		test_mask = [[-6,6],[6,-6]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[-3, 10, -9, -1, 2, -3], [1, -5, -3, -11, 1, 4], [-9, 8, 2, -1, 4, 10], [16, 3, -1, 3, 10, 1], [-12, 14, -5, 9, -3, 5], [13, -11, 11, -12, 9, 1]])

	def test_apply_18(self):
		test_ls =   [[-6, -6, 10, -8, 6, 0, -6, 0, -10, -1], [6, -5, 8, 6, 0, 2, 5, 7, 2, 9], [8, -3, -9, 5, 0, 3, -2, -3, -4, 10], [10, -6, 2, 10, 6, 1, 10, 3, 10, 3], [-1, -9, 4, -9, 0, -5, 6, 5, -10, 4]]
		test_mask = [[10,20],[20,10]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[4, 14, 20, 12, 16, 20, 4, 20, 0, 19], [26, 5, 28, 16, 20, 12, 25, 17, 22, 19], [18, 17, 1, 25, 10, 23, 8, 17, 6, 30], [30, 4, 22, 20, 26, 11, 30, 13, 30, 13], [9, 11, 14, 11, 10, 15, 16, 25, 0, 24]])

	def test_apply_19(self):
		test_ls =   [[-3, 10, 7, 2, -2], [-8, -3, -3, -4, -2], [5, 10, 2, -1, -4], [-8, -5, -2, 9, 0], [2, 6, 5, -8, 5], [-5, 2, -3, -10, -5], [-3, 0, 2, 5, 3], [4, -3, 2, -1, 2], [5, -7, 4, 0, -5], [4, -4, -6, -2, 0]]
		test_mask = [[0,5],[-5,-10]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[-3, 15, 7, 7, -2], [-13, -13, -8, -14, -7], [5, 15, 2, 4, -4], [-13, -15, -7, -1, -5], [2, 11, 5, -3, 5], [-10, -8, -8, -20, -10], [-3, 5, 2, 10, 3], [-1, -13, -3, -11, -3], [5, -2, 4, 5, -5], [-1, -14, -11, -12, -5]])

	def test_apply_20(self):
		test_ls =   [[-6, 3, -6, -4, 2, -6, 10, -10], [5, 1, 5, 5, 1, 0, -8, 5], [-7, 4, -2, 6, 1, -2, 3, -8], [-2, -6, 1, -1, -5, -9, 9, 4]]
		test_mask = [[10,10],[10,10]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[4, 13, 4, 6, 12, 4, 20, 0], [15, 11, 15, 15, 11, 10, 2, 15], [3, 14, 8, 16, 11, 8, 13, 2], [8, 4, 11, 9, 5, 1, 19, 14]])

	def test_apply_21(self):
		test_ls =   [[-9, 9, -9, -1], [4, -2, 2, 8], [8, 1, -1, 5], [-5, -10, -10, 1], [-5, -5, 6, -3], [-5, -5, -10, -2], [2, 5, -2, 8], [-1, -8, -4, -10]]
		test_mask = [[10,10],[10,10]]
		res = apply(test_mask, test_ls)
		self.assertEqual(test_ls, [[1, 19, 1, 9], [14, 8, 12, 18], [18, 11, 9, 15], [5, 0, 0, 11], [5, 5, 16, 7], [5, 5, 0, 8], [12, 15, 8, 18], [9, 2, 6, 0]])


	############################################################################

# This class digs through AllTests, counts and builds all the tests,
# so that we have an entire test suite that can be run as a group.
class TheTestSuite (unittest.TestSuite):
	# constructor.
	def __init__(self,wants):
		self.num_req = 0
		self.num_ec = 0
		# find all methods that begin with "test".
		fs = []
		for w in wants:
			for func in AllTests.__dict__:
				# append regular tests
				# drop any digits from the end of str(func).
				dropnum = str(func)
				while dropnum[-1] in "1234567890":
					dropnum = dropnum[:-1]

				if dropnum==("test_"+w+"_") and (not (dropnum==("test_extra_credit_"+w+"_"))):
					fs.append(AllTests(str(func)))
				if dropnum==("test_extra_credit_"+w+"_") and not BATCH_MODE:
					fs.append(AllTests(str(func)))

#		print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
		# call parent class's constructor.
		unittest.TestSuite.__init__(self,fs)

class TheExtraCreditTestSuite (unittest.TestSuite):
		# constructor.
		def __init__(self,wants):
			# find all methods that begin with "test_extra_credit_".
			fs = []
			for w in wants:
				for func in AllTests.__dict__:
					if str(func).startswith("test_extra_credit_"+w):
						fs.append(AllTests(str(func)))

#			print("TTS ====> ",list(map(lambda f: (f,id(f)),fs)))
			# call parent class's constructor.
			unittest.TestSuite.__init__(self,fs)

# all (non-directory) file names, regardless of folder depth,
# under the given directory 'dir'.
def files_list(dir):
	this_file = __file__
	if dir==".":
		dir = os.getcwd()
	info = os.walk(dir)
	filenames = []
	for (dirpath,dirnames,filez) in info:
#		print(dirpath,dirnames,filez)
		if dirpath==".":
			continue
		for file in filez:
			if file==this_file:
				continue
			filenames.append(os.path.join(dirpath,file))
#		print(dirpath,dirnames,filez,"\n")
	return filenames

def main():
	if len(sys.argv)<2:
		raise Exception("needed student's file name as command-line argument:"\
			+"\n\t\"python3 testerX.py gmason76_2xx_Px.py\"")

	if BATCH_MODE:
		print("BATCH MODE.\n")
		run_all()
		return

	else:
		want_all = len(sys.argv) <=2
		wants = []
		# remove batch_mode signifiers from want-candidates.
		want_candidates = sys.argv[2:]
		for i in range(len(want_candidates)-1,-1,-1):
			if want_candidates[i] in ['.'] or os.path.isdir(want_candidates[i]):
				del want_candidates[i]

		# set wants and extra_credits to either be the lists of things they want, or all of them when unspecified.
		wants = []
		extra_credits = []
		if not want_all:
			for w in want_candidates:
				if w in REQUIRED_DEFNS:
					wants.append(w)
				elif w in SUB_DEFNS:
					wants.append(w)
				elif w in EXTRA_CREDIT_DEFNS:
					extra_credits.append(w)
				else:
					raise Exception("asked to limit testing to unknown function '%s'."%w)
		else:
			wants = REQUIRED_DEFNS + SUB_DEFNS
			extra_credits = EXTRA_CREDIT_DEFNS

		# now that we have parsed the function names to test, run this one file.
		run_one(wants,extra_credits)
		return
	return # should be unreachable!

# only used for non-batch mode, since it does the printing.
# it nicely prints less info when no extra credit was attempted.
def run_one(wants, extra_credits):

	has_reqs = len(wants)>0
	has_ec   = len(extra_credits)>0

	# make sure they exist.
	passed1 = 0
	passed2 = 0
	tried1 = 0
	tried2 = 0

	# only run tests if needed.
	if has_reqs:
		print("\nRunning required definitions:")
		(tag, passed1,tried1) = run_file(sys.argv[1],wants,False)
	if has_ec:
		print("\nRunning extra credit definitions:")
		(tag, passed2,tried2) = run_file(sys.argv[1],extra_credits,True)

	# print output based on what we ran.
	if has_reqs and not has_ec:
		print("\n%d/%d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
		print("\nScore based on test cases: %.2f/%d (%.2f*%d) " % (
																passed1*weight_required,
																total_points_from_tests,
																passed1,
																weight_required
															 ))
	elif has_ec and not has_reqs:
		print("%d/%d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
	else: # has both, we assume.
		print("\n%d / %d Required test cases passed (worth %d each)" % (passed1,tried1,weight_required) )
		print("%d / %d Extra credit test cases passed (worth %d each)" % (passed2, tried2, weight_extra_credit))
		print("\nScore based on test cases: %.2f / %d ( %d * %d + %d * %d) " % (
																passed1*weight_required+passed2*weight_extra_credit,
																total_points_from_tests,
																passed1,
																weight_required,
																passed2,
																weight_extra_credit
															 ))
	if CURRENTLY_GRADING:
		print("( %d %d %d %d )\n%s" % (passed1,tried1,passed2,tried2,tag))

# only used for batch mode.
def run_all():
		filenames = files_list(sys.argv[1])
		#print(filenames)

		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS

		results = []
		for filename in filenames:
			print(" Batching on : " +filename)
			# I'd like to use subprocess here, but I can't get it to give me the output when there's an error code returned... TODO for sure.
			lines = os.popen("python3 tester1p.py \""+filename+"\"").readlines()

			# delay of shame...
			time.sleep(DELAY_OF_SHAME)

			name = os.path.basename(lines[-1])
			stuff =lines[-2].split(" ")[1:-1]
			print("STUFF: ",stuff, "LINES: ", lines)
			(passed_req, tried_req, passed_ec, tried_ec) = stuff
			results.append((lines[-1],int(passed_req), int(tried_req), int(passed_ec), int(tried_ec)))
			continue

		print("\n\n\nGRAND RESULTS:\n")


		for (tag_req, passed_req, tried_req, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req).strip()
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible,
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))
# only used for batch mode.
def run_all_orig():
		filenames = files_list(sys.argv[1])
		#print(filenames)

		wants = REQUIRED_DEFNS + SUB_DEFNS
		extra_credits = EXTRA_CREDIT_DEFNS

		results = []
		for filename in filenames:
			# wipe out all definitions between users.
			for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
				globals()[fn] = decoy(fn)
				fn = decoy(fn)
			try:
				name = os.path.basename(filename)
				print("\n\n\nRUNNING: "+name)
				(tag_req, passed_req, tried_req) = run_file(filename,wants,False)
				(tag_ec,  passed_ec,  tried_ec ) = run_file(filename,extra_credits,True)
				results.append((tag_req,passed_req,tried_req,tag_ec,passed_ec,tried_ec))
				print(" ###### ", results)
			except SyntaxError as e:
				tag = filename+"_SYNTAX_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except NameError as e:
				tag =filename+"_Name_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ValueError as e:
				tag = filename+"_VALUE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except TypeError as e:
				tag = filename+"_TYPE_ERROR"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except ImportError as e:
				tag = filename+"_IMPORT_ERROR_TRY_AGAIN"
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))
			except Exception as e:
				tag = filename+str(e.__reduce__()[0])
				results.append((tag,0,len(wants),tag,0,len(extra_credits)))

# 			try:
# 				print("\n |||||||||| scrupe: "+str(scruples))
# 			except Exception as e:
# 				print("NO SCRUPE.",e)
# 			scruples = None

		print("\n\n\nGRAND RESULTS:\n")
		for (tag_req, passed_req, tried_req, tag_ec, passed_ec, tried_ec) in results:
			name = os.path.basename(tag_req)
			earned   = passed_req*weight_required + passed_ec*weight_extra_credit
			possible = tried_req *weight_required # + tried_ec *weight_extra_credit
			print("%10s : %3d / %3d = %5.2d %% (%d/%d*%d + %d/%d*%d)" % (
															name,
															earned,
															possible,
															(earned/possible)*100,
															passed_req,tried_req,weight_required,
															passed_ec,tried_ec,weight_extra_credit
														  ))

def try_copy(filename1, filename2, numTries):
	have_copy = False
	i = 0
	while (not have_copy) and (i < numTries):
		try:
			# move the student's code to a valid file.
			shutil.copy(filename1,filename2)

			# wait for file I/O to catch up...
			if(not wait_for_access(filename2, numTries)):
				return False

			have_copy = True
		except PermissionError:
			print("Trying to copy "+filename1+", may be locked...")
			i += 1
			time.sleep(1)
		except BaseException as e:
			print("\n\n\n\n\n\ntry-copy saw: "+e)

	if(i == numTries):
		return False
	return True

def try_remove(filename, numTries):
	removed = False
	i = 0
	while os.path.exists(filename) and (not removed) and (i < numTries):
		try:
			os.remove(filename)
			removed = True
		except OSError:
			print("Trying to remove "+filename+", may be locked...")
			i += 1
			time.sleep(1)
	if(i == numTries):
		return False
	return True

def wait_for_access(filename, numTries):
	i = 0
	while (not os.path.exists(filename) or not os.access(filename, os.R_OK)) and i < numTries:
		print("Waiting for access to "+filename+", may be locked...")
		time.sleep(1)
		i += 1
	if(i == numTries):
		return False
	return True

# this will group all the tests together, prepare them as
# a test suite, and run them.
def run_file(filename,wants=None,checking_ec = False):
	if wants==None:
		wants = []

	# move the student's code to a valid file.
	if(not try_copy(filename,"student.py", 5)):
		print("Failed to copy " + filename + " to student.py.")
		quit()

	# import student's code, and *only* copy over the expected functions
	# for later use.
	import importlib
	count = 0
	while True:
		try:
# 			print("\n\n\nbegin attempt:")
			while True:
				try:
					f = open("student.py","a")
					f.close()
					break
				except:
					pass
# 			print ("\n\nSUCCESS!")

			import student
			importlib.reload(student)
			break
		except ImportError as e:
			print("import error getting student... trying again. "+os.getcwd(), os.path.exists("student.py"),e)
			time.sleep(0.5)
			while not os.path.exists("student.py"):
				time.sleep(0.5)
			count+=1
			if count>3:
				raise ImportError("too many attempts at importing!")
		except SyntaxError as e:
			print("SyntaxError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_SYNTAX_ERROR",None, None, None)
		except NameError as e:
			print("NameError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return((filename+"_Name_ERROR",0,1))
		except ValueError as e:
			print("ValueError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_VALUE_ERROR",0,1)
		except TypeError as e:
			print("TypeError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+"_TYPE_ERROR",0,1)
		except ImportError as e:
			print("ImportError in "+filename+":\n"+str(e))
			print("Run your file without the tester to see the details or try again")
			return((filename+"_IMPORT_ERROR_TRY_AGAIN	",0,1))
		except Exception as e:
			print("Exception in loading"+filename+":\n"+str(e))
			print("Run your file without the tester to see the details")
			return(filename+str(e.__reduce__()[0]),0,1)

	# make a global for each expected definition.
	for fn in REQUIRED_DEFNS+EXTRA_CREDIT_DEFNS	:
		globals()[fn] = decoy(fn)
		try:
			globals()[fn] = getattr(student,fn)
		except:
			if fn in wants:
				print("\nNO DEFINITION FOR '%s'." % fn)

	if not checking_ec:
		# create an object that can run tests.
		runner = unittest.TextTestRunner()

		# define the suite of tests that should be run.
		suite = TheTestSuite(wants)


		# let the runner run the suite of tests.
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		# print(ans)

	else:
		# do the same for the extra credit.
		runner = unittest.TextTestRunner()
		suite = TheExtraCreditTestSuite(wants)
		ans = runner.run(suite)
		num_errors   = len(ans.__dict__['errors'])
		num_failures = len(ans.__dict__['failures'])
		num_tests    = ans.__dict__['testsRun']
		num_passed   = num_tests - num_errors - num_failures
		#print(ans)

	# remove our temporary file.
	os.remove("student.py")
	if os.path.exists("__pycache__"):
		shutil.rmtree("__pycache__")
	if(not try_remove("student.py", 5)):
		print("Failed to remove " + filename + " to student.py.")

	tag = ".".join(filename.split(".")[:-1])


	return (tag, num_passed, num_tests)


# make a global for each expected definition.
def decoy(name):
		# this can accept any kind/amount of args, and will print a helpful message.
		def failyfail(*args, **kwargs):
			return ("<no '%s' definition was found - missing, or typo perhaps?>" % name)
		return failyfail

# this determines if we were imported (not __main__) or not;
# when we are the one file being run, perform the tests! :)
if __name__ == "__main__":
	main()
