def solution(X, A):
    A_zip = []

    for K, pos in enumerate(A):
        A_zip.append((K, pos))

    A_zip_sorted = sorted(A_zip, key=lambda x: x[1])

    prev_pos = 0
    prev_K = 0

    for pos in A_zip_sorted:
        if pos[1] <= prev_pos + 1:
            if pos[1] == prev_pos + 1:
                if prev_K < pos[0]:
                    prev_K = pos[0]
            prev_pos = pos[1]
            if pos[1] == X:
                return prev_K
        else:
            return -1

    return -1
