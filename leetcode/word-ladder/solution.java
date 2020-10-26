class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        HashSet<String> set = new HashSet<>();
        for(String word : wordList){
            set.add(word);
        }
        if(!set.contains(endWord)){
            System.out.println("break point");
           return 0; 
        }  
        
        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        
        int level = 1;
        
        while(!queue.isEmpty()){
            Integer size = queue.size();
            for(int i=0; i<size; i++){
                String word = queue.poll();
                char[] word_char = word.toCharArray();
                for(int j=0; j<word_char.length; j++){
                    char single_char = word_char[j];
                    for(char compare_char = 'a'; compare_char <= 'z'; compare_char++){
                        if(compare_char == word_char[j]) continue;
                        word_char[j] = compare_char;
                        String converted_word = String.valueOf(word_char);
                        if(converted_word.equals(endWord)){
                            return level + 1;  
                        } 
                        if(set.contains(converted_word)){
                            queue.add(converted_word);
                            set.remove(converted_word);
                        } 
                    }
                    word_char[j] = single_char;
                }               
            }
            level++;
        }
        return 0; 
    }
}
