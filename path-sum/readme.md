## Problem
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

## Approach
- dfs로 리프에 도달하면 path의 값들을 전부 더해서 비교한다.
```
리프에 도달하면 그냥 sum을 초기화 시키고 다시 0부터 sum을 더했는데 그렇게하면 리프에 도달한 후
바로 다음 깊이 우선 노드를 찾게 되므로 중간 중간 분기점 마다 sum을 저장해주어야 했다.
따라서 분기점, 즉 node.left와 node.right가 모두 존재할 때 stack에 현재 sum값을 저장하고
리프에 도달해서 답이 나오지 않으면 저장된 sum부터 다음 깊이 우선 노드의 val을 더하도록 했다.
```