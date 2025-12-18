

def main():
    n, m = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c_i= 0
    a_i= 0
    bought = 0
    while c_i!= n and a_i!= m:
        if(a[a_i]>=c[c_i]):
            a_i+=1
            c_i+=1
            bought+=1
        else:
            c_i+=1
    print(bought)
if __name__ == "__main__":
    main()