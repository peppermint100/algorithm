import Foundation

var arr = [5,7,2,2,3,5,8,9,5,3,12]

func selectionSort(_ arr: inout [Int]) {
    for i in 0..<arr.count {
        var min = i
        for j in i+1..<arr.count {
            if arr[min] > arr[j] {
                min = j
            }
        }
        arr.swapAt(i, min)
    }
    
    print(arr)
}

func insertionSort(_ arr: inout [Int]) {
    for i in 0..<arr.count {
        for j in stride(from: i-1, to: 0, by: -1) {
            if arr[j] < arr[j-1] {
                arr.swapAt(j, j-1)
            }
        }
    }
    
    print(arr)
}

func bubbleSort(_ arr: inout [Int]) {
    for i in 0..<arr.count {
        for j in i..<arr.count {
            if arr[i] > arr[j] {
                arr.swapAt(i, j)
            }
        }
    }
    print(arr)
}

func mergeSort(_ arr: [Int]) -> [Int] {
    if arr.count <= 1 {
        return arr
    }
    
    let mid = arr.count / 2
    return merge(mergeSort(Array(arr[..<mid])), mergeSort(Array(arr[mid...])))
}

func merge(_ left: [Int], _ right: [Int]) -> [Int] {
    var left = left
    var right = right
    var result: Array<Int> = []
    while !left.isEmpty && !right.isEmpty {
        if left[0] < right[0] {
            result.append(left.removeFirst())
        } else {
            result.append(right.removeFirst())
        }
    }
    
    if !left.isEmpty {
        result.append(contentsOf: left)
    }
    
    if !right.isEmpty {
        result.append(contentsOf: right)
    }
    
    return result
}

func quickSort(_ arr: [Int]) -> [Int] {
    guard let pivot = arr.randomElement(), arr.count > 1 else { return arr }
    let left = arr.filter { $0 < pivot }
    let equal = arr.filter{ $0 == pivot }
    let right = arr.filter { $0 > pivot }
    
    return quickSort(left) + equal + quickSort(right)
}


