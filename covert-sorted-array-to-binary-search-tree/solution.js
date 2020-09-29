var sortedArrayToBST = function(nums) {
    if(!nums || !nums.length) return null 
    
    const mid = Math.floor(nums.length / 2)
    
    const node = new TreeNode(nums[mid])
     
    node.left = sortedArrayToBST(nums.slice(0, mid))
    node.right = sortedArrayToBST(nums.slice(mid+1,nums.length))
   
    return node
};

