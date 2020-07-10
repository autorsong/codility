def solution(A):
    front = {}
    back = {}

    equi_leader = 0

    front_len = 0
    back_len = len(A)

    front_leader = None
    front_leader_count = 0

    for num in A:
        back[num] = back.get(num, 0) + 1

    for num in A:
        front[num] = front.get(num, 0) + 1
        back[num] = back.get(num, 0) - 1
        front_len += 1
        back_len -= 1

        if front_leader is None or front[num] > front_leader_count:
            front_leader = num
            front_leader_count = front[num]

        front_leader = front_leader if front[front_leader] > 0.5 * front_len else None

        if front_leader is not None:
            back_leader = front_leader if back[front_leader] > 0.5 * back_len else None

        if front_leader == back_leader and front_leader is not None:
            equi_leader += 1

    return equi_leader
