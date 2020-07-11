def solution(A):
    if len(A) == 0:
        return 0

    profit = 0
    minimal = A[0]

    for num in A[1:]:
        cur = num - minimal

        if cur > 0:
            profit = profit if profit > cur else cur
        else:
            minimal = num

    return profit
