"""
Task description:
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it. 
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

Explanation:
A zero-based permutation nums is an array of distinct integers where the values are a rearrangement of the indices. 
In other words, it's an array where each number appears exactly once, and those numbers are drawn from the range of indices (0 to nums.length - 1) in the array. 
This means that the values in the array represent a permutation of the indices starting from zero.
"""
class Solution(object):

    # Solution with O(n) time complexity as you need to process each element of the array to calculate the corresponding value in the new array.
    # solution's runtime depends on the size of the input
    def build_array(nums):
        n = len(nums)
        ans = [0] * n
        
        for i in range(n):
            ans[i] = nums[nums[i]]
        
        return ans
    

# Example usage of first solution

input = [2, 0, 1, 3]
print(Solution.build_array(input))  # Output: [1, 2, 0, 3]

input = [0,2,1,5,3,4]
print(Solution.build_array(input))  # Output: [0, 1, 2, 4, 5, 3]

