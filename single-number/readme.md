## Problem
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

## complexity
```java
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
``이
는
nums.length만 큼의 계산이 두 번 일어나므로 시간복잡도는 O(2N) 즉 O(N)이다. 
공간 복잡도는 nums 만큼의 해쉬 맵이 필요하므로 공간 복잡도 역시 O(N)이다.
