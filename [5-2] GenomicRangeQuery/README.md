# 문제

DNA는 ACGT로 이루어져 있고 순서대로 1, 2, 3, 4의 impact factor를 가진다  
DNA sequence S가 주어지고 길이가 같은 P와 Q의 정수 배열이 주어진다  
P[K]는 Q[K] 보다 언제나 작거나 같다  
S[P[K]] 와 S[Q[K]] 사이의 ACGT 중 가장 작은 impact factor를 각 K마다 구하고 배열 형태로 리턴하여라  

# solution

```{.python}
def solution(S, P, Q):
    res = []

    for K in range(len(P)):
        sub_sequence = list(S[P[K]:Q[K] + 1])
        sub_sequence.sort()

        if sub_sequence[0] == 'A':
            res.append(1)
        elif sub_sequence[0] == 'C':
            res.append(2)
        elif sub_sequence[0] == 'G':
            res.append(3)
        elif sub_sequence[0] == 'T':
            res.append(4)

    return res
```

위 코드로 처음 시도해 봤는데 correctness는 100%였지만 performance 가 빵점  

prefix sum을 잘 이용해야 한다  
각 gene이 누적될 때마다 더해준 결과를 query_acc에 추가  
*** 이 과정에서 prev를 구할 때 [:] 가 없으면 이전 값을 바꾸게 됨 (새로운 객채 생성 X, 복사를 해야 함)  
