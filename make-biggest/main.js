var number = "1231234"
var k = 3

function solution(number, k) {
    var answer = ''
    var lengthofreturnvalue = number.length - k
    console.log(lengthofreturnvalue)
    let list = number.split("").map(x => parseInt(x))
    console.log(list)
    while (answer.length !== number.length - k) {
        let biggest = Math.max(...list.slice(0, -(lengthofreturnvalue - 1)))
        console.log('biggest : ', biggest)
        answer = answer.concat(biggest.toString())
        console.log("answer : ", answer)
        list.splice(list.indexOf(biggest), 1)
        lengthofreturnvalue--
        console.log("left ", list)
    }
    console.log(answer)
}

// console.log(solution(number, k))
solution(number, k)
console.log([1, 2, 3, 4, 5].slice(0, -2))
