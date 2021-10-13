def angry_professor(limit, students):
    """
    @https://www.hackerrank.com/challenges/angry-professor/problem
    """
    test = lambda x: x <= 0
    return 'NO' if len(list(filter(test, students))) >= limit else 'YES'


if __name__ == "__main__":

    k = 3
    s = [-1, -3, 4, 2]
    print(angry_professor(k, s))
