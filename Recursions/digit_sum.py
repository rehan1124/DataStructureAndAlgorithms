def digit_sum(n):
    if n == 0:
        return 0
    else:
        return int(n % 10) + digit_sum(int(n/10))


print(digit_sum(12))
