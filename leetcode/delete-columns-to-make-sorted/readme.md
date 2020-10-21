## 문제
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]]).

Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.

## 풀이 전략
이중 배열을 이용하여 첫 번째 문자부터 크기(아스키코드로 Char형태로 비교 가능)를 비교하여 오름차순이 아니라면 D에 1을 더한다.
