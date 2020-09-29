var reconstructQueue = function (people) {
    const constraint = ([h1, k1], [h2, k2]) => {
        if (h1 !== h2) return h2 - h1
        else if (k1 !== k2) return k1 - k2
    }
    people.sort(constraint)
    const answer = []
    for (let i = 0; i < people.length; i++) {
        answer.splice(people[i][1], 0, people[i])
    }
    return answer
};

