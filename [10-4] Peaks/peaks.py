def solution(A):
    peaks = [0] * len(A)

    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks[i] = 1

    if sum(peaks) <= 1:
        return sum(peaks)

    for i in range(sum(peaks), 0, -1):
        if len(A) % i != 0:
            continue

        div = len(A) // i
        blocks = [peaks[j * div:(j + 1) * div] for j in range(i)]

        filtered_blocks = list(filter(lambda x: sum(x) >= 1, blocks))

        if len(filtered_blocks) == len(blocks):
            return len(blocks)

    return 0
