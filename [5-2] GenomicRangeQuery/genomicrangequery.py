def solution(S, P, Q):
    query_acc = [[0, 0, 0, 0]]
    res = []

    for index, gene in enumerate(S):
        prev = query_acc[index][:]

        if gene == 'A':
            prev[0] += 1
        elif gene == 'C':
            prev[1] += 1
        elif gene == 'G':
            prev[2] += 1
        elif gene == 'T':
            prev[3] += 1

        query_acc.append(prev)

    for K in range(len(P)):
        for i in range(4):
            if query_acc[Q[K] + 1][i] - query_acc[P[K]][i] > 0:
                res.append(i + 1)
                break

    return res
