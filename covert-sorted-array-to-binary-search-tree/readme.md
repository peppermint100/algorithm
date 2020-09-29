## Problem
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

```
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```


## Approach
처음엔 dfs나 순회방법을 생각했는데 문제에 힌트가 있었다. 배열을 이분탐색하여 순서대로 node에 재귀적으로 넣어주면
해결된다. 이분탐색을 사용하여 각 계산마다 계산해야하는 양이 반 씩 줄어드므로 시간복잡도는 O(logN)이고 공간복잡도는 
트리의 높이인 O(h)이다.