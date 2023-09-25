"""
Task description:
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it. 
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

Explanation:
A zero-based permutation nums is an array of distinct integers where the values are a rearrangement of the indices. 
In other words, it's an array where each number appears exactly once, and those numbers are drawn from the range of indices (0 to nums.length - 1) in the array. 
This means that the values in the array represent a permutation of the indices starting from zero.
"""

"""
This solution follows a cyclic permutation technique. It involves two passes through the array to rearrange the elements using constant extra space (O(1)).
In the first loop, we modify each nums[i] value to hold both the original value and the new value. We use (nums[nums[i]] % n) * n to store the new value in the nums[i] position.
In the second loop, we divide each nums[i] value by n to extract the original value (restoring it) and place the desired value (ans[i]) in the correct position.
The cyclic permutation approach ensures O(1) space complexity while rearranging the array as required by the problem statement.
"""

"""
Let's walk through the example of nums = [2, 0, 1, 3] and apply the formula nums[i] = nums[i] + n * (nums[nums[i]] % n) step by step:

Given nums = [2, 0, 1, 3] and n = 4 (length of nums):

1. For i = 0:
   - nums[0] = 2, so nums[nums[0]] = nums[2] = 1
   - 1 % 4 = 1
   - nums[0] = nums[0] + 4 * 1 = 2 + 4 = 6
   
   Updated nums: [6, 0, 1, 3]

2. For i = 1:
   - nums[1] = 0, so nums[nums[1]] = nums[0] = 6
   - 6 % 4 = 2
   - nums[1] = nums[1] + 4 * 2 = 0 + 8 = 8
   
   Updated nums: [6, 8, 1, 3]

3. For i = 2:
   - nums[2] = 1, so nums[nums[2]] = nums[1] = 8
   - 8 % 4 = 0
   - nums[2] = nums[2] + 4 * 0 = 1 + 0 = 1
   
   Updated nums: [6, 8, 1, 3]

4. For i = 3:
   - nums[3] = 3, so nums[nums[3]] = nums[3] = 3
   - 3 % 4 = 3
   - nums[3] = nums[3] + 4 * 3 = 3 + 12 = 15
   
   Updated nums: [6, 8, 1, 15]

After applying the formula for all i values, the final updated nums array is [6, 8, 1, 15]. This process represents the first loop in the solution, where we modify each nums[i] value
 to store both the original value and the new value.
"""
class CyclicPermutationArray:
    def __init__(self, nums):
        self._nums = nums
        self._n = len(nums)
    
    def __len__(self):
        return self._n
        
    
    def getInputValue(self, i):
        # [0 .. n-1]
        return self._nums[i] % self._n;

    #make function that overloads [] operator
    def __getitem__(self, i):
        return self.getInputValue(i)
    
    def setNewValue(self, i, newValue):
        # [0 .. n-1] already taken for input values
        # [0 .. n-1] for new values
        # [0 .. n^2 - n] for newValue * n, intersection only in 0 when both new and input values are 0.
       # self._nums[i] = self._nums[i] + (newValue * self._n + self._n)
        self._nums[i] = self.getInputValue(i) + newValue * self._n
    
    def getNewValue(self, i):
        # [0 .. n^2 - n] for newValue * n, intersection only in 0 when both new and input values are 0.
        # [0 .. n-1]
        return self._nums[i] // self._n 
    
    def getArray(self):
        return self._nums
    
    # clear input value and keep new values only in range [0 .. n-1]
    def buildNewArray(self):
        for i in range(len(self)):
            self._nums[i] = self.getNewValue(i)       

def calculateNewValue(cyclic_array, i):
    return cyclic_array[cyclic_array[i]]

def build_array(nums):
    cyclic_array = CyclicPermutationArray(nums)  # stores array with input values and calculated values: getInputValue(i), setNewValue(i, value), buildNewArray(), getArray(), len()
    
    # calculate new values
    for i in range(len(cyclic_array)):
        # function that calculates new value for index i (TBD)
        newValue = cyclic_array[cyclic_array[i]]
        cyclic_array.setNewValue(i, newValue)

    cyclic_array.buildNewArray()
    
    return cyclic_array.getArray()

# Example usage
nums = [0,2,1,5,3,4]
result = build_array(nums)
print(result)  # Output: [0, 1, 2, 4, 5, 3]
