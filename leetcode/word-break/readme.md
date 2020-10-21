# Problem
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

## Approach
- boolean으로 이루어진 dp 배열을 만들고 각 단어의 인덱스에서 word break를 했을 때 만족하는지를 확인하여 true 혹은 false를 dp에 넣는다.
- i를 1부터 시작하고 j는 i-1부터 0까지 진행하며 dp[j]가 true인지 확인한다. 이유는 false일 경우 어차피 그 사잇값들이 wordDict 내에 있는것을 만족하지 않기 때문인다.
- 그리고 j부터 i까지를 substring한 결과가 wordDict내에 있는지 확인한다. 있다면 dp[i]에 true를 넣어서 이 부분에서는 wordDict에서 자를수 있는 값만 있도록 표기한다.
- dp 배열의 마지막 상태를 반환한다.
