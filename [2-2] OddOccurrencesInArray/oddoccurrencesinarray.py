# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()

    if len(A) == 1:
        return A[0]
    else:
        for i in range(0, len(A)-1, 2):
            if A[i] != A[i+1]:
                return A[i]

        return A[-1]
