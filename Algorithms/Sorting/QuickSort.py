def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[pivot_index] > my_list[i]:
            swap_index += 1
            my_list[swap_index], my_list[i] = my_list[i], my_list[swap_index]

    my_list[pivot_index], my_list[swap_index] = my_list[swap_index], my_list[pivot_index]
    return swap_index


def quick_sort(my_list, left, right):
    if left >= right:
        return
    pivot_index = pivot(my_list, left, right)
    quick_sort(my_list, left, pivot_index - 1)
    quick_sort(my_list, pivot_index + 1, right)
    return my_list


a = list(map(int, input().split()))
quick_sort(a, 0, len(a)-1)
print(a)
