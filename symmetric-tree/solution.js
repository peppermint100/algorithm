
var iterative = (root) =>{
    if(!root) return true
    
    const t1 = [root.left]
    const t2 = [root.right]
    
    
    while(t1.length > 0 && t2.length > 0){
        const leftVal = t1.shift()
        const rightVal = t2.shift()

        if(!leftVal && !rightVal) continue 
        if(!leftVal || !rightVal || leftVal.val !== rightVal.val) return false
        
        t1.push(leftVal.left)
        t1.push(leftVal.right)
        t2.push(rightVal.right)
        t2.push(rightVal.left)
    }
    
    return true
};


var checkSym = (left, right) =>{
        if(left === null || right === null) return left === right
       return (left.val == right.val) && checkSym(left.left, right.right) && (checkSym(left.right, right.left))
    }

var recursive = function(root) {
    return checkSym(root, root)
};