# 문제

현재 위치 x와 목표 위치 y 값이 주어졌을 때 한 번의 이동 거리 d를 얼마나 반복하여 이동하여야 x에서 y에 도달할 수 있는 지를 구해라

# solution

```{.python}
def solution(X, Y, D):
    return int((Y - X) / D) if (Y - X) % D == 0 else int((Y - X) / D) + 1  
```

간단하다.  
올림 함수를 쓰면 더 간단했을듯  