# 문제

어떤 정수 N을 이진법으로 표현했을 때 그 이진수 sequence에서 1 사이에 둘러싸인 0의 개수를 binary gap의 길이라고 한다.  
N이 주어졌을 때 N의 이진수 표현 sequence 중 가장 긴 binary gap의 길이를 리턴하라. binary gap이 없다면 0을 리턴하라.  

# solution

결국 이진수의 뒤에서부터 binary gap을 구하게 되는데 is_bg라는 변수를 통해 1의 출현을 먼저 확인하고 나서 binary gap을 계산하기 시작한다  

# sth more

bin() 이라는 함수 사용  
strip을 사용하는 것도 생각했었는데 역시 깔끔한 풀이가 있다  
strip('0').strip('1')을 사용해 순차적으로 양 끝의 0과 1을 strip 하고 1로 split 한 후 배열의 max값 구하면 간단하게 해결  