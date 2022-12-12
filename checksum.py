a = list(map(int,list(input())))
b = list(map(int,list(input())))

n = len(a)
res = [0 for i in range(len(a))]

c = 0

for i in range(n - 1, -1, -1):
    add = a[i] + b[i] + c 
    res[i] = add % 2
    c = add // 2

if c == 1:
    for i in range(n - 1, -1, -1):
        add = res[i] + c 
        res[i] = add % 2
        c = add // 2

for i in res:
    print(int(not i), end = "")
