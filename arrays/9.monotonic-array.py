"""
Day 5: 8th Dec 2022
Arrays - Medium Problem - 9
https://www.algoexpert.io/questions/monotonic-array

Monotonic Array
"""

#Solution 1 - START
def isMonotonic(array):
    """
    Time Complexity : O(N)
    Space Complexity: O(1)
    """
    if len(array) <= 1:
        return True
    index = 0
    last_seen = None
    while index < len(array) - 1:
        current = array[index]
        next = array[index + 1]
        if next < current and (last_seen is None or last_seen == 'decreasing'):
            last_seen = 'decreasing'
            index += 1
        elif next > current and (last_seen is None or last_seen == 'increasing'):
            last_seen = 'increasing'
            index += 1
        elif next == current:
            index += 1
        else:
            return False
    return True
#Solution 1 - END

#Solution 2 - START
def isMonotonic(array):
    """
    Time Complexity : O(N)
    Space Complexity: O(1)
    """
    isNonIncreasing = True
    isNonDecreasing = True
    for index in range(1, len(array)):
        if array[index] < array[index - 1]:
            isNonDecreasing = False
        if array[index] > array[index - 1]:
            isNonIncreasing = False
    return isNonIncreasing or isNonDecreasing
#Solution 2 - END
