class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if (x < 0) {
            return false
        }

        let sx = String(x)
        let sxr = String(sx.reversed())
        
        return sx == sxr
    }
}