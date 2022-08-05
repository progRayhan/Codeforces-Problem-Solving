count = int(input())
for i in range(count):
    word = input()
    if len(word) > 10:
        a = word[0]
        b = str(len(word[1:-1]))
        c = word[-1]
        print(a+b+c)
    else:
        print(word)