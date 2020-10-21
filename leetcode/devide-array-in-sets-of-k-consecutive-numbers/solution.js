var isPossibleDivide = function(nums, k) {
    // impossible 
    if(nums.length % k !== 0){
        return false
    }
    const counts = {}
    
     for (const n of nums) {
    counts[n] = counts [n] || 0;
    counts [n]++;
  }
    const roots = [];
      for (const n of nums) {
        if (!counts[n - 1]) {
          roots.push(n);
        }
      }

    
    while(roots.length > 0){
        const r = roots.pop()
        if(!counts[r]){
            continue
        }
        
        for(let i = r; i <= r + k; i++){
            if(i < r + k){
            if(!counts[i]){
                return false
            }
            counts[i]--
            }
            
            if(counts[i] && !counts[i-1]){
            roots.push(i)
            }
        }
        
    }
    return true;

};