n,m=map(int,input().split())
listi=[]
for i in range(0,n):
    string=input()
    listi.append(string)
rownum=0 
flag=False
for row in listi:
    
    for letter in row:
            if("B" in row):
                p=row.index("B")
                
                s=row[::-1]
                q=abs(m-s.index("B")-1)
                
                if(p==q):
                    print(rownum+1,row.index(row[p])+1)
                    flag=True
                    break
                mr=(q+p)/2
                
                length=abs(q-p+1)
                
                rn= rownum + length//2
                
                print(rn+1,int(mr+1))
                flag=True
                break
            
            
    if(flag==True):
        break
            
    rownum+=1