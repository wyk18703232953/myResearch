a = list(input())
b = input()
out = []
mx = '/'
a.sort()
a.reverse()
x = len(a)
if x == len (b):
    for i in range(x):
        q = 0
        
        for j in range(len(a)):
            if a[j] == b[i]:
                out.append(a[j])
                a.pop(a.index(a[j]))
                q = 1
                break
            elif a[j] < b[i]:
                out.append(a[j])
                a.pop(a.index(a[j]))
                print(''.join(out), end = '')
                print(''.join(a))
                exit(0)
        if q == 0:
            break
    if q == 1:
        print(''.join(out))
    else:
        y = len(out)
        for i in range(y-1, -1, -1):
            for j in range(len(a)):
                if a[j] < b[i] and a[j]>mx:
                    mx = a[j]
            if mx != '/':
                   
                    
                a.append(out[len(out)-1])
                out.pop()
                out.append(mx)
                a.pop(a.index(mx))
                a.sort()
                a.reverse()              
                print(''.join(out), end = '')
                print(''.join(a))
                exit(0)
            else:
                a.append(out[len(out)-1])
                out.pop()
                a.sort()
                a.reverse()
                    
                    
                    
        a.pop(a.index(mx))
        print(mx, end ='')
        print(''.join(a))
                
                
else:
    print(''.join(a))
        
'''15778899
98715689'''

