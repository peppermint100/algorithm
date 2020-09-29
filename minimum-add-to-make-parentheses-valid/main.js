var minAddToMakeValid = function (S) {
    let count = 0;
    const list = S.split("")

    for (let i = 0; i < list.length; i++) {
        count += 1
        if (list[i] === '(') {
            for (let j = i + 1; j < list.length; j++) {
                if (list[j] === ')') {
                    console.log('match found!')
                    list[j] = null
                    count -= 1
                    break;
                }
            }
        } else if (list[i] === null) { // case null
            count -= 1
        }
    }

    return count
};