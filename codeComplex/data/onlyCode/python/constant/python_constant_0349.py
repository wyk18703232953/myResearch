lst = []
ans = {'purple' : 'Power', 'green' : 'Time', 'blue': 'Space', "orange" : "Soul", "red" : "Reality", "yellow" : "Mind"}
for i in range(int(input())):
    lst.append(input())
a = []
for i in ans.keys():
    if i not in lst:
        a.append(ans[i])
print(len(a))
for i in a:
    print(i)