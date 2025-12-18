n = int(input())
li1 = []
s=""
li2 = {"purple":"Power", "green":"Time", "blue":"Space", "orange":"Soul", "red":"Reality","yellow":"Mind"}
for i in range(n):
    s = input()
    li1.append(s)
print(6-n)
for key in li2:
    if key in li1:
        continue
    else:
        li1.append(key)
        print(li2[key])