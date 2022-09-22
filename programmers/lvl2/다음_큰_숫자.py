def solution(n):
    noo = get_number_of_one(get_bin_of(n))
    for i in range(n+1, 1000000):
        c_bin = get_bin_of(i)
        if get_number_of_one(c_bin) == noo:
            return i 

def get_bin_of(n):
    return bin(n)[2:]

def get_number_of_one(n):
    count = 0
    for i in n:
        if i=="1":
            count+=1
    return count
    