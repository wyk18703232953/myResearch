def forninho(miolo, s):
    premiolo = miolo
    temp = 0
    while (miolo > 0):
        temp += miolo % 10;
        miolo = miolo // 10;
    if (premiolo - temp >= s):
        return 1
    else:
        return 0

entrada = input().split()
n = int(entrada[0])
s = int(entrada[1])

result = -1
l = 1
r = n
while (r-l >= 0):
    miolo = (l + r) // 2
    if(forninho(miolo,s) == 1):
        r = miolo - 1
        result = miolo
    else:
        l = miolo + 1

if (result == -1):
    print("0")
else:
    print(n - result + 1)
  		  	 			 	   	 		 	  		  	