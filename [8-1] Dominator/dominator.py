def solution(A):
    A_sorted = sorted(A)

    dominator = None
    dominator_num = 0
    highest_dominator = None
    highest_dominator_num = 0

    for num in A_sorted:
        if dominator != num:
            if dominator_num > highest_dominator_num or highest_dominator is None:
                highest_dominator = dominator
                highest_dominator_num = dominator_num

            dominator = num
            dominator_num = 1

        else:
            dominator_num += 1

    if dominator_num > highest_dominator_num or highest_dominator is None:
        highest_dominator = dominator
        highest_dominator_num = dominator_num

    if highest_dominator_num > 0.5 * len(A):
        for i, num in enumerate(A):
            if num == highest_dominator:
                return i
    else:
        return -1
