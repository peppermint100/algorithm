var lemonadeChange = function (bills) {
    let five = 0
    let ten = 0

    for (x of bills) {
        if (x === 5) {
            five++
        } else if (x === 10) {
            if (five > 0) {
                five--
                ten++
            } else {
                return false
            }
        } else {
            if (five > 0 && ten > 0) {
                five--
                ten--
            } else if (five >= 3) {
                five -= 3
            } else {
                return false
            }
        }
    }
    return true
};