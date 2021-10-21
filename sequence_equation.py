def sequence_equation(p):
    """
    @https://www.hackerrank.com/challenges/permutation-equation/problem
    """
    return [p.index(y)+1 for y in [p.index(x)+1 for x in sorted(p)]]


if __name__ == "__main__":
    n = [int(x) for x in '5 2 1 3 4'.split()]
    print(sequence_equation(n))
