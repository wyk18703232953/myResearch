# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
#
# n = int(input())
#
# if n>3:
#     print(fibo(n-1),fibo(n-3),fibo(n-4))

a = [0,1]
n = int(input())
i=2
r=0
while r<n:
     r = a[i-1]+a[i-2]
     a.append(r)
     i+=1
l = len(a)-1
if n>3:
    print(a[l-4],a[l-3],a[l-1])
elif n==3:
    print(1,1,1)
elif n==2:
    print(0,1,1)
elif n==1:
    print(0,0,1)
elif n==0:
    print(0,0,0)