# Single Number
# Given an array of integers, every element appears twice 
# except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

class Solution:
	# @param A, a list of integer
		# @return an integer
	def singleNumber(self, A):

		result = 0
		for number in A:
			result ^= number
		return result