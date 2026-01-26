n = int(input())
lst = [int(i) for i in input().split()]
st = set()
flag = False
count = 0
for i in lst:
    if i not in st:
        st.add(i)
    else:
        flag = True
        count+=1
        lol = i
sum1 = n*(n-1)//2
if count>1:
    print('cslnb')
    quit()
if not flag:    
    if (sum(lst)- sum1)% 2 == 0:
        print('cslnb')
    else:
        print('sjfnb')
else:
    if (lol-1) in lst or lol == 0:
        print('cslnb')
    else:
        if (sum(lst)- sum1)% 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')
