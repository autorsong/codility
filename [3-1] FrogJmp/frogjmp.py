def solution(X, Y, D):
    return int((Y - X) / D) if (Y - X) % D == 0 else int((Y - X) / D) + 1