"""
Arrays - Easy Problem
https://www.algoexpert.io/questions/validate-subsequence

Validate Subsequence
"""

#Solution 1 - START
def isValidSubsequence(array, sequence):
    """
    Time Complexity : O(N) | N = len(array)
    Space Complexity: O(1)
    """
    sequence_index = 0
    array_index = 0
    while sequence_index < len(sequence) and array_index < len(array):
        if sequence[sequence_index] == array[array_index]:
            sequence_index += 1
        array_index += 1
    return True if sequence_index == len(sequence) else False
#Solution 1 - END

#Solution 2 - START
def isValidSubsequence(array, sequence):
    """
    Time Complexity : O(N) | N = len(array)
    Space Complexity: O(1)    
    """
    sequence_Idx = 0
    for number in array:
        if sequence_Idx == len(sequence):
            break
        elif sequence[sequence_Idx] == number:
            sequence_Idx += 1
    return True if sequence_Idx == len(sequence) else False
#Solution 2 - END
