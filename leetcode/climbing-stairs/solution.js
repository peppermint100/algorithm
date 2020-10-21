var answer = 0
var climbStairs = function(n) {
    if(n === 0) return 0
    if(n === 1) return 1
    let sum = 0
    
    takeSteps(sum, n)
    
    return answer
};

var takeSteps = (sum, match) => {
    if(sum === match){
        answer+=1
        return;
    }; 
    if(sum > match){
        return;
    }
    
    takeSteps(sum+1 , match)
    takeSteps(sum+2 , match)
}
