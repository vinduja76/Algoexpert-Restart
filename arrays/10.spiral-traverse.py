"""
Day 5: 8th Dec 2022
Arrays - Easy Problem - 10
https://www.algoexpert.io/questions/spiral-traverse

Spiral Traverse
"""

#Solution 1 - START
def spiralTraverse(array):
    """
    Time Complexity: O(M * N) | M * N = Total Number of Elements in Array
    Space Complexity: O(M * N)
    """
    startRow, endRow = 0, len(array)
    startCol, endCol = 0, len(array[0])
    result = []
    while startRow < endRow and startCol < endCol:
        for col in range(startCol, endCol):
            result.append(array[startRow][col])
        startRow += 1
        for row in range(startRow, endRow):
            result.append(array[row][endCol - 1])
        endCol -= 1
        if startRow == endRow or startCol == endCol:
            break
        for col in range(endCol - 1, startCol - 1, -1):
            result.append(array[endRow - 1][col])
        endRow -= 1
        for row in range(endRow - 1, startRow -1 , -1):
            result.append(array[row][startCol])
        startCol += 1
    return result
#Solution 1 - END
