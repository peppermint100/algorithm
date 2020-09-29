var advantageCount = function(A, B) {
    const answer = []
    for(let j = 0; j < A.length; j++){
        answer[j] = "occupied"
    }
    const originA = JSON.parse(JSON.stringify(A));
    const originB = JSON.parse(JSON.stringify(B));
    const sortedA = A.sort((a, b) => (a - b))
    const sortedB = B.sort((a, b) => (a - b))
    console.log(sortedA)
    console.log(sortedB)
    // console.log(originA)
    // console.log(originB)

    for(let i = 0; i < A.length; i++){
        if(sortedA[i] > sortedB[i]){
            answer[originB.indexOf(sortedB[i])] = sortedA[i]            
            console.log(answer)
            // answer.splice(B.indexOf(sortedB[i]), 0, sortedA[i])
        }else{
            answer[originB.indexOf(Math.max(...B))] = sortedA[i]            
            console.log(answer)
            // answer.splice(B.indexOf(Math.max(...B)), 0, sortedA[i])
        }
    }
    console.log("answer : ", answer)
};

advantageCount([12,24,8,32],[13,25,32,11])
