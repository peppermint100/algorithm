## Problem
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

```

## Approach
처음에는 비슷한 easy 문제인 maximun-subarray 처럼 dp 배열을 만들고 최대 곱을 연산하려고 했지만 sum이 음수인 경우와 배열 내 0이 있는 경우를 처리하지 못해서 실패했다.
정답은 곱의 최댓값 그리고 곱의 최솟값 둘을 저장해놓는 것이다. 왜냐하면 배열 값이 0인경우와 음수인 경우가 있기 때문에 만약 최솟값이 음수인데 또 음수를 만나면 굉장히 큰 양수가 되어 최댓값이 될 수가 있기 때문이다. 따라서

1. max, min, answer 값을 전부 배열 첫 번째 값으로 지정한다.
2. max는 배열 현재값, 그리고 max * 배열 현재값, min * 배열 현재값(음수 * 음수를 고려)한 값중 가장 큰 값을 저장한다.
3. min에는 배열 현재값 그리고 min * 배열현재값(음수 * 음수를 고려 ), 그리고 max * 배열 현재값(음수가 될 가능성 그리고 이후 음수 * 음수의 가능성)을 전부 저장한다.
4. max 과 answer 값을 비교하여 가장 큰 값을 계속 갱신한다.
