bs = int(input('bucket size: '))
ogs = int(input('outgoing size: '))
n = int(input('no of frame: '))
ins = int(input('incoming packet size: '))

s = 0
for i in range(n):
    if ins <= bs - s:
        s += ins
    else:
        print("packet loss ",(ins - (bs - s)))
        s = bs 
    print("bucket buffer size is ",s," out of ",bs)
    s -= ogs
    print('after outgoing: bucket buffer size is ',s, " out of ", bs)
