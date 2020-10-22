## Problem

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.


```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

```

## Approach
다이나믹 프로그래밍의 전형적인 예이다. 
1. 먼저 n+1 dp 배열을 선언하고 선언한 정수 타입중 가장 큰 값 java에서는 \`Integer.MAX_VALUE\` 로 배열을 채운다. 
2. 배열을 순회하며 그 수를 이루기 위해 가장 적은 제곱수들의 조합 경우의 수는 현재 탐색 중인 제곱수를 뺀 값을 구하는 경우의 수에 제곱수 자체 = 자기자신을 구하는 수 의 방법인 한가지를 더 더하면 된다. 즉
```java
dp[i] = dp[i - j*j] + 1;
```
이다. 이 알고리즘을 이해하면 된다. 그리고 
3. 이 방법과 이전에 사용했던 방법 즉 원래 dp[i]에 저장된 값을 비교하여
우리는 최소의 경우의 수를 찾는 것이니 java의 \`Math.min()\`을 통해 작은 값으로 dp 배열을 최신화 시켜준다.