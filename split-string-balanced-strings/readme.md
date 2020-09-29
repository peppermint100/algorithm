## 문제
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

## 풀이 전략
문자열을 배열로 변경하고 0번 인덱스부터 훑으며 만약 L이 나오면 match를 1 증가시키고 R이 나오면 match를 1 감소시킨다.
그리고 매번 match를 확인하여 match가 0이 되면 지금까지 읽은 문자열들이 balanced되었다는 의미이므로 answercounter에 1을 더한다.
