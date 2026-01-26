from sys import stdout
N,M=map(int,input().split())
if M%2==0 and N%2==0:
    for m in range (1,M//2+1): 
        for n in range (1,N+1):
            stdout.write(str(n)+' '+str(m)+'\n')
            stdout.write(str(N+1-n)+' '+str(M+1-m)+'\n')
elif M%2==0 and N%2==1:
    for m in range (1,M//2+1): 
        for i in range (1,N+1):
            stdout.write(str(i)+' '+str(m)+'\n')
            stdout.write(str(N+1-i)+' '+str(M+1-m)+'\n')
else:
    for m in range (1,(M+1)//2): 
        for n in range (1,N+1):
            stdout.write(str(n)+' '+str(m)+'\n')
            stdout.write(str(N+1-n)+' '+str(M+1-m)+'\n')
    if N%2==0:
        for i in range (1,N//2+1):
            stdout.write(str(i)+' '+str((M+1)//2)+'\n')
            stdout.write(str(N+1-i)+' '+str((M+1)//2)+'\n')
    else:
        for i in range (1,(N+1)//2):
            stdout.write(str(i)+' '+str((M+1)//2)+'\n')
            stdout.write(str(N+1-i)+' '+str((M+1)//2)+'\n')
        stdout.write(str((N+1)//2)+' '+str((M+1)//2)+'\n')