def solution(N):
    factor = 1
    factors_num = 0

    while factor * factor <= N:
        if factor * factor == N:
            factors_num += 1
        elif N % factor == 0:
            factors_num += 2
        factor += 1

    return factors_num
