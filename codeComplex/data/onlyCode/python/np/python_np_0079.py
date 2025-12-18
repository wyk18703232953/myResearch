import math

sent = input()
received = input()

sp = sent.count('+')
sm = sent.count('-')
rp = received.count('+')
rm = received.count('-')
quest = received.count('?')
# Then deal with the ? message
dist = sp - rp

if dist < 0 or dist > quest:
    print(0)
elif dist == 0 and quest == 0:
    print(1)
else:
    total = 2 ** quest
    possible = math.factorial(quest) / math.factorial(dist) / math.factorial(quest-dist)
    print(possible/total)
