def check(x,n,k):
    ate = x
    rem = n-ate
    #print(rem,ate)
    if rem*(rem+1)//2 == k+ate and rem >= 0 and ate >= 0:
        return True

    return False

def main():
    n,k = map(int,input().split())
    b = -1*(2*n+3)
    a = 1
    c = n**2
    c += n-(2*k)

    d = ((b**2)-(4*a*c))**0.5
    x1 = (-b+d)/2*a
    x2 = (-b-d)/2*a
    #print(x1,x2)
    if check(x1,n,k):
        print(int(x1))
        return

    print(int(x2))
    

main()
