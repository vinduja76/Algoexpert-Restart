"""
Arrays - Easy Problem
https://www.algoexpert.io/questions/two-number-sum

Two Number Sum
"""
#Solution 1 - START

def twoNumberSum(array, targetSum):
    # Write your code here.
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    target = {}
    for num in array:
        remaining_num = targetSum - num
        if remaining_num in target:
            return [num, remaining_num]
        target[num] = True
    return []
#Solution 1 - END
