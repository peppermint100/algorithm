class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        var arr: [[String]] = strs.map { Array($0).map { String($0) } }
        var result = ""

        let minString = strs.min { $0.count < $1.count }
        let minLen = minString!.count

        for i in 0..<minLen {
            var cur = ""
            for s in arr {
                let idx = s.index(s.startIndex, offsetBy: i)
                let c = String(s[idx])

                if cur.isEmpty {
                    cur = c
                } else {
                    if cur != c {
                        return result
                    }
                }
            }

            result += cur
        }
        
        return result
    }
}
