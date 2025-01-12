def counting_sort(my_list):
    mx = max(my_list)
    count = [0] * (mx + 1)
    for num in my_list:
        count[num] += 1
    for i in range(1, mx + 1):
        count[i] += count[i - 1]

    result = [0] * len(my_list)
    for i in range(len(my_list) - 1, -1, -1):
        result[count[my_list[i]] - 1] = my_list[i]
        count[my_list[i]] -= 1
        
    return result


if __name__ == '__main__':
    a = [12, 1, 3, 124, 5, 986, 2, 6]
    print(counting_sort(a))
