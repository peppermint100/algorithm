## problem
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

## Approach
가장 높은 무게를 가진 사람과 가장 낮은 무게를 가진 사람의 무게를 합치고
limit와 비교하여  
limit 보다 작으면 함께 보트에 태워서 보내고  
limit 보다 높으면 가장 높은 무게를 가진 사람만 보낸다.  
이 작업을 people.length가 0이 될 때 까지 반복한다.

## Case 1

```javascript
var numRescueBoats = function(people, limit) {
    let boats = 0
    while(people.length > 0){
        if(people.length === 1){
            boats++
            break;
        }
        const max = Math.max(...people)
        const min = Math.min(...people)

        if(max + min <= limit){
           people.splice(people.indexOf(max), 1) 
           people.splice(people.indexOf(min), 1) 
           boats++
        }else{
           people.splice(people.indexOf(max), 1) 
           boats++
        }
    }

    console.log(boats)
};

```
처음에 생각해 낸 알고리즘 대로 작성을 하니 leetcode에서 time limit exceed가 떠서
people을 정렬해서 제출했더니 통과했다.

