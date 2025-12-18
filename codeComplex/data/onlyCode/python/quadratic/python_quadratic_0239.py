from os import path
import sys,time, collections as c , math , pprint as p , itertools as it , operator as op
maxx , localsys , mod = float('inf'), 0 , int(1e9 + 7) 
if (path.exists('input.txt')):  sys.stdin=open('input.txt','r') ;   sys.stdout=open('output.txt','w')
input = sys.stdin.readline
n = int(input()) ; s = list(map(int , input().split())) ; c = list(map(int , input().split()))
ans = maxx
for mid in range(1 , n - 1):
    l = [maxx] + [c[i] for i in range(mid) if s[i] < s[mid]]
    r = [maxx] + [c[i] for i in range(mid+1 , n) if s[i] > s[mid]]
    ans = min(ans , min(l) + c[mid] + min(r))
print(ans if ans != float('inf') else -1)














# for _ in  range(int(input())):
#     n = int(input())
#     a , i , j ,ok = [[int(i) for i in input().rstrip('\n')] for _ in range(2)] , 0 , 0 , True
#     while j < n :
#         if a[i][j] > 2:
#             if a[i^1][j] < 3:
#                 break
#             else:
#                 i^=1
#         j+=1
#     print('YES' if i==1 and j == n else 'NO')
#for example suppose if you are at row 1 and standing on the curled tile which will obviously lead to another row
#and if this row has ( | or - ) then obviously you have no other way to move forward
#all other combinations are viable




# n = int(input()) ; g = c.defaultdict(list)
# for _ in range(n-1):
#     u , v = map(int , input().split())
#     g[u].append(v)
#     g[v].append(u)
# v , q  , ans  = [0]*(n+1) , [(1 ,1 ,0)] , 0 #p , cnt , height
# while q :
#     p , cnt , h = q.pop()
#     v[p] , c = 1 , 0
#     for i in g[p]:
#         if not v[i]:
#             c+=1
#     if c == 0 :
#         ans+= cnt*h
#     else:
#         for i in g[p]:
#             if not v[i]:
#                 q.append((i , cnt/c , h+1))
#                 v[i] = 1
#     print(q,ans , p, cnt , h)
# print('%.14f'%(ans))
# #probability of the horse taking the route to each of the child of the parent * length of the journey = expected value for that vertex




# def ok(p , s):
#     cnt , need =0 , 0
#     for i in s:
#         if p[need] == i:
#             cnt+=1 ; need ^= 1
#     if cnt % 2 and p[0] != p[1]:
#         cnt-=1
#     return cnt

# for _ in range(int(input())):
#     s = input().rstrip('\n') ; n , ans = len(s) , maxx
#     for i in range(10):
#         for j in range(10):
#             ans = min(ans , n - ok((str(i) , str(j)), s))
#     print(ans)
#This problem was so easy oh gawd , so you can only make left cyclic shift = right cyclic shift , when there are at most
#2 characters
#(incase of 1 ch) at the same time if total string has only character it is valid no matter how you see it 
#(incase of 2 ch) all the characters at odd positions must be equal , and all the characters at even position must be equal





# n , k = map(int , input().split()) ; s = input().rstrip('\n')
# ans = a = b = j = 0
# for i in range(n):
#     a , b = (a+1 , b) if s[i] == 'a' else (a , b+1 )
#     if min(a, b) > k :
#         a , b = (a -1 , b) if s[j] == 'a' else (a , b -1) ; j+=1
#     else:
#         ans+=1
# print(ans)
# #two - pointer method , if at any point min(a , b )> k then keep on decreasing from the beginning untill and unless you get min(a , b) 
# #less than k