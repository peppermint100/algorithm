class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length;i++){
            Integer target = hashMap.get(nums[i]);
            if(target != null){
                hashMap.put(nums[i], target + 1);
            }else{
                hashMap.put(nums[i], 1);
            }
        };
        
        
        for(int j=0; j<nums.length;j++){
            Integer freq = hashMap.get(nums[j]);
            if(freq == 1){
                return nums[j];
            }
        }
        
        return 0;
    };
}