var BFS = function(root) {
    if(!root) return 0;
    
    const queue = [root]
    let height = 0

    while(queue.length){
        const size = queue.length
        for(let i = 0; i < size; i++){
            const node = queue.shift()
            for(let j = 0; j < node.children.length; j++){
                queue.push(node.children[j])
            }    
        }
        height++
    }

    return height
} 

var max_depth = 0;
var DFS = function(root) {
    if(root == null) return 0
    getMaxDepth(root, 1)
    return max_depth
} 

var getMaxDepth = (node, depth) => {
    if(node == null) return
    max_depth = Math.max(depth, max_depth)
    for(let i = 0; i < node.children.length; i++){
       getMaxDepth(node.children[i], depth + 1) 
    }
}
    