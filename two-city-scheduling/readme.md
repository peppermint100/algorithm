## 문제
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

## 풀이 전략
costs 배열 요소의 차를 구해서 차를 토대로 정렬하면 A 또는 B로 보낼 때의 이득이
얼마나 큰지 알 수있다. 정렬된 배열의 앞 부분을 한 도시로 또 나머지 뒷 부분을 다른
도시로 보내면 된다.