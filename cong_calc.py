if __name__ == "__main__":
    a = input("a values: ")
    a = list(map(int,a.split(' ')))
    p = int(input("p: "))

    res = 1
    for val in a:
        prev = res
        res = res * val
        res = res % p

        print(f"{prev} * {val} mod {p} = {res}")
