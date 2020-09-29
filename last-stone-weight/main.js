var lastStoneWeight = function (stones) {
    while (stones.length > 1) {
        let left = Math.max(...stones)
        stones.splice(stones.indexOf(Math.max(...stones)), 1)
        let right = Math.max(...stones)
        stones.splice(stones.indexOf(Math.max(...stones)), 1)

        if (left !== right) {
            stones.push(Math.max(left, right) - Math.min(left, right))
        }
    }

    return stones.length === 1 ? stones[0] : 0
};