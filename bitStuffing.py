data = input()

ans = ""

c = 0
for i in data:
    if i == '1':
        c += 1
    else:
        c = 0
    ans += i
    if c == 5:
        ans += '0'
        c = 0 

print(ans)
