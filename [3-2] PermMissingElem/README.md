# 문제

N 길이의 배열 A가 주어지고 A 안에는 1에서 N+1 사이의 정수들이 한 개씩 있다  
즉 1에서 N+1 사이에 한 개의 숫자가 빠져있다는 것  
빠진 숫자가 무엇인지 구하라  

# solution 

먼저 리스트가 비어있을 경우를 생각해야 한다  
그리고 시작과 끝 값을 잘 생각해야 한다  
즉 A를 정렬했을 때 sequence가 2부터 시작하는 경우, 마지막 값까지 비는 값 없이 연속되는 경우 처리 필요  

항상 주어진 input 값의 범위를 잘 확인하자  

# sth else

python의 list의 내장 method 인 sort() 는 timsort 라는 알고리즘을 사용한다  
worst case time complexity 가 n log n, best 가 n 이다  