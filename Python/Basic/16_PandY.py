def solution(s):
    p = 0
    y = 0

    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            p += 1
        elif s[i] == "y" or s[i] == "Y":
            y += 1

    return p == y


def solution1(s):
    return s.lower().count('p') == s.lower().count('y')

