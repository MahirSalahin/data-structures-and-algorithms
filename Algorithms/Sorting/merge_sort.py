def merge(list1, list2):
    i1 = i2 = 0
    res = []
    while i1 < len(list1) or i2 < len(list2):
        if i2 == len(list2) or (i1 < len(list1) and list1[i1] < list2[i2]):
            res.append(list1[i1])
            i1 += 1

        else:
            res.append(list2[i2])
            i2 += 1

    return res


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid = len(my_list) // 2
    left = merge_sort(my_list[: mid])
    right = merge_sort(my_list[mid:])

    return merge(left, right)


a = list(map(int, input().split()))
print(merge_sort(a))
