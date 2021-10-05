def superReducedStringFast(s):
    """
    Reduce a string of lowercase characters in range ascii[‘a’..’z’]
    by doing a series of operations. In each operation, 
    select a pair of adjacent letters that match, and delete them.

    @https://www.hackerrank.com/challenges/reduced-string/problem
    """
    new_str = [""]
    for char in s:
        if char != new_str[-1]:
            new_str.append(char)
        else:
            new_str.pop()

    return "".join(new_str) if len(new_str) > 1 else "Empty String"


def superReducedString1(s):

    ls = list(s)
    n = 0
    while n < (len(ls) - 1):
        a = ls[n]
        b = ls[n + 1]
        if a == b:
            del ls[n]
            del ls[n]
            n = max(0, n-1)
        else:
            n += 1
    return "".join(ls) if len(ls) > 0 else "Empty String"


def superReducedString2(S):
    LS = list(S)
    i = 0
    while i < len(LS)-1:
        if LS[i] == LS[i+1]:
            del LS[i]
            del LS[i]
            i = 0
            if len(LS) == 0:
                print('Empty String')
                break
        else:
            i += 1
    return ''.join(LS)


def superReducedString3(s):
    index = 0
    while index < len(s) - 1 and len(s) > 0:
        if s[index] == s[index+1]:
            s = s[:index] + s[index+2:]
            index = 0
            continue
        index += 1
    if len(s) == 0:
        return 'Empty String'
    return s


def superReducedString4(s):
    stack = ["0"]
    for g in s:
        if g == stack[-1]:
            stack.pop()
        else:
            stack.append(g)
    return "Empty String" if "".join(stack[1:]) == "" else "".join(stack[1:])


if __name__ == "__main__":
    import random
    import time

    functions = [superReducedStringFast, superReducedString1,
                 superReducedString2, superReducedString3, superReducedString4]

    s = "".join([chr(random.randint(97, 98)) for _ in range(100001)])

    for f in functions:
        print(f.__name__)
        start = time.perf_counter_ns()
        result1 = f(s)
        end = time.perf_counter_ns()
        t1 = (end-start) / 10**6
        print("Elapsed time", t1, "ms\n")