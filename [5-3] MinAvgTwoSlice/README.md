A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].

# 문제

정수 배열 A가 주어지고, 정수 페어 (P, Q)가 있을 때 A 배열의 인덱스 P, Q 사이의 값들의 평균이 최저가 되는 P의 값을 구해라.

# solution

minimal이 되는 슬라이스의 길이는 무조건 2 아니면 3일 수 밖에 없다
길이가 4 이상인 경우는 그 자체가 다시 2개 2개의 슬라이스로 나뉠 수 있는데
4개의 평균은 무조건 나뉜 2개 2개 슬라이스의 평균들의 평균이고
그러면 무조건 그 2개 2개의 각각의 평균 중 하나의 값보다 크거나 같을 것이기 때문
그래서 앞에서부터 순차적으로 2개 아님 3개만 보아 O(n) 시간에 탐색 가능하고
길이가 2인 경우만 따로 고려해주면 됨
