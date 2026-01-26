N = int(input())
m1 = []
m2 = []
ms = []
for n in range(N):
    m1.append(input())
for n in range(N):
    m2.append(input())

ms = [
    m2,
    [x[::-1] for x in m2],
    [x for x in reversed(m2)],
]

a = []
for m in ms:
    a.append(m)
    a.append([x[::-1] for x in reversed(m)])
    a.append([''.join(m[j][i] for j in range(N - 1, -1, -1)) for i in range(N)])
    a.append([''.join(m[j][i] for j in range(N)) for i in range(N - 1, -1, -1)])

ms = a
print(['NO', 'YES'][m1 in ms])
