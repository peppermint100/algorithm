var balancedStringSplit = function (s) {
    const list = s.split("")
    let answer = 0
    let match = 0
    for (x of list) {
        if (x === "L") {
            match += 1
        } else {
            match -= 1
        }

        if (match === 0) {
            answer += 1
        }
    }

    return answer
};