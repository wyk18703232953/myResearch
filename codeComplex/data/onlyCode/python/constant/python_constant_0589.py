q = int(input())
a,s = map(int,input().split())
if ((a+s-2)<=(q+q-a-s)):
    print("White")
else:
    print('Black')
