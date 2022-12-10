"""
Day 7: 10th Dec 2022
Arrays - Medium Problem - 13
https://www.algoexpert.io/questions/first-duplicate-value

First Duplicate Value
"""

#Solution 1 - START
def firstDuplicateValue(array):
    """
    Time Complexity : O(N*N)
    Space Complexity: O(1)
    """
    minLengthValue = len(array)
    for idx in range(len(array)):
        for index in range(idx + 1, len(array)):
            if array[idx] == array[index]:
                minLengthValue = min(minLengthValue, index)
                break
    return array[minLengthValue] if minLengthValue != len(array) else -1
#Solution 1 - END

#Solution 2 - START
def firstDuplicateValue(array):
    """
    Time Complexity : O(N)
    Space Complexity: O(N)
    """
    isPresent = {}
    for number in array:
        if number in isPresent:
            return number
        isPresent[number] = True
    return -1
#Solution 2 - END

#Solution 3 - START
def firstDuplicateValue(array):
    """
    Time Complexity : O(N)
    Space Complexity: O(1)
    """
    for number in array:
        absValue = abs(number)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] = -1 * array[absValue - 1]
    return -1
#Solution 3 - END

