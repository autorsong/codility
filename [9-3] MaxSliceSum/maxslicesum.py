def solution(A):
    sum_part = 0
    sum_max = -2147483648

    for num in A:
        sum_max = max(sum_part + num, sum_max)
        sum_part = max(0, sum_part + num)

    return sum_max
