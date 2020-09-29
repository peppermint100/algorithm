var BFS = function(employees, id) {
    let value = 0
    const queue = []
    
    for(let i = 0; i < employees.length; i++){
        if(employees[i].id !== id) continue 
        queue.push(employees[i])
        value = value + employees[i].importance
    } 
    
    while(queue.length){
        const node = queue.shift()
        if(!node) continue
        const size = node.subordinates.length
        for(let i = 0; i < size; i++){
            const empSize = employees.length
            for(let j = 0; j < empSize; j++){
                if(node.subordinates[i] == employees[j].id){
                    queue.push(employees[j])
                    value = value + employees[j].importance
                }
            }
        }
    }
    return value
};
var value = 0

var DFS = function(employees, id) {
    const size = employees.length
    let start = null
    for(let i = 0; i < size; i++){
       if(employees[i].id == id){
           start = employees[i].id
       } 
    }
    if(!start) return 0 
    
    importanceHelper(start, size, employees)
    
    return value
};

var importanceHelper = (id, size, employees) =>{
    let node = null
    for(let i = 0; i < size; i++){
       if(employees[i].id == id){
            node = employees[i]
       } 
    }
    if(!node) return
    
    value = value + node.importance        
    
    for(let j = 0; j < node.subordinates.length; j++){
        importanceHelper(node.subordinates[j], size, employees)
    }
}