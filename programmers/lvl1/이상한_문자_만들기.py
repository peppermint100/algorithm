
def solution(s):
    answer = ''

    t_list = s.split(" ")

    for i in range(len(t_list)):
        c = t_list[i]
        nw = ""
        for j in range(len(c)):
            if j%2==0:
                nw+=c[j].upper()
            else:
                nw+=c[j].lower()
        t_list[i] = nw

    return " ".join(t_list)
