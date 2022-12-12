sendData = list(map(int,list(input())))
revData = list(map(int,list(input())))

sendData = sendData[::-1]

temp = [0,0] + sendData[:1] + [0] + sendData[1:4] + [0] + sendData[4:]

temp[0] = (temp[0] + temp[2] + temp[4] + temp[6] + temp[8] + temp[10]) % 2
temp[1] = (temp[1] + temp[2] + temp[5] + temp[6] + temp[9] + temp[10]) % 2
temp[3] = (temp[3] + temp[4] + temp[5] + temp[6]) % 2
temp[4] = (temp[7] + temp[8] + temp[9] + temp[10]) % 2

print(temp[::-1])

temp = revData[::-1]

r1 = (temp[0] + temp[2] + temp[4] + temp[6] + temp[8] + temp[10]) % 2
r2 = (temp[1] + temp[2] + temp[5] + temp[6] + temp[9] + temp[10]) % 2
r3 = (temp[3] + temp[4] + temp[5] + temp[6]) % 2
r4 = (temp[7] + temp[8] + temp[9] + temp[10]) % 2

errorBit = str(r4) + str(r3) + str(r2) + str(r1)

errorBit = int(errorBit, 2)

if errorBit == 0:
    print("no error")
else:
    print(errorBit)
