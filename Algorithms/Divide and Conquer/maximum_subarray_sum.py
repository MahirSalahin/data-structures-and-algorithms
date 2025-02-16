def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    curr_sum = 0
    left_index = mid

    # Find maximum sum for left subarray
    for i in range(mid, low - 1, -1):
        curr_sum += arr[i]
        if curr_sum > left_sum:
            left_sum = curr_sum
            left_index = i

    right_sum = float('-inf')
    curr_sum = 0
    right_index = mid + 1

    # Find maximum sum for right subarray
    for i in range(mid + 1, high + 1):
        curr_sum += arr[i]
        if curr_sum > right_sum:
            right_sum = curr_sum
            right_index = i

    return left_index, right_index, left_sum + right_sum


def find_maximum_subarray(arr, low, high):
    # Base case: if there is only one element
    if low == high:
        return low, high, arr[low]

    mid = (low + high) // 2

    # Get results from left and right subarrays and crossing sum
    left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(
        arr, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(
        arr, low, mid, high)

    # Return the maximum of the three possible cases
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


if __name__ == "__main__":
    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    n = len(arr)
    start, end, max_sum = find_maximum_subarray(arr, 0, n-1)
    print(f"Maximum subarray sum is {max_sum}")
    print(f"Subarray spans from index {start} to {end}")
    print(f"Subarray is: {arr[start:end+1]}")
