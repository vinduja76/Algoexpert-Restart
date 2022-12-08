"""
Day 4: 7th Dec 2022
Arrays - Medium Problem - 8
https://www.algoexpert.io/questions/move-element-to-end

Move Element to End
"""

#Solution 1 - START
def moveElementToEnd(array, toMove):
    """
    Time Complexity : O(N)
    Space Complexity: O(1)
    """
    startIdx = 0
    endIdx = len(array) - 1
    while startIdx < endIdx:
        if array[endIdx] == toMove:
            endIdx -= 1
        elif array[startIdx] == toMove:
            array[startIdx], array[endIdx] = array[endIdx], array[startIdx]
            startIdx += 1
            endIdx -= 1
        else:
            startIdx += 1
    return array
#Solution 1 - END
