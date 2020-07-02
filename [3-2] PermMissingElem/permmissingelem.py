def solution(A):
    A.sort()

    if len(A) == 0:
        return 1

    if A[0] == 2:
        return 1

    for i in range(0, len(A) - 1):
        if A[i + 1] - A[i] > 1:
            return A[i] + 1

    return A[-1] + 1
