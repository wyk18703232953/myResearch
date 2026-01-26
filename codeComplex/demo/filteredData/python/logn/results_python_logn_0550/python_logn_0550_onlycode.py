k = int(input())
prev=0
next=0
NumofDigits=0
#i = 0
#while(sum<(2^12)):
while(True):
    prev = next
    next = next+(9*(10**(NumofDigits-1))*NumofDigits)
    if(k>= prev and k<=next):
        break
    NumofDigits=NumofDigits+1
if(NumofDigits==1):
    print(k)
else:
    result = (10**(NumofDigits-1))+int((k-(prev+1))/NumofDigits)
    i=0
    while(True):
        if (k-int(prev+1))%NumofDigits == i:
            break
        i=i+1
    result = str(result)
    print(result[i])