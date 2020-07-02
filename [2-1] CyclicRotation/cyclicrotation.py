def solution(A, K):
    if K == 0 or len(A) == 0:
        return A

    return A[-(K % len(A)):] + A[:-(K % len(A))]
