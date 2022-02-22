
문제

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key column for this table.
Each row of this table contains information about the salary of an employee.


Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null.

The query result format is in the following example.



Example 1:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
Example 2:

Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+


최초에는 원시적으로 생각을 했다. salary를 desc로 2개만 가져와서 asc로 다시 정렬 후 첫 번째거만 가져오되
갯수가 총 갯수가 적으면 null을 리턴하도록 작성을 했다.

```sql
select if(count(*)=1, null, a.salary) as SecondHighestSalary
from
    (
        select e.salary # 300, 200
        from Employee e
        order by e.salary desc
        limit 2
    ) as a
order by a.salary asc
limit 1
```


해당 쿼리는 생각대로 작동하지 않는데 sql에서 if문 안에 count 함수가 작동하지 않는 문제가 있었다.
왜냐하면 if 문은 첫 레코드의 참/거짓 유무를 통해 판단을 하고 바로 값을 리턴하기 때문이었다.

즉 `()` 내 서브쿼리 값이 0이 아니므로 바로 a.salary를 반환해버렸다.

정답은 sql의 offset을 이용하는 것이었다. sql 쓰면서 돈을 버는 개발자가 직업인데, offset 문법을 몰랐다니
맨날 JPA, QueryDSL의 실무 및 일반적인 경우에만 익숙해져 모르는 부분이 많았다.

이렇게 복잡한 쿼리를 만날때마다 해메는 내 모습을 자주 보게 되었어서 sql 문제 풀이를 공부하기로 마음 먹은거긴 하지만..

아래와 같이 distict로 같은 salary를 같는 직원들까지 하나로 뭉쳐서 offset을 지정해주면 통과가 가능하다.
(row의 결과가 하나라면 offset 1은 자동으로 null처리를 해준다.)

```sql
select(
    select distinct e.salary
    from Employee e
    order by e.salary desc
    limit 1 offset 1
) as SecondHighestSalary
```
