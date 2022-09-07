import sys

s1 = 'beakjoon'
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans = [0] * 26

for s in s1:
    target_index = a.index(s)
    new_ans = ans[target_index] + 1
    ans[target_index] = new_ans

print(*ans)
