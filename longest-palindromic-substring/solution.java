class Solution {
    public String longestPalindrome(String s) {
        String max = "";
        
        int start = 0;
        int end = 0;
        
        for(int i=0; i<s.length(); i++){
            int len1 = checkPalin(s, i, i);
            int len2 = checkPalin(s, i, i+1);
            
            int len = Math.max(len1, len2);
            start = i - (len-1)/2;
            end = i + (len)/2 + 1; 
            
            if(max.length() < len){
                max = s.substring(start, end);
            }
        }
        
        return max;
    }
    
    public int checkPalin(String s, int left, int right){
       if(s == null || left > right){
           return 0;
       } 
       while(left >= 0 &&  right <s.length() && s.charAt(left) == s.charAt(right)){
          left--;
          right++;
       }
        return right - left - 1;
    }
}