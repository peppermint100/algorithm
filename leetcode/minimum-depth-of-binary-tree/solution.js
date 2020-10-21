var minDepth = function(root) {
    if(!root) return 0
    let curr = 0
    const queue = [root]
    
    while(queue.length){
        const size = queue.length 
        curr++
        
        for(let i = 0; i < size; i++){
            const node = queue.shift()
            if(!node) continue    
            if(!node.left && !node.right){
                return curr
            }else{
                if(node.left) queue.push(node.left) 
                if(node.right) queue.push(node.right)
            }
            
        }
        
    }
};