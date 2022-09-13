def solution(s):
    s = list(s)
    st = ""
    answer = ""
    n_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    while s:
        c = s.pop(0)

        if c.isalpha():
            st+=c
            if st in n_list:
                answer+=str(n_list.index(st))
                st=""
        else:
            answer+=c


    return int(answer)
