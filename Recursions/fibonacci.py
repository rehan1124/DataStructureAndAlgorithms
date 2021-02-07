def fibo(n):
    assert (n >= 0) and (int(n) == n), "Number should be positive!"
    if n in (0, 1):
        return n
    return fibo(n - 1) + fibo(n - 2)


print(fibo(9))  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
