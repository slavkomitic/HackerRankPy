def circular_array_rotation(a, k, queries):
    """
    @https://www.hackerrank.com/challenges/circular-array-rotation/problem
    """
    k = k % len(a)
    a = a[-k:] + a[:-k]
    return [a[q] for q in queries]


if __name__ == "__main__":

    print(circular_array_rotation([3, 4, 5], 2, [0, 1, 2]))
    print(circular_array_rotation([3, 4, 5], 4, [0, 1, 2]))
