def utopian_tree(n):
    """
    @https://www.hackerrank.com/challenges/utopian-tree/problem
    """

    height = 1
    for period in range(1, n+1):
        if not period % 2:
            height += 1
        else:
            height *= 2

    return height


if __name__ == "__main__":

    print(utopian_tree(5))
