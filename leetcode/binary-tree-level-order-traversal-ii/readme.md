## Problem 
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

## Apporoach
마지막 리프부터 거꾸로 순회할 필요 없이 자바스크립트의 reverse를 사용하면 간단하게 해결이 가능했다.
트리를 루트부터 하나씩 순회하며 같은 높이에 있는 노드들을 한 배열에 묶어서 넣고 마지막에 reverse 메소드
를 통해 해결했다.