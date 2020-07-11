def solution(A):
    profit = 0
    minimal = A[0]

    for num in A[1:]:
        cur = num - minimal

        if cur > 0:
            profit = profit if profit > cur else cur
        else:
            minimal = num

    return profit
