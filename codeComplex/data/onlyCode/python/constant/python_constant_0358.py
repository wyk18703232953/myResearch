n = int(input())
d = {'red':'Reality', 'purple': 'Power', 'yellow':'Mind', 'orange':'Soul','blue':'Space','green':'Time'}
stones = ['Reality', 'Power', 'Mind', 'Soul', 'Space', 'Time']
st=[]
for _ in range(n):
    st.append(d[input()])
b=[]
for a in stones:
    if a not in st:
        b.append(a)
print(len(b))
for k in b:
    print(k)