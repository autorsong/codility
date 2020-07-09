def solution(A, B):
    if len(set(B)) == 1:
        return len(A)

    stack = []

    for i in range(len(A)):
        if len(stack) == 0:
            stack.append((A[i], B[i]))

        else:
            if B[i] == 1 and stack[len(stack) - 1][1] == 0:
                stack.append((A[i], B[i]))

            elif B[i] == 0 and stack[len(stack) - 1][1] == 1:
                while stack[len(stack) - 1][1] == 1:
                    if A[i] > stack[len(stack) - 1][0]:
                        del stack[len(stack) - 1]

                        if len(stack) == 0:
                            break
                    else:
                        break

                if len(stack) > 0:
                    if stack[len(stack) - 1][1] == 1 and A[i] < stack[len(stack) - 1][0]:
                        pass
                    else:
                        stack.append((A[i], B[i]))
                else:
                    stack.append((A[i], B[i]))

            else:
                stack.append((A[i], B[i]))

    return len(stack)
