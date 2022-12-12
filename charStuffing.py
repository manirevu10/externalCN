head = input()
tail = input()
data = input()

ans = ""

for i in data:
    if i == head:
        ans += head
    elif i == tail:
        ans += tail
    ans += i 

print(head + ans + tail)
