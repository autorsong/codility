def solution(N, A):
    mc = [0] * N
    highest = 0
    prev_max_counters = 0

    for k in A:
        if k > 0 and k <= N:
            mc[k - 1] += 1
            if mc[k - 1] > highest:
                highest = mc[k - 1]
        elif k == N + 1:
            if highest > prev_max_counters:
                mc = [highest] * N
                prev_max_counters = highest

    return mc
