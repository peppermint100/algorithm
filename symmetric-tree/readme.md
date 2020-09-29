## Problem
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

## Recursive Approach
1. 종료 조건 : 왼쪽 노드가 없거나 오른쪽 노드가 없으면 종료한다. 
2. 재귀 계산은(5 * 4!) 왼쪽노드의 값과 오른쪽 노드의 값을 체크하고 재귀로 돌리는 부분은 왼쪽 노드의 왼쪽, 그리고 오른쪽 노드의 오른쪽,
그리고 오른쪽 노드의 왼쪽, 왼쪽 노드의 왼쪽이 같아야 하므로 이부분들을 재귀함수 처리한다.

## Iterative Approach
1. 큐에 값을 넣고 하나씩 dequeue하며 비교한다.
2. 만약 꺼내진 값들이 전부 null 즉 비었다면 다음 값을 체크하기 위해
continue 처리한다
3. 만약 두 값이 null이 아니라면 값을 비교하고 다르다면 false를 리턴한다
4. 값이 같다면 다음 노드를 확인하기 위해 왼쪽과 오른쪽 비교할 대상에
맞춰서 각각 큐에 enqueue해준다.