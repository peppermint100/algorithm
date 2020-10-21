var canCompleteCircuit = function (gas, cost) {
    for (let i = 0; i < gas.length; i++) {
        let tank = 0
        let possible = true
        for (let j = i; j < gas.length + i; j++) {
            let current = j % gas.length
            tank = tank + gas[current] - cost[current]
            if (tank < 0) {
                possible = false
                break
            }
        }
        if (possible) {
            return i
        }
    }
    return -1
};