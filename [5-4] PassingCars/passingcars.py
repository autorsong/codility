def solution(A):
    cross_count = 0
    crossing = 0

    for car in A:
        if car == 0:
            cross_count += 1

        elif car == 1:
            crossing += cross_count

        if crossing > 1000000000:
            crossing = -1
            break

    return crossing
