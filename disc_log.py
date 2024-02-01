if __name__ == "__main__":
    g = int(input("g: "))
    p = int(input("p: "))
    h = int(input("h: "))

    i = 1
    res = g

    print(f"{g}^{i} % {p} = {res % p}")

    while res != h:
        res = (res * g) % p
        i += 1
        print(f"{g}^{i} % {p} = {res}")
