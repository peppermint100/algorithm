var levelOrder = function(root) {
    if(!root) return []
    const queue = [root]
    const answer = []
    
    while(queue.length){
        const size = queue.length 
        const temp = []
        
        for(let i=0; i<size; i++){
            const node = queue.shift() 
            temp.push(node.val)
            if(node.left) queue.push(node.left)
            if(node.right) queue.push(node.right)
        }
        answer.push(temp)
    }
    
    return answer
};