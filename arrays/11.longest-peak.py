"""
Day 6: 9th Dec 2022
Arrays - Medium Problem - 11
https://www.algoexpert.io/questions/longest-peak

Longest Peak
"""

#Solution 1 - START
def longestPeak(array):
    """
    Time Complexity : O(N) - Each element is traversed at least one and only elements to the left will be traversed more than once i.e. max 2 or 3 times not more than that
    Space Complexity: O(1)
    """
    maxPeakLength = 0
    idx = 1
    while idx < len(array) - 1:
        isPeak = array[idx - 1] < array[idx] and array[idx] > array[idx + 1]
        if not isPeak:
            idx += 1
            continue

        leftIdx = idx - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = idx + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
        currentPeak = rightIdx - leftIdx - 1
        maxPeakLength = max(maxPeakLength, currentPeak)
        idx = rightIdx
    return maxPeakLength
#Solution 1 - END
