var minDeletionSize = function (A) {
    let D = 0
    for (let i = 0; i < A[0].length; i++) {
        for (let j = 0; j < A.length - 1; j++) {
            if (A[j][i] > A[j + 1][i]) {
                D += 1
                break
            }
        }
    }
    return D
};
