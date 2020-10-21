## Problem
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.


## Approach

```
[2,3,1,1,4]
```

1. 맨 마지막 인덱스부터 가장 첫 인덱스까지 순회한다.
2. 순회하며 그 인덱스에서 최대 점프 거리로 Good Index까지 도달할 수 있는지 확인한다.
3. Good Index란 가장 마지막까지 도달하기에 충분한 점프 거리를 가진 인덱스를 말한다.

예를 들면 3번째 인덱스인 1에서 마지막 인덱스인 4까지는 1의 점프 거리로 도달할 수 있다.  
따라서 그 뒤의 인덱스는 3 번째 인덱스까지만 도달할 수 있으면 마지막까지 도달할 수 있으므로  
3번째 인덱스가 Good Index가 된다. 

만약 도달할 수 없는 경우의 인덱스는 일단 넘어가고 그 다음 인덱스가 마지막 Good Index까지  
도달할 수 있는지 보면 된다.  

마지막에 Good Index가 0인지 확인하여 Boolean을 리턴한다.

