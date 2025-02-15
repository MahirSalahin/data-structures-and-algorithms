from insertion_sort import insertion_sort


def bucket_sort(my_list):
    n = len(my_list)
    mx = max(my_list)
    bucket = [[] for _ in range(n)]
    for i in range(n):
        index = (my_list[i] * n) // (mx + 1)
        bucket[index].append(my_list[i])
    for i in range(n):
        insertion_sort(bucket[i])
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            my_list[k] = bucket[i][j]
            k += 1
    return my_list


if __name__ == '__main__':
    a = [12, 1, 3, 124, 5, 986, 2, 6]
    print(bucket_sort(a))
