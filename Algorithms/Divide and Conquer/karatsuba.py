def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    a, b = divmod(x, 10 ** m)
    c, d = divmod(y, 10 ** m)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * 10 ** (2 * m) + ad_bc * 10 ** m + bd


if __name__ == '__main__':
    x = 1234
    y = 5678
    print(karatsuba(x, y))
