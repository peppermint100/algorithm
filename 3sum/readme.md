## Problem
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

## Apporoach
이 문제에서 주의할 점은 중복되는 원소가 있어서 같은 sum이 존재할 경우 제외해
주어야 한다는 점이다. 따라서 다음과 같은 문제 풀이 전략을 세운다.

1. 배열을 오름차순으로 정렬하고 for문으로 처음부터 루프를 돈다.
2. 어차피 3개를 중복되지 않게 선택하므로 nums.length - 2까지만 루프를 돈다.
3. 현재 인덱스에서 남은 부분들을 가지고 two sum 알고리즘을 만들어서 현재 인덱스의 값과 비교하여 맞는 triplet인지 확인한다.
4. 단 현재 인덱스와 이전 인덱스의 값이 같으면 중복된 결과가 나올수 있으므로 다음 인덱스로 넘어가 준다.  
5. 오름차순으로 정렬하였기 때문에 low와 high 인덱스를 정하여 sum 값과 비교하여 계산을 효율적으로 할 수 있게 한다.
