def binary_search(arr, target):
    """
    Binary search algorithm to find the index of the target element in the array.
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
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    print(binary_search(arr, target))  # Output: 4
    target = 10
    print(binary_search(arr, target))  # Output: -1
    target = 1
    print(binary_search(arr, target))  # Output: 0
