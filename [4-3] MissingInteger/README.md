This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

# 문제

정수 배열 A가 주어진다  
A 안에 나타나지 않은 가장 작은 양의 정수를 리턴하라  

# solution

배열을 정렬하고 마지막 요소가 음수라면 바로 1을 리턴  
0부터 시작하여 값이 하나 증가하면 prev 값을 올리고  
한번에 2 이상을 점프하면 이전 값의 +1 된 값을 출력  
배열을 끝까지 순회했는데 return이 안 되었다면 배열 안에 순서대로 값이 1 증가되도록 있다는 뜻이므로  
마지막 요소에 +1 된 값을 리턴   
