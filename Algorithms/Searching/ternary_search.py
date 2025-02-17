def ternary_search(arr, target):
    """
    Ternary search algorithm to find the index of the target element in the array.
    Args:
        arr (list(int)): List of integers.
        target (int): The element to search for in the array.
    Returns:
        int: The index of the target element in the array. If the element is not found, returns -1.

    Time Complexity: O(log(n)), where n is the number of elements in the array.\n
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr)
    while left < right:
        mid1 = left + (right - left) // 3
        mid2 = left + 2 * (right - left) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if arr[mid1] > target:
            right = mid1
        elif arr[mid2] < target:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    print(ternary_search(arr, target))  # Output: 4
    target = 10
    print(ternary_search(arr, target))  # Output: -1
    target = 1
    print(ternary_search(arr, target))  # Output: 0
