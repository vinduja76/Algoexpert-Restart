"""
Day 1: 4th Dec 2022
Arrays - Easy Problem - 1
https://www.algoexpert.io/questions/two-number-sum

Two Number Sum
"""

#Solution 1 - START
def twoNumberSum(array, targetSum):
    """
    Time Complexity : O(N)
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


#Solution 2 - START
def twoNumberSum(array, targetSum):
    """
    Time Complexity : O(N log (N)) + O(N) = O(N log(N))
    Space Complexity: O(1)
    """
    array.sort()
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx < rightIdx:
        currentTargetSum = array[leftIdx] + array[rightIdx]
        if currentTargetSum == targetSum:
            return [array[leftIdx], array[rightIdx]]
        elif currentTargetSum < targetSum:
            leftIdx += 1
        else:
            rightIdx -= 1
    return []
#Solution 2 - END


#Solution 3 - START
def twoNumberSum(array, targetSum):
    """
    Time Complexity : O(N*N)
    Space Complexity: O(1)
    """
    for index in range(len(array)):
        first_num = array[index]
        for next in range(index + 1, len(array)):
            second_num = array[next]
            if first_num + second_num == targetSum:
                return [first_num, second_num]
    return []
#Solution 3 - END
