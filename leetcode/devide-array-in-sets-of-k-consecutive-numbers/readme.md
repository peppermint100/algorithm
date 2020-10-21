## Problem
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

## Approach
1. 먼저 counts라는 오브젝트안에 배열의 숫자 빈도수를 저장하는 해시 맵을 구성한다.
2. 2 이상 띄어져 있는 숫자가 있다면 그 숫자는 나눠진 배열의 시작점(root)가 되어야 하므로 roots 라는 배열을 선언해서 전부 넣어준다.
3. roots를 하나씩 빼면서 roots에서 연속으로 이어지는 숫자가 있는지 확인하고
 없으면 false를 리턴한다. 그리고 이어지는 숫자를 확인할 때 그 다음 숫자가 roots의
 조건을 만족하는지 확인하여 roots에 넣어준다.

 (https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/discuss/813175/JavaScript-Short-Video-Explanation-of-Popular-O(N)-Solution)
 