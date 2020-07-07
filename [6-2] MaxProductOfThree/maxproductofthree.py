def solution(A):
    A.sort()

    maximal = A[-1] * A[-2] * A[-3] if A[0] * A[1] * A[-1] < A[-1] * A[-2] * A[-3] else A[0] * A[1] * A[-1]

    return maximal
