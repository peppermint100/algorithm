const command = [4, -1, 3]
const obstacles = []
var robotSim = function (commands, obstacles) {
    let pos = [0, 0]
    let xstick = [0, 1, 0, -1]
    let ystick = [1, 0, -1, 0]
    let direction = 0  // 0, 1, 2, 3 length of each stick   

    for (x in commands) {
        if (x === -2) {
            direction = (direction + 1) % 4
        } else if (x === -1) {
            direction = (direction + 3) % 4
        } else {
            for (; x <= 0; x--) {
                let prevPos = pos
                pos[0] += xstick[direction]
                pos[1] += ystick[direction]
                for (y in obstacles) {
                    if (y === pos) {
                        pos = prevPos
                    }
                }
            }

        }
    }
    return Math.pow(pos[0], 2) + Math.pow(pos[1], 2)
};

console.log(robotSim(command, obstacles))