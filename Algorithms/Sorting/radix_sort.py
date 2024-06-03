from math import log10


def radix_sort(my_list):
    mx_digits = int(log10(max(my_list))) + 1
    for i in range(mx_digits):
        temp = []
        for j in range(10):
            for k in range(len(my_list)):
                ith_digit = (my_list[k] // (10 ** i)) % 10
                if ith_digit == j:
                    temp.append(my_list[k])
        my_list = temp
    return my_list


if __name__ == '__main__':
    a = [12, 1, 3, 124, 5, 986, 2, 6]
    print(radix_sort(a))
