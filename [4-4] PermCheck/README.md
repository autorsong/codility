# 문제

길이가 N인 정수 배열 A가 주어지는데 A 안에 1부터 N까지 정수들이 모두 오직 한 번씩만 들어있으면 1을, 아니면 0을 리턴하라  

# solution

너무 간단해서 말할 것도 없네예  

# sth else

간단한 문제인 만큼 여러 가지의 솔루션이 가능한 것 같음  

```{.python}
if max(A) != len(A) or len(set(A)) != len(A):  
    return 0  
return 1  
```

이런 간단하고 멋있는 방법도 있고  
bitwise 연산자를 사용하는 방법  

```{.python}
for i in range(1, N+1):  
    xorSum ^= i ^ A[i-1]  

if xorSum == 0:  
    return 1  
else:  
    return 0  
```

도 있다.  
bitwise 진짜 신박하다...  
