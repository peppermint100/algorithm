## Problem
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

## Approach 
동적 프로그래밍을 활용한다. dp array를 따로 만들지 않고 주어진 배열에서
직접 배열을 순회하며 전 원소와 현재 원소를 합친 값과 현재 원소의 값을 비교하여 어떤 값이 더 큰지 확인하고 그 값을 따로 글로벌한 max값과 같은지
비교한다.

## Complexity
시간 복잡도는 nums에 비례하므로 O(N)이고 공간복잡도 역시 nums에
비례하므로 O(N)이다.
