def solution(A):
    if len(A) == 2:
        return abs(A[1] - A[0])

    front = A[0]
    back = sum(A[1:])

    diff = abs(front - back)

    for i in range(1, len(A) - 1):
        front += A[i]
        back -= A[i]

        now_diff = abs(front - back)

        if now_diff < diff:
            diff = now_diff

    return diff
