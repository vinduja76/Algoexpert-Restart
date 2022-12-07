"""
Day 4: 6th Dec 2022
Arrays - Easy Problem - 7
https://www.algoexpert.io/questions/smallest-difference

Smallest Difference
"""

#Solution 1 - START
def smallestDifference(arrayOne, arrayTwo):
    """
    Time Complexity : O(M log(M)) + O(N log (N)) + (O(M) or O(N)) = O(M log(M)) + O(N log (N))
    Space Complexity: O(1)
    M = length of arrayOne | N = length of arrayTwo
    """
    arrayOne.sort()
    arrayTwo.sort()
    difference = [float('-inf'), float('inf')]
    leftIdx = 0
    rightIdx = 0
    while leftIdx < len(arrayOne) and rightIdx < len(arrayTwo):
        firstNum = arrayOne[leftIdx]
        secondNum = arrayTwo[rightIdx]
        currentDifference = abs(firstNum - secondNum)
        if currentDifference < abs(difference[0] - difference[1]):
            difference = [firstNum, secondNum]
        if firstNum < secondNum:
            leftIdx += 1
        else:
            rightIdx += 1
    return difference
#Solution 1 - END
