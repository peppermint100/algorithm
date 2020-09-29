var iterate = function(root) {
    if(!root) return 0
    
    let stack = [root]
    let depth = 0;
    
    while (stack.length !== 0) {
        let temp = [];
        
        while (stack.length !== 0) {
            let node = stack.pop();
            
            if (node.left) 
                temp.push(node.left);
            
            if (node.right) 
                temp.push(node.right);
        }
        stack = temp 
        depth++
    }
    
    return depth;
}

var recursive = (root) =>{
    var depth = 0
    if(!root) return 0;
    if(root.length === 1) return 1;
    
    maxDepthHelper(root, 1)
    
    return depth
}

var maxDepthHelper = (node, currDepth) =>{
    if(!node) return    
    
    depth = Math.max(depth,  currDepth)
    
    if(node.left) maxDepthHelper(node.left, currDepth + 1)
    if(node.right) maxDepthHelper(node.right, currDepth + 1)
}

var sexyRecursive = function(root) {
    if (root === null) return 0
    return Math.max(sexyRecursive(root.left), sexyRecursive(root.right)) + 1
};



