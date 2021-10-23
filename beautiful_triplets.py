def beautiful_triplets(d, arr):
    """
    @https://www.hackerrank.com/challenges/beautiful-triplets/problem
    """
    triplets = 0
    numbers = sorted(arr)
    for n in numbers:
        if (first:=(n + d)) in numbers:
            if (first + d) in numbers:
                triplets += 1

    return triplets


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 8, 10]
    d = 3
    print(beautiful_triplets(d, arr))

    arr = [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]
    d = 3
    print(beautiful_triplets(d, arr))
