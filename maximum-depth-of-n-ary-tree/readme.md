## Problem
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

## Approach
1. BFS
- 큐에 root를 넣는다.
- 큐의 사이즈만큼 루프를 돌며 큐의 children을 큐에 넣는다.
- 이 작업이 끝나면 queue안에는 높이가 같은 노드들이 들어있고 이 때 height에 1을 더한다.
- 그 다음 큐의 사이즈만큼 큐를 돌며 큐 내의 chilren들을 또 queue에 넣는다.
- 정해진 큐 사이즈 루프가 끝나면 또 height에 1을 더한다.
- 반복한다.

2. DFS
- max_depth 변수를 지정하고 재귀 함수를 통해 노드의 가장 깊은 곳 까지 내려가며 max_depth를 변화시킨다.
