A = input().lower()
B = input().lower()

if A == B:
    print(0)
elif A < B:
    print(-1)
elif B < A:
    print(1)