## 문제
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

## 풀이 전략
주어진 배열에서 가장 큰 두 수를 뽑고 두 수가 같지 않다면 큰 값에서 작은 값을 뺄셈하여 stones 배열에 추가한다. 이 과정이 stones의 배열 길이가 1보다 클 동안 while문을 통해 반복하고 마지막에 stones에 하나도 남지 않으면 0, 남으면 가장 첫 번째 인덱스를 반환한다.