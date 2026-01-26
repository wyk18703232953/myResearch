

def totaller(i):
    if i==0:
        return 0
    else:
        total1=totaller(i-1)+ 9*(10**(i-1))*i
        return total1


no_of_digits=int(input())
j=0
for i in range(1,13):
    if no_of_digits>=totaller(i):
        j=i
kth_digit=(no_of_digits-totaller(j))//(j+1)
if(((no_of_digits-totaller(j))%(j+1))!=0):
    answer=str(kth_digit+10**j)
    # print(answer)
    print(answer[((no_of_digits-totaller(j))%(j+1))-1])
else:
    answer=str(kth_digit+10**j-1)
    print(answer[((no_of_digits-totaller(j))%(j+1))-1])
