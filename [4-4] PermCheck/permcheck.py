def solution(A):
    A.sort()
    prev = 0

    for i in A:
        if i == prev + 1:
            prev = i
        else:
            return 0

    return 1
