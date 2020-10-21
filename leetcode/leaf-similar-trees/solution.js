var leafSimilar = function(root1, root2) {
    return JSON.stringify(findLeaves(root1)) === JSON.stringify(findLeaves(root2))
};

var findLeaves = (root) => {
    if(!root) return []
    
    let stack = [root]
    const arr = []
        
        while(stack.length){
            const node = stack.pop()
            if(!node) continue
            if(node.left) stack.push(node.left)
            if(node.right) stack.push(node.right)
            
            if(!node.left && !node.right) arr.push(node.val)
    }
    
    return arr
}