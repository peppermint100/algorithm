

var isSameTree = function(p, q) {
    if(!p && !q) return true
    if(!p || !q) return false
    
    return helper(p, q)
};

var helper = (p, q) => {
    if(!p && !q) return true 
    if(!p || !q) return false
    if((p && q) && p.val !== q.val) return false
    
    return helper(p.left, q.left) && helper(p.right, q.right)
}