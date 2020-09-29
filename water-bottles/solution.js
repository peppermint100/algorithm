var numWaterBottles = function (numBottles, numExchange) {
    let belly = numBottles

    while (numExchange <= numBottles) {
        belly = belly + parseInt(numBottles / numExchange)
        numBottles = parseInt(numBottles / numExchange) + numBottles % numExchange
    }

    console.log(belly)
};



numWaterBottles(9, 3)

