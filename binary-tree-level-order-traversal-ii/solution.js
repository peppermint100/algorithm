var levelOrderBottom = function(root) {
    if(!root) return []
    const queue = [root]
    const arr = [[root.val]] 
    while(queue.length > 0){
        const size = queue.length
        const cousins = []
        
        for(let i = 0; i < size; i++){
            const node = queue.shift()  
            if(!node) continue
            if(node.left) {
                cousins.push(node.left.val)
                queue.push(node.left)
            }
            if(node.right){
              cousins.push(node.right.val)  
                queue.push(node.right)
            } 
        }
        if(cousins.length > 0){
            arr.push(cousins)
        }
    }
    
    return arr.reverse()
};