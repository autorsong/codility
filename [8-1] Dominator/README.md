An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

# 문제

정수 배열 A가 주어진다. A 안에 가장 많은 개수가 들어있는 원소의 개수가 A 전체 원소 개수의 절반이 넘으면 해당 숫자, 아니면 -1을 리턴하라

# solution 

그냥 A를 정렬한 후 앞에서부터 개수를 세고 highest를 갱신하는 방식으로 계산
근데 너무 별 방법이 아니라 다른 어떤 방법이 있지 않을까 하는 생각

# sth else