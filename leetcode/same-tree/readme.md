## Problem
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

## Approach
1. 두 트리의 첫 번째 노드의 val이 같은 지 확인한다.
2. 같다면 왼쪽 자식이 있는지 확인하고 있다면 각 왼쪽 자식이 같은지 확인한다. 오른쪽 자식에도 똑같이 한다.
3. 노드의 val이 null이라면 함수를 종료한다.
4. 재귀 실행한다.

