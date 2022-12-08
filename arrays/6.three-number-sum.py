"""
Day 3: 6th Dec 2022
Arrays - Medium Problem - 6
https://www.algoexpert.io/questions/three-number-sum

Three Number Sum
"""

#Solution 1 - START
def nonConstructibleChange(coins):
    """
    Time Complexity : O(N log(N)) + O(N) = O(N log(N))
    Space Complexity: O(1)
    """
    coins.sort()

    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    return currentChangeCreated + 1
#Solution 1 - END


