## Problem
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

## Approach
b 배열을 순회하며 b[i]보다 큰 원소중 가장 작은 값을 a배열의 i 인덱스에 위치시킨다.

## First Try
```javascript
var advantageCount = function(A, B) {
    const answer = []
    for(let i = 0; i < B.length; i++){
        let arr = []
        for(let j = 0; j < A.length; j++){
            if(B[i] < A[j]){
                arr.push(A[j])
            }
        }
        if(arr.length == 0){
            answer.push(Math.min(...A))
            A.splice(A.indexOf(Math.min(...A)) ,1)
            
        }else{
            arr.sort((a, b) => a - b)
           answer.push(arr[0])
            A.splice(A.indexOf(arr[0]) ,1)
        }
        arr = [] 
    }
    return answer
};
```
답은 맞지만 역시 time limit exceed 오류가 생긴다. 더 좋은 알고리즘이 필요하다.

## Second Approach
1. A의 가장 작은 값과 B의 가장 작은 값을 비교한다.
2. 만약 A가 더크면 B와 같은 인덱스에 그 값을 삽입한다.
3. 만약 B가 더크면 그 A는 어떤 B 원소보다도 작으므로 B 원소중
가장 큰 값의 인덱스에 삽입한다.
4. 이렇게 하면 반복문을 한 번만 써도 된다.