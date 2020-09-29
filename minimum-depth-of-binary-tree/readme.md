## Problem 
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

## Approach
1. BFS로 한 층을 전부 순회할때마다 현재 높이를 1씩 증가시켜 현재 높이를 
측정하며 순회한다.
2. 만약 left child와 right child를 모두 가지지 않은 노드에 다다른다면 그 노드가 최소 높이를 가진
노드이므로 바로 현재 높이를 반환한다.