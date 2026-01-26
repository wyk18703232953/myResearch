MAX=10**9 #O((n*m+(2**m)**2)*log(MAX))
def main():
    
    n,m=readIntArr()
    arrs=[]
    for _ in range(n):
        arrs.append(readIntArr())
    
    def checkPossible(minB):
        binRepresentations=set()
        for arr in arrs:
            binRepresentations.add(convertToBinary(arr,minB))
        binList=list(binRepresentations)
        ii=jj=-1
        n=len(binList)
        for i in range(n):
            for j in range(i,n):
                if binList[i]|binList[j]==(1<<m)-1: #ok
                    ii=binList[i]
                    jj=binList[j]
        if ii!=-1: #ok
            ansi=ansj=-1
            for i in range(len(arrs)):
                b=convertToBinary(arrs[i],minB)
                if b==ii:
                    ansi=i
                if b==jj:
                    ansj=i
            # print('ii:{} jj:{}'.format(ii,jj))
            # print('ok minB:{} ansi:{} ansj:{}'.format(minB,ansi,ansj))
            return (ansi,ansj)
        else:
            return None
                    
    def convertToBinary(arr,minB):
        b=0
        for i in range(m):
            if arr[i]>=minB:
                b|=(1<<i)
        return b
    
    minB=-1
    i=j=-1
    b=MAX
    while b>0:
        temp=checkPossible(minB+b)
        if temp==None: #cannot
            b//=2
        else: #can
            minB+=b
            i,j=temp
    i+=1;j+=1
    print('{} {}'.format(i,j))
    
    return
    
import sys
input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.
 
def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))
 
def readIntArr():
    return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]
 
def makeArr(*args):
    """
    *args : (default value, dimension 1, dimension 2,...)
    
    Returns : arr[dim1][dim2]... filled with default value
    """
    assert len(args) >= 2, "makeArr args should be (default value, dimension 1, dimension 2,..."
    if len(args) == 2:
        return [args[0] for _ in range(args[1])]
    else:
        return [makeArr(args[0],*args[2:]) for _ in range(args[1])]
 
def queryInteractive(x,y):
    print('? {} {}'.format(x,y))
    sys.stdout.flush()
    return int(input())
 
def answerInteractive(ans):
    print('! {}'.format(ans))
    sys.stdout.flush()
 
inf=float('inf')
MOD=10**9+7
 
for _abc in range(1):
    main()