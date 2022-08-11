[문제링크](https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true)

Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.


문제는 City의 length가 가장 긴 곳, 가장 짧은 곳을 쿼리하면 되고 City Length가 동일한 곳에서는 알파벳 순으로
뽑으면 된다고 한다.

또 문제의 Note에 single query가 아니라 two seperate queries 도 허용한다 하여 간단히 order by 만을 이용하여 문제를
풀었다.

```sql
select * from (select s.city, length(s.city)
from station s
order by length(s.city), s.city asc) as a limit 1;


select * from (select s.city, length(s.city)
from station s
order by length(s.city) desc , s.city asc) as a limit 1;
```

너무 간단해서 풀고 구글링하여 더 좋은 방법이 있나 찾아봤지만 딱히 눈에 들어오는 방법은 없었다



