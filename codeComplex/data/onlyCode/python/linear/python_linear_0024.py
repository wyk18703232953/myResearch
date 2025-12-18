n = int(input())

lst = list(map(int, input().split()))

evens = []
odds = []

for e, x in enumerate(lst):
    if x % 2 == 0:
        evens.append(e + 1)
    else:
        odds.append(e + 1)

if len(evens) < len(odds):
    print(evens[0])
else:
    print(odds[0])
