# 문제

N개의 정수가 들어있는 배열 A가 주어진다 (1 < N <= 100000)  
그리고 N보다 작고 0보다 큰 정수 P가 주어지는데 이 P라는 인덱스를 기준으로 A를 앞뒤로 나누고 나눈 각각의 배열 안의 값을 모두 합친다  
이 각각 합친 값의 절대값의 차이 중 가장 작은 값을 return

# solution

별 거 없는 문제  
O(n) 으로 앞에거에 더해주고 뒤에거 빼주면서 비교  

근데 더 깔끔한 코드로 풀 수 있진 않을까?  