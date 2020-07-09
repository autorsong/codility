def solution(S):
    stack = []

    for s in S:
        if s == "(" or s == "{" or s == "[":
            stack.append(s)

        elif s == ")" or s == "}" or s == "]":
            if len(stack) == 0:
                return 0

            if s == ")":
                if stack[len(stack) - 1] == "(":
                    del stack[(len(stack) - 1)]
                else:
                    return 0

            elif s == "}":
                if stack[len(stack) - 1] == "{":
                    del stack[(len(stack) - 1)]
                else:
                    return 0

            elif s == "]":
                if stack[len(stack) - 1] == "[":
                    del stack[(len(stack) - 1)]
                else:
                    return 0

        else:
            continue

    return 1 if len(stack) == 0 else 0
