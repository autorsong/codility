def solution(S):
    stack = 0

    for s in S:
        if s == "(":
            stack += 1

        else:
            if stack > 0:
                stack -= 1
            else:
                return 0

    return 1 if stack == 0 else 0
