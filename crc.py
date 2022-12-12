def xor(x, y):
    ans = ""
    for i in range(1, len(x)):
        if x[i] == y[i]:
            ans += '0'
        else:
            ans += '1'
    return ans


def divide(dividend, divisior): 
    n = len(divisior)
    tmp = dividend[:n]
    while n < len(dividend):
        if tmp[0] == '1':
            tmp = xor(tmp, divisior) + dividend[n]
        else:
            tmp = tmp[1:] + dividend[n]
        n += 1
    if tmp[0] == "1":
        tmp = xor(tmp, divisior)
    else:
        tmp = tmp[1:]
    
    return tmp

keys = ["1100000001111", "11000000000000101", "10001000000100001"]

n = int(input())
sendData = input()
revData = input()


key = keys[n - 1]

n = len(key)

tmp = sendData + '0' * (n - 1)

rem = divide(tmp, key)

print(sendData + rem)

check = divide(revData, key)

if(check == '0' * (n - 1)):
    print("no error")
else:
    print("error")
