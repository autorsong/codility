def solution(A):
    A.sort()

    if A[len(A) - 1] < 0:
        return 1

    prev = 0

    for i in A:
        if i < 0:
            continue

        if i <= prev + 1:
            prev = i
        else:
            return prev + 1

    return prev + 1
