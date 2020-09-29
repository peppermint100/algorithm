## Problem
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.


## Approach
키는 내림차순, 그리고 앞의 있는 사람 수(k)는 오름 차순으로 정렬한다.
```javascript
  const constraint = ([h1, k1], [h2, k2]) =>{
        if(h1 !== h2) return h2-h1
        else if(k1 !== k2) return k1 - k2
    }
people.sort(constraint)
```
그 후 빈 배열을 선언하여 전략에 따라 맞는 자리에 하나씩 넣어준다.  
정렬된 배열을 탐색하며 앞에 있는 사람수와 같은 인덱스에 넣어주면 된다.  
키가 내림차순으로 정해져 있기 때문에 앞에 있는 사람 수는 계속해서 그 인덱스의 위치와 같다.
