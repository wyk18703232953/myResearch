def possible(a,index,a1,b):
    rem = []
    for i in range(len(a)):
        if i != index:
            rem.append(a[i])

    a3 = a1[:]
    rem.sort()
    a3.append(a[index])
    a3.extend(rem)
    a2 = ''
    for i in a3:
        a2 += str(i)

    if int(a2) <= b:
        return True

    return False

def main():
    a = list(map(int,input()))
    b = int(input())

    a.sort(reverse = True)
    a1 = []
    for pos in range(len(a)):
        for i in range(len(a)):
            if possible(a,i,a1,b):
                a1.append(a[i])
                a.pop(i)
                break
            
    for i in a1:
        print(i,end = '')

main()
