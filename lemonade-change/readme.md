## 문제 
At a lemonade stand, each lemonade costs $5. 

Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).

Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Return true if and only if you can provide every customer with correct change.

## 풀이 전략
five, ten 변수를 0으로 선언하고 bills를 for of 문으로 순회하며 5달러 짜리라면
five에 1을 더하고 10달러라면 five 변수를 확인하여 five가 1 이상이면 five를 1 감소시켜 거슬러준다. 20달러짜리라면 five 3개 또는 ten 1개, five 1개로 거슬러준다
twenty는 거슬러줄일도 셀 필요도 없으므로 무시해도 된다.

<strong>단 20달러를 받았을 때 10달러를 먼저 소진하도록 해야만 통과가 가능하다.</strong>