def solution(A):
    l_sum = [0] * len(A)
    r_sum = [0] * len(A)

    for i in range(1, len(A) - 1):
        l_sum[i] = max(0, l_sum[i - 1] + A[i])
    for i in range(len(A) - 2, 0, -1):
        r_sum[i] = max(0, r_sum[i + 1] + A[i])

    maxsum = 0

    for i in range(1, len(A) - 1):
        maxsum = max(maxsum, l_sum[i - 1] + r_sum[i + 1])

    return maxsum

    # print(l_sum, r_sum)

# solution([3,2,6,-1,4,5,-1,2])