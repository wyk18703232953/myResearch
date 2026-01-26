def qtd(u):
    ans = 0
    while(u > 0):
        u//=10
        ans += 1
    return ans

def digitos(u):
    ans = 0
    while(u > 0):
        ans += u%10
        u//=10
    return ans

n, m = input().split()
m = int(m)
number = int(n)
ans = 0
size_n = qtd(m)
i = m

while(i < m+(size_n*9) + 1): 
    if(i > number): #n não pode ser maior que m
        break
    if(i - digitos(i) >= m): #verificar digitos
        ans += 1
    i += 1

    
if(i > number):
    print(ans)
else:
    print(number-i+1+ans)

   				    			 			  		  	 	