def making_anagrams(first, second):
    """
    @https://www.hackerrank.com/challenges/making-anagrams/problem
    """
    letters = sorted(set(first+second))
    first, second = list(first), list(second)

    f = [(letter, first.count(letter)) for letter in letters]
    s = [(letter, second.count(letter)) for letter in letters]

    diffs = [abs(a[1]-b[1]) for a, b in zip(f, s)]
    return sum(diffs)


if __name__ == '__main__':

    a = 'cde'
    b = 'abc'
    print(making_anagrams(a, b))
