import bisect
xyz=[9,90,900,9000,90000,900000,9000000,90000000,900000000,9000000000,900000000000]
xzy=[10,190,2890,38890,488890,5888890,68888890,788888890,8888888890,98888888890,1088888888890,11888888888890]
count=2
k=int(input())
digits=bisect.bisect_left(xzy,k)
#print('d',digits)
if k==10:
    print(1)
elif k>10:
    apu=k-xzy[digits-1]
    #print('a',apu)
    modulo=apu%(digits+1)
    #print('m',modulo)
    dlj=apu//(digits+1)
    #print('d',dlj)
    output=10**(digits)+dlj
    #print('o',output)
    list1=[i for i in str(output)]
    #print(list1)
    print(list1[modulo])
else:
    print(k)

        
        
        
        
        
