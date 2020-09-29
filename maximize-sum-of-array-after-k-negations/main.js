var largestSumAfterKNegations = function (A, K) {
    let i = 0
    let answer = 0
    while (i < K) {
        i++
        let j = 0
        let min = Math.min(...A)
        let idx = A.indexOf(min)
        A[j] = -A[j]
    }

    for (x of A) {
        answer += x
    }

    return answer
};;