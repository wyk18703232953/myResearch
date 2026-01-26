def numtostr(a):
    var=[]
    while a>0:
 
       if a%26==0:
          var.append("Z")
          a=a//26-1
       else:
          var.append(chr(a%26-1+ord("A")))
          a=a//26
    var.reverse()
    return "".join(var)
 
def strtonum(b):
    par=len(b)
    result=0
    for i in range(1,par):
        result+=(26**i)
    par=len(b)-1
    for elem in b:
        if par!=0:
             result+=((ord(elem)-ord("A"))*((26)**par))
        else:
            result += ((ord(elem) - ord("A"))+1)
 
        if par==0:
            break
        par -= 1
    return result
 
def method1(par1):
    C=par1.index("C")
    result=numtostr(int(par1[C+1:]))+str(par1[1:C])
    return result
 
def method2(par2):
    c=0
    for elem in par2:
        try:
            if int(elem):
                break
        except:
            c+=1
    return "R"+par2[c:]+"C"+str(strtonum(par2[:c]))
 
i=input()
inp=[]
for j in range(int(i)):
     x=input()
     inp.append(x)
for key in range(len(inp)):
    if "R" in inp[key] and "C" in inp[key]:
        try:
            if int(inp[key][1:inp[key].index("C")]) and int(inp[key][inp[key].index("C")+1:]):
                print(method1(inp[key]))
        except:
            print(method2(inp[key]))
    else:
        print(method2(inp[key]))