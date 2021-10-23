def chocolate_feast(n, c, m):
    """
    @https://www.hackerrank.com/challenges/chocolate-feast/problem
    """
    wrappers = n // c
    eaten = wrappers
    while wrappers >= m:
        eaten += wrappers // m
        wrappers = wrappers // m + wrappers % m
    return eaten


if __name__ == "__main__":
    n, c, m = 10, 2, 5
    print(chocolate_feast(n, c, m))
    n, c, m = 12, 4, 4
    print(chocolate_feast(n, c, m))
    n, c, m = 6, 2, 2
    print(chocolate_feast(n, c, m))
