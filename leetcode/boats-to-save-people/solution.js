
var numRescueBoats = function(people, limit) {
    let boats = 0
    people.sort((a, b) => {
        return a - b
    })
    console.log(people)
    while(people.length > 0){
        if(people.length === 1){
            boats++
            break;
        }
        const max = people[people.length - 1]
        const min = people[0] 

        if(max + min <= limit){
           people.splice(people.indexOf(max), 1) 
           people.splice(people.indexOf(min), 1) 
           boats++
        }else{
           people.splice(people.indexOf(max), 1) 
           boats++
        }
    }

    return boats
};


numRescueBoats(
[44,10,29,12,49,41,23,5,17,26], 50)