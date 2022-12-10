"""
Day 7: 10th Dec 2022
Arrays - Medium Problem - 14
https://www.algoexpert.io/questions/merge-overlapping-intervals

Merge Overlapping Intervals
"""

#Solution 1 - START
def mergeOverlappingIntervals(intervals):
    """
    Time Complexity : O(N log(N)) + O(N) = O(N log(N))
    Space Complexity: O(N)
    """
    sortedIntervals = sorted(intervals, key = lambda item: item[0])
    result = []
    currentInterval = sortedIntervals[0]
    result.append(currentInterval)
    for nextInterval in sortedIntervals:
        if nextInterval[0] <= currentInterval[1]:
            currentInterval = [currentInterval[0], max(currentInterval[1], nextInterval[1])]
            result[-1] = currentInterval
        else:
            currentInterval = nextInterval
            result.append(nextInterval)
    return result            
#Solution 1 - END

#Solution 2 - START
def mergeOverlappingIntervals(intervals):
    """
    Time Complexity : O(N log(N)) + O(N) = O(N log(N))
    Space Complexity: O(N)
    """    
    sortedIntervals = sorted(intervals, key=lambda item: item[0])
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)
    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
    return mergedIntervals
#Solution 2 - END


