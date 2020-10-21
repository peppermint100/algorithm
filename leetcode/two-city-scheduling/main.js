
var twoCitySchedCost = function (costs) {
    let total = 0
    let len = costs.length
    let i = 0
    let sortedCosts = costs
    for (x of costs) {
        x.push(x[0] - x[1])
    }

    costs.sort((a, b) => a[2] - b[2])
    for (i; i < len; i++) {
        if (i < len / 2) {
            total = total + costs[i][0]
        } else {
            total = total + costs[i][1]
        }
    }
    return total
}