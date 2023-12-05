class Solution {
    func isValid(_ s: String) -> Bool {
        var arr = [Character]()
        var dict = [Character: Character]()
        dict[")"] = "("
        dict["}"] = "{"
        dict["]"] = "["
        
        for p in s {
            if arr.isEmpty {
                arr.append(p)
                continue
            }

            let next = arr.last!

            if next == dict[p] {
                arr.removeLast()
            } else {
                arr.append(p)
            }
        }

        return arr.count == 0
    }
}