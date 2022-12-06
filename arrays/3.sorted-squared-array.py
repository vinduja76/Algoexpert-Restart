"""
Day 2: 5th Dec 2022
Arrays - Easy Problem - 3
https://www.algoexpert.io/questions/sorted-squared-array

Sorted Squared Array
"""

#Solution 1 - START
def sortedSquaredArray(array):
    # Write your code here.
    """
    Time Compelxity : O(N log(N))
    Space Complexity: O(N) - space used for result output  
    """
    result = []
    for number in array:
        result.append(number * number)
    result.sort()
    return result
#Solution 1 - END


#Solution 2 - START
def sortedSquaredArray(array):
    """
    Time Complexity  : O(N)
    Space Complexity : O(N)
    """
    startIdx = 0
    endIdx = len(array) - 1
    result = []
    while startIdx <= endIdx:
        if abs(array[startIdx]) >= abs(array[endIdx]):
            result = [array[startIdx] * array[startIdx]] + result
            startIdx += 1
        else:
            result = [array[endIdx] * array[endIdx]] + result
            endIdx -=1
    return result
#Solution 2 - END

#Solution 2 - START
def sortedSquaredArray(array):
    """
    Time Complexity : O(N)
    Space Complexity: O(N)
    """
    startIdx = 0
    endIdx = len(array) - 1
    result = [0 for _ in range(len(array))]

    for idx in reversed(range(len(array))):
        if abs(array[startIdx]) >= abs(array[endIdx]):
            result[idx] = array[startIdx] * array[startIdx]
            startIdx += 1
        else:
            result[idx] = array[endIdx] * array[endIdx]
            endIdx -= 1
    return result
#Solution 3 - END
