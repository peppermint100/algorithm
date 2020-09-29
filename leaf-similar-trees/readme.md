## Problem
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

## Approach
스택을 통한 DFS로 트리를 순회한다. 순회하면서 노드가 left child와 right child를 동시에 갖지 않으면
그 노드가 leaf노드이므로 leaf 노드의 value를 배열에 담아서 리턴해주는 helper함수를 만든다.  

그리고 두 트리를 helper함수를 통해 리프만 뽑아서 비교를 한다.

자바스크립트에서 배열이 같은지 비교하는 방법은 reduce를 사용하는 방법이 있고 간단하게
JSON.stringfy를 사용하는 방법이 있다.