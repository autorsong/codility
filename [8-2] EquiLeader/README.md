# 문제

정수 배열 A가 주어졌을 때, 어떤 인덱스를 기준으로 양 쪽으로 배열을 나누면 leader (가장 많이 나온 원소) 가 같아질 때가 있는데 해당 index를 equi leader라 한다  
A의 equi leader가 몇 개 있는지 반환하라  

# solution

A를 front와 back 앞뒤로 나누어서 dict 형태로 몇 개나 나왔는지 가지고 있는데,  
front의 leader와 back의 leader가 무조건 같아야 하기에  
일단 front의 leader를 구하고 그 front의 leader가 되는 수가 back에서도 leader의 조건을 만족하는지를 보는 방식으로 구한다  
매번 max 함수를 통해 구하게 되면 시간이 많이 소요되므로  
이러한 방법을 통해야 매 이동에 상수 시간으로 구할 수 있다  
