
var countPrimes = function(n) {
    const seive = new Array(n).fill(true) 
    let answer = 0
    
    for(let i=0; i<n+1; i++){
        if(i===0 || i===1) continue
        
        for(j=2; i*j<=n; j++){
            seive[i*j] = false
        }
    }
    
    for(let i=2; i<n; i++){
        if(seive[i]){
            answer+=1
        }
    }
    
    return answer
};