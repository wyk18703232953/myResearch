mecces, burgerKing, both, groupSize = map(int,input().strip().split(' '))
mecces -= both
burgerKing -= both
notPassed = groupSize - sum((mecces,burgerKing,both))
if notPassed > 0 and burgerKing >= 0 and mecces >= 0:
    print(notPassed)
else:
    print(-1)