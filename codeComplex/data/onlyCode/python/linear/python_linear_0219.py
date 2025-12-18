num=int(input())

b=input()

if b=='0' or b=='1':
    print(b)

else:
    s=len(list(filter(lambda x:x=='0',b)))

    print('1'+'0'*s)