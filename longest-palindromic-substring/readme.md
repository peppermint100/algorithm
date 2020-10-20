## Problem
Given a string s, return the longest palindromic substring in s.

## Approach
1. 문자열을 처음부터 하나씩 루프를 돌며 palindromic을 만족하는지 체크한다.  
2. 체크하는 방법은 그 인덱스의 문자를 가운데로 지정하고 left와 right를 하나씩 줄이고 늘려가며 palindromic을 만족하지 않을 때 까지 늘려서 만족하는 길이를 반환하는 메소드를 만들어준다.
3. 메인 메소드에서 길이를 중심으로 현재 인덱스를 통해 그 길이가 max 보다 크다면 max를 바꿔준다.

## 주의할 점
indexOutOfRange 에러가 많이 발생할 수 있고 "racecar" 에러를 잡아주어야 한다. "racecar" 에러란 예를 들면 "abba"는 전형적인 palindromic인데 racecar의 경우에는 e가 양쪽으로 같지 않으면서 palindromic을 만족한다. 따라서 두 가지 경우를 모두 체크해주어야 한다.