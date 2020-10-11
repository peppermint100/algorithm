var threeSum = function(nums) {
   const answer = []
   nums.sort((a,b) => a - b)
    
   for(let i=0; i<nums.length-2;i++){
       if(i===0 || (i>0 && nums[i] !== nums[i-1])){
           let low = i+1
           let high = nums.length-1
           const sum = 0-nums[i]
           
           while(low < high){
               if(nums[low] + nums[high] === sum){
                   answer.push([nums[i], nums[low], nums[high]])
                   while(low < high && nums[low] === nums[low+1]) low+=1
                   while(low < high && nums[high] === nums[high-1]) high-=1 
                   low+=1
                   high-=1
               }else if(nums[low] + nums[high] > sum){
                   high-=1
               }else{
                   low+=1
               }
           }
       }
   }
   
   return answer
};
