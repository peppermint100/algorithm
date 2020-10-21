var hasPathSum = function(root, sum) {
   const stack = [root] 
   const inter = []
   let payload = 0
   
   while(stack.length){
       const node = stack.pop()
       if(!node) continue
       
       payload +=node.val
       
       if(node.left) stack.push(node.left)
       if(node.right) stack.push(node.right)
       
       if(!node.left && !node.right){
           if(payload  === sum) return true 
           payload = inter.pop()
       }
       
       if(node.left && node.right){
           inter.push(payload)
       }
           
   }
   return false     
};
