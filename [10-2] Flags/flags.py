def solution(A):
    peaks = [0] * len(A)
    next_peaks = [0] * len(A)

    for i in range(1, len(A) - 1):
        peaks[i] = 1 if A[i] > A[i - 1] and A[i] > A[i + 1] else 0

    next_peaks[-1] = -1

    for i in range(len(A) - 2, -1, -1):
        next_peaks[i] = i if peaks[i] == 1 else next_peaks[i + 1]

    if len(peaks) == 0:
        return 0

    max_flags = 0
    num_flags = 2

    while num_flags * (num_flags - 1) < len(A):
        flags = 0
        peak_index = 0

        while peak_index < len(A) and flags < num_flags:
            peak_index = next_peaks[peak_index]

            if peak_index == -1:
                break

            flags += 1
            peak_index += num_flags

        max_flags = max(max_flags, flags)
        num_flags += 1

    return max_flags
