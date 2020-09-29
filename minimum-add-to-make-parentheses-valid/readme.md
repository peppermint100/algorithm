## 문제
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

## 풀이 전략

### first approach
- count 변수를 선언하고 ( 가 나오면 +1 )가 나오면 -1을 하고 count를 절대값 처리하여 리턴
- )))((( 를 처리할 수 없었음

### second approach
- 문자열을 배열화 하고 0번 인덱스 부터 탐색
1. ( 가 나오면 다음 ) 를 찾는다 찾게되면 찾은 )를 배열에서 제거하고 다음 인덱스로 넘어감  
찾지못하면 )를 추가하여 문자를 만들수 있으므로 count에 1을 더함
2. ) 가 나오면 (를 하나 추가하여 문자를 만들 수 있으므로 그냥 count에 1을 더함

