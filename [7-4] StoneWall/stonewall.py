def solution(H):
    stack = []
    wall = 0

    for h in H:
        while len(stack) > 0 and stack[-1] > h:
            stack.pop()

        if len(stack) == 0 or h > stack[-1]:
            stack.append(h)
            wall += 1

    return wall
