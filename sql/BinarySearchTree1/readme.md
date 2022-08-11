
[문제링크](https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true)
```sql
select N,
    if(P is null, 'Root',
       if (
           N in (select distinct P from bst)
       ,'Inner','Leaf'))
from bst
order by N
```


문제 풀이 핵심은 N 중에서  P가 null 인 경우인 N은 Root,
P안에 없는 N 값이면 Inner, 나머지는 Leaf라는 점을 알면 된다.

패스를 계속 못해서 결국 답을 찾아봤는데, 마지막에 order by n을 붙여주지 않았던 문제 였다.

깔끔한 방법은 CASE WHEN을 이용하는 방식이다.

```sql
SELECT CASE
    WHEN P IS NULL THEN CONCAT(N, ' Root')
    WHEN N IN (SELECT DISTINCT P FROM BST) THEN CONCAT(N, ' Inner')
    ELSE CONCAT(N, ' Leaf')
    END
FROM BST
ORDER BY N ASC
```
