
var findContentChildren = function (g, s) {
    // g = children
    // s = cookies
    let contentChildren = 0;
    let i = 0
    let j = 0
    g.sort((a, b) => a - b)
    s.sort((a, b) => a - b)

    while (j <= s.length) {
        if (g[i] <= s[j]) {
            contentChildren++
            i++
            j++
        } else {
            j++
        }
    }

    return contentChildren
};