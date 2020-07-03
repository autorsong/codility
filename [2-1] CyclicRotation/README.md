# 문제
정수 배열 A가 주어졌을 때 A의 rotation이라 함은 맨 뒤의 요소가 배열의 맨 앞으로 오고 나머지 요소들이 한 칸씩 밀리는 것을 의미  
A를 K번 rotation한 배열을 리턴하라  

# solution

```{.python}
def solution(A, K):
    return A[-K:] + A[:-K]  
```

으로 처음에 풀었었는데 A의 길이보다 K가 길어지면 제대로 나오지 않는 경우가 생김  
mod를 쓰면 된다.  

```{.python}
def solution(A, K):
    return A[-(K % len(A)):] + A[:-(K % len(A))]  
```

그랬더니 zerodivision 문제 생김. 모든 예외 상황을 잘 생각하자  
일단 input이 주어지면, input 각각이 0일 상황 등 양 끝값을 먼저 생각  