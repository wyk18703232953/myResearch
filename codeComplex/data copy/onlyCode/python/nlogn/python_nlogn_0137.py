def socket(n,m,k,arr):
    arr.sort(reverse=True)
    devices=m
    curr_socket=0
    e_socket=k
    i=0
    t_socket=0
    count=0
    while i<n:
        if e_socket>=devices:
            return 0
        if curr_socket==0:
            curr_socket+=arr[i]
            count+=1
            e_socket-=1
            t_socket=curr_socket+e_socket
        else:
            if t_socket>=devices:
                return count
            else:
                curr_socket+=arr[i]-1
                count+=1
                t_socket=curr_socket+e_socket
        i+=1
    if t_socket>=devices:
        return count
    return -1

n,m,k=map(int,input().split())
arr=list(map(int,input().split()))
print(socket(n,m,k,arr))