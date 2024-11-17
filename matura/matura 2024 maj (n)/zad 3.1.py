def skrot(n):
    m = 0
    y = 1
    while n > 0:
        if not n % 2 == 0:
            m = m + n % 10 * y
            y *= 10
        else:
            pass
        n = n // 10
    return m
m = skrot(2244)
print (m)