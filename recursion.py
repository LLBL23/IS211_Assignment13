def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)


def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


def compareTo(s1, s2):
    if s1 == '' and s2 == '':
        return 0
    elif len(s1) < len(s2):
        return 0 - len(s2)
    elif len(s1) > len(s2):
        return 0 + len(s1)
    elif s1[0] != s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])
