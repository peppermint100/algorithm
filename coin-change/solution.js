var coinChange = function(coins, amount) {
    let dp = new Array(amount+1)
    dp.fill(amount+1, 0)
    
    dp[0] = 0
    
    for(let i=0; i<dp.length; i++){
        for(let j=0; j<coins.length; j++){
            if(coins[j] <= i){
                dp[i] = Math.min(dp[i], dp[i-coins[j]] + 1)
            }
        }
    }
    console.log(dp)
    
    return dp[amount] >= amount+1 ? -1 : dp[amount] 
    
};