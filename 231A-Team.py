n = int(input())

total = 0

for i in range(n):
    z = input()
    if z.count("1") >= 2:
        total = total+1
print(total)