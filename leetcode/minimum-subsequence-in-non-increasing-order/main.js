var minSubsequence = function (nums) {
    let answer = []
    while (sumOfArr(answer) <= sumOfArr(nums)) {
        let max = Math.max(...nums)
        nums.splice(nums.indexOf(max), 1)
        answer.push(max)
    }

    return answer
};

var sumOfArr = (list) => {
    if (list.length <= 0) {
        return 0;
    }
    let sum = 0
    for (x of list) {
        sum += x
    }
    return sum
}