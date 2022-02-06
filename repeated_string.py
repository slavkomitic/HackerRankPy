def repeated_string(s, n):
    """
    https://www.hackerrank.com/challenges/repeated-string/problem
    """
    full, partial = int(n/len(s)), n % len(s)
    a_counter = lambda x: len(list(filter(lambda y: y == 'a', x)))
    
    return full * a_counter(s) + a_counter(s[:partial])



if __name__ == '__main__':
    s = 'aba'
    n = 10
    print(repeated_string(s, n))