var titleToNumber = function(s) {
    const arr = s.split("")
    const size = arr.length
    let answer = 0
    
    for(let i=0; i<arr.length; i++){
        const pow = size - (i + 1)
        const payload = calc(arr[i]) * Math.pow(26, pow) 
        answer+=payload
    }
    
    return answer
};

var calc = (s) => {
    return s.charCodeAt(0) - 64
}