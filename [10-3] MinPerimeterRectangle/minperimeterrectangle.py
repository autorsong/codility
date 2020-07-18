def solution(N):
    factor = 1
    garo = 0

    while factor * factor <= N:
        if N % factor == 0:
            garo = factor
        factor += 1

    sero = N / garo

    return int(2 * (garo + sero))
