
var containsDuplicate = function(nums) {
    const hashMap = {}
    for(let i=0; i<nums.length; i++){
        if(typeof hashMap[String(nums[i])] === "undefined" ){
           hashMap[String(nums[i])] = 1 
        }else{
            hashMap[String(nums[i])] += 1 
        }
    }
    console.log(hashMap)
    for(let j in hashMap){
        if(hashMap[j] >= 2){
            return true
        }
    }
    
    return false
};