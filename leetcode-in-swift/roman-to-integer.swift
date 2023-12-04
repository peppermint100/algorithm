class Solution {
    func romanToInt(_ s: String) -> Int {
        var dict: [Character: Int] = [:]
        dict["I"] = 1
        dict["V"] = 5
        dict["X"] = 10
        dict["L"] = 50
        dict["C"] = 100
        dict["D"] = 500
        dict["M"] = 1000

        var result = 0
        var cur = 0
        var list = Array(s)

        while !list.isEmpty {
            let curChar = list.removeFirst()
            let curInt = dict[curChar]!
            if let nextChar = list.first, nextChar != nil,
             let nextInt = dict[nextChar], nextInt != nil,
             curInt < nextInt
              {
                result += nextInt - curInt
                list.removeFirst()
            } else {
                result += curInt
            }
        }

        return result 
    }
}