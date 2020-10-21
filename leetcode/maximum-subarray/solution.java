class Solution {
    public int maxSubArray(int[] nums) {
       if(nums.length == 0) return 0;
       if(nums.length == 1) return nums[0];
        
       int max = nums[0];
       
       for(int i=1; i<nums.length; i++){
           nums[i] = Math.max(nums[i], nums[i-1] + nums[i]);
           max = Math.max(nums[i], max);
       }
       
       return max;
    }
}