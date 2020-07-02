

def solution(N):
    bg = 0
    longest_bg = 0
    is_bg = False

    while N >= 1:
        remainder = N % 2
        N = int(N / 2)

        if remainder == 1:
            is_bg = True

        if remainder == 0:
            if is_bg:
                bg += 1
        else:
            if bg > longest_bg:
                longest_bg = bg
            bg = 0

    return longest_bg

print(solution(17))
