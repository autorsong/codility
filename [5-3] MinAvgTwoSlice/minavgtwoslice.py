def solution(A):
    minimal = None
    minimal_P = 0

    if len(A) < 3:
        return 0

    for i in range(len(A) - 1):
        avg_two = (A[i] + A[i + 1]) / 2

        if i + 2 < len(A):
            avg_three = (A[i] + A[i + 1] + A[i + 2]) / 3

        if minimal is None:
            minimal = avg_two

        if minimal > avg_two:
            minimal = avg_two
            minimal_P = i

        if minimal > avg_three:
            minimal = avg_three
            minimal_P = i

    return minimal_P
