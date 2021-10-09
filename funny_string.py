def funny_string(word):
    """
    https://www.hackerrank.com/challenges/funny-string/problem
    """
    get_values = lambda x: [abs(ord(x[i]) - ord(x[i-1]))
                               for i, _ in enumerate(x) if i > 0]

    return "Funny" if get_values(word) == get_values(word[::-1]) else "Not Funny"


if __name__ == '__main__':

    q = "acxz"
    print(funny_string(q))
    q = "bcxz"
    print(funny_string(q))
