## Problem
You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

## Approach

### BFS
1. 시작 점을 찾는다.
2. 시작 점을 큐에 넣고 큐에서 하나 씩 꺼내가며 importance를 더한다.

```javascript
 * function Employee(id, importance, subordinates) {
 *     this.id = id;
 *     this.importance = importance;
 *     this.subordinates = subordinates;
 * }
```

릿코드에서 subordinates가 상위 프로토타입인 Employ를 다시 체이닝하지 않아서
employee를 계속 순환하느라 코드가 길어졌다.

### DFS
1. 시작점을 찾는다.
2. 이 문제의 subordinates가 체이닝을 안하기 때문에 node 자체를 넣는 것이 아니기 때문에
id를 받아서 재귀를 하도록 helper 함수를 만든다ㅣ.

- employ 오브젝트의 subordinates가 체이닝을 하지 않으므로 helper 함수가 id를 받도록하고 매번 employees에서 찾는다.
- size와 employees 자체도 helper함수가 알아야하기 때문에 보기 좋지 않지만 역시 파라미터로 넣어주었다.
- leetcode에 에러인지 아니면 알고리즘을 잘못 짠건지 모르겠는데 leetcode에서 BFS로 태그를 걸어놓은 문제들을 DFS 재귀로 풀면 Run Code 버튼에서는 테스트 케이스가 전부 통과를 하는데 Submit이 되지 않는다. 