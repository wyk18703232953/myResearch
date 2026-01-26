str1,str2=map(str,input("").split())
lst=[]
lst_ans=[]
l_count=0
count=0
for i in str2:
    if(count<1):
        lst.append(i)
    else:
        break
for i in str1:
    if(count==0):
        lst_ans.append(i)
        count+=1
    elif(ord(i)<ord(lst[0])):
        lst_ans.append(i)
    else:
        lst_ans.append(lst[0])
        break
else:
    lst_ans.append(lst[0])
print(''.join(lst_ans))  