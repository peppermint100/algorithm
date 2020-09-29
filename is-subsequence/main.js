
var s = "abc"
var t = "ahbgdc"

var isSubsequence = function (s, t) {
    let sList = s.split("")
    let tList = t.split("")
    let i = 0
    let j = 0
    console.log(sList)
    console.log(tList)
    while (j <= tList.length) {
        if (i >= sList.length) {
            return true
        } else if (sList[i] === tList[j]) {
            i++
            j++
        } else {
            j++
        }
    }
    return false
}

console.log(isSubsequence(s, t))
