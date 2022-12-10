"""
Day 6: 9th Dec 2022
Arrays - Medium Problem - 12
https://www.algoexpert.io/questions/array-of-products

Array of Products
"""

#Solution 1 - START
def arrayOfProducts(array):
    """
    Time Complexity : O(N*N)
    Space Complexity: O(N) 
    """
    result = []
    for index in range(len(array)):
        product = 1
        for idx in range(len(array)):
            if index == idx: continue
            product = product * array[idx]
        result.append(product)
    return result
#Solution 1 - END

#Solution 2 - START
def arrayOfProducts(array):
    """
    Time Complexity  : O(N)
    Space Complexity : O(1)
    """
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]
    products = [1 for _ in range(len(array))]

    left_product = 1
    for leftIdx in range(len(array)):
        leftProducts[leftIdx] = left_product
        left_product = left_product * array[leftIdx]

    right_product = 1
    for rightIdx in reversed(range(len(array))):
        rightProducts[rightIdx] = right_product
        right_product = right_product * array[rightIdx]

    for idx in range(len(array)):
        products[idx] = leftProducts[idx] * rightProducts[idx]
        
    return products
#Solution 2 - END

#Solution 3 - START
def arrayOfProducts(array):
    """
    Time Complexity  : O(N)
    Space Complexity : O(1)
    """
    products = [1 for _ in range(len(array))]

    left = 1
    for idx in range(len(array)):
        products[idx] = left
        left = left * array[idx]

    right = 1
    for idx in reversed(range(len(array))):
        products[idx] *= right
        right = right * array[idx]
        
    return products
#Solution 3 - END
