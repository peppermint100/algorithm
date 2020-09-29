## 문제
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

## 풀이 전략
- g, s를 모두 오름차순 정렬하고 0번 인덱스 부터 탐색하며 같은 값 또는 더 크다면 인덱스를 하나씩 증가시키고 카운트에 1을 더함
- 만족시킬수 없다면 반복문 종료하고 카운트를 리턴 