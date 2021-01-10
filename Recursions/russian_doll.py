def russian_doll(x):
    if x == 1:
        print(f"All dolls are open")
    else:
        print(x)
        russian_doll(x - 1)


russian_doll(7)
