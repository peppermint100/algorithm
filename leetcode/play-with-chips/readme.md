## 문제
There are some chips, and the i-th chip is at position chips[i].

You can perform any of the two following types of moves any number of times (possibly zero) on any chip:

Move the i-th chip by 2 units to the left or to the right with a cost of 0.
Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
There can be two or more chips at the same position initially.

Return the minimum cost needed to move all the chips to the same position (any position).

## 풀이 전략
짝수 인덱스에 있는 칩들은 모두 비용없이 한 곳에 모을 수 있고   
홀수 인덱스에 있는 칩들은 모두 비용없이 한 곳에 모을 수 있다  
따라서 두 인덱스에 모든 칩들을 비용없이 모으고 그 중 적은 칩이 있는 곳에서
칩이 많은 쪽으로 모두 1의 비용을 들여 옮긴다.