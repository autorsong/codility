# 문제

홀수 길이의 배열에 딱 하나의 값만 한 개가 들어있고 나머지는 모두 두 개씩 숫자가 들어있다  
배열 속 홀로 있는 짝을 못 지은 숫자를 찾아 리턴하라

# solution

    ```{.python}
def solution(A):  
    A.sort()
    
    if len(A) == 1:
        return A[0]
    else:
        if A[0] != A[1]:
            return A[0]
        elif A[-1] != A[-2]:
            return A[-1]
        else:
            for i in range(1, len(A)-1):
                if A[i - 1] != A[i] and A[i] != A[i + 1]:
                    return A[i]
    ```

대체적으로 맞지만 '짝'이라는 게 중요했음  
배열 안의 짝을 못 지은 숫자가 배열에서 유일하게 나오는 것은 아니다  
어떤 숫자가 3개 5개 있다면 해당 숫자가 짝을 못 찾은 숫자인 것  

그래서 3개씩 비교하는 거에서 2개씩 비교하는 것으로 변경  
코드 자체도 훨씬 간단해졌다  
문제를 잘 읽어볼 것, 그리고 설령 원래 가정이 맞다고 해도 2개 비교가 더 간단하고 일반적인 방법임  

# sth more

def solution(A):  
    return reduce(lambda x,y: x^y, A)  

bitwise 연산... 천재냐 오마에?  
특정 숫자의 bitwise xor 연산을 두번 수행하면 다시 돌아오는 원리 이용  
놀랍다.  

reduce, map, filter 함수 등도 알아두면 좋을 듯 하다  


