def bubble_sort(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


if __name__ == '__main__':
    a = [12, 1, 3, 124, 5, 986, 2, 6]
    print(bubble_sort(a))
