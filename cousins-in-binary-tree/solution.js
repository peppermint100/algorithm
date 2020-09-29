var isCousins = function(root, x, y) {
    const queue = [root]    
    while(queue.length){
        const size = queue.length
        let findX = false
        let findY = false
        
        for(let i = 0; i < size ; i++){
            const node = queue.shift()
            if(node.left !== null && node.right !== null){
                
            if((node.left.val === x && node.right.val === y)
               || (node.left.val === y && node.right.val === x)
              ) return false
            
            }
            if(node.val === x) findX = true
            if(node.val === y) findY = true
            
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)
            
        }
        
        if(findX && findY) return true
        
    }    
    return false
};
