n , s = map(int , input().split())
lst = []
for i in range(n):
    lst.append(list(map(int , input().split())))
lst = sorted(lst , key =lambda x : x[0] , reverse = True)
prev , ans = s , 0
for i in range(n):
    ans += prev -lst[i][0]
    if ans < lst[i][1]:
        ans += (lst[i][1]- ans)
    
    prev = lst[i][0]
print(ans+prev)