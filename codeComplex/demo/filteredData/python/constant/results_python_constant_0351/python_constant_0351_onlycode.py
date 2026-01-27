
d = {"purple":"Power", "green":"Time", "blue":"Space","orange":"Soul", "red":"Reality","yellow":"Mind"}

i = int(input())
l = []
for x in range(i):
    d.pop(input())

print(len(d))
for i in d.values() : print(i)