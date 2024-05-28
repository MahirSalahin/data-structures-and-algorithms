def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        j = i
        while j > 0 and my_list[j] < my_list[j-1]:
            my_list[j-1], my_list[j] = my_list[j], my_list[j-1]
            j -= 1
    return my_list


if __name__ == '__main__':
    a = [12, 1, 3, 124, 5, 986, 2, 6]
    print(insertion_sort(a))
