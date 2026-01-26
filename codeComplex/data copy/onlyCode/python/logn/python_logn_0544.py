import bisect
xzy=[10,190,2890,38890,488890,5888890,68888890,788888890,8888888890,98888888890,1088888888890,11888888888890]
k=int(input())
digits=bisect.bisect_left(xzy,k)
if k==10:
    print(1)
elif k>10:
    apu=k-xzy[digits-1]
    modulo=apu%(digits+1)
    dlj=apu//(digits+1)
    output=10**(digits)+dlj
    list1=[i for i in str(output)]
    print(list1[modulo])
else:
    print(k)

        
        
        
        
        
