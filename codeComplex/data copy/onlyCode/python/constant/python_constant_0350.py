dic = {'purple':'Power', 'green':'Time','blue':'Space','orange':'Soul','red':'Reality','yellow':'Mind'}
n = int(input())
a = []
for i in range(n):
    a.append(input())
print(6-len(a))
for i in dic:
    if i not in a:
        print(dic[i])