var binaryTreePaths = function(root) {
    if(!root) return []
   if(root.length <= 0) return []  
    
   const stack = [root]
   const path = []
   const answer = []
   let currentPath = ""
   while(stack.length){
       const size = stack.length
       const node = stack.pop()
       if(!node) continue 
       if(currentPath.length > 0){
         currentPath = currentPath.concat("->")  
       } 
       currentPath = currentPath.concat(node.val.toString())
         
       if(node.left){
          stack.push(node.left) 
       }
       if(node.right){
          stack.push(node.right) 
       }
       if(node.left && node.right){
          path.push(currentPath) 
       }
       if(!node.left && !node.right){
          answer.push(currentPath)
          currentPath = path.pop() 
       }
   }
    
    return answer
};