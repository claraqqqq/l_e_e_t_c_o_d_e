# Search a 2D Matrix
# Write an efficient algorithm that searches for a value in 
# an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last 
# integer of the previous row.
# For example,
# Consider the following matrix:
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        idx_row = 0
        idx_col = len(matrix[0]) - 1
        while idx_row < len(matrix) and idx_col >= 0:
            if matrix[idx_row][idx_col] == target: 
                return True
            elif matrix[idx_row][idx_col] > target: 
                idx_col -= 1
            else: 
                idx_row += 1
        return False