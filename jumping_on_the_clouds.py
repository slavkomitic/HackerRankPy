def jumping_on_the_clouds(clouds):
    """
    @https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
    """
    jumps, n = 0, 0
    limit = len(clouds)-2
  
    while n <= limit:
        if (n == limit) or (clouds[n+2] == 1):
            jumps += 1
            n += 1
        else:
            jumps += 1
            n += 2

    return jumps


if __name__ == "__main__":

    l1 = [int(n) for n in "0 0 1 0 0 1 0".split(" ")]
    l2 = [int(n) for n in "0 0 0 0 1 0".split(" ")]
    print(jumping_on_the_clouds(l1))
    print(jumping_on_the_clouds(l2))
