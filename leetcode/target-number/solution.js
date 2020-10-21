var answer = 0;

function solution(numbers, target) {
    const sum = numbers.reduce((acc, curr) => acc + curr)
   if(sum < target) return 0;
   
    for(let i = 0; i < numbers.length; i++){
        numbers[i] = -numbers[i]
        helper(numbers, target, i)
        numbers[i] = -numbers[i]
    }
    
    return answer
}

var helper = (numbers, target, idx) => {
    const sum = numbers.reduce((acc, curr) => acc + curr)
   if(sum == target) answer++
   else if(sum > target){
       for(let i = idx + 1; i < numbers.length; i++){
         numbers[i] = -numbers[i]
        helper(numbers, target, i)
        numbers[i] = -numbers[i]  
       }
   }
}
