var canJump = function (nums) {
    let count = nums.length - 1
    for (let i = (nums.length - 1); i >= 0; i--) {
        if (i + nums[i] >= count) {
            count = i
        }
    }
    return count == 0
};