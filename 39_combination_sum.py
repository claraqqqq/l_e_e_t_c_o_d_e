# Combination Sum
# Given a set of candidate numbers (C) and a target number 
# (T), find all unique combinations in C where the candidate 
# numbers sums to T.
# The same repeated number may be chosen from C unlimited 
# number of times.
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in 
# non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7, 
# A solution set is: 
# [7] 
# [2, 2, 3] 

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    
    def combinationSum(self, candidates, target):
        result = []
        self.combinationDFS(sorted(candidates), target, 0, [], result)
        return result
        
    def combinationDFS(self, candidates, target, idx, current, result):
        if target == 0:
            result.append(current)
        else:
            while idx < len(candidates) and candidates[idx] <= target:
                self.combinationDFS(candidates, target-candidates[idx], idx, current+[candidates[idx]], result)
                idx += 1