## Problem 
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

## Approach
1. List 보다 Set 구조가 contains 메소드의 복잡도 효율이 좋으므로 Set 으로 변경해준다(List로 하면 Time Limit Exceed 에러가 나온다.)
2. 큐를 지정하고 시작단어를 넣는다.
3. 큐에서 하나 씩 빼가면서 단어를 char array로 만들고 char array의 맨 처음부터 아스키코드를 이용하여 한 단어씩 바꿔가며 바꾼 단어가 endWord에 있다면 리턴하고 그게 아니면 wordList에 있는 단어인지 확인하고 있다면 다음 비교를 위에 큐를 넣고 둘다 아니라면 contiune한다.


