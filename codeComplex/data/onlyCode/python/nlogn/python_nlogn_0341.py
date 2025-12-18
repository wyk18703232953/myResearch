def main():
    n = int(input())
    
    s = []
    
    for i in range(n):
        s.append(input())
    
    for i in s:
        for j in s:
            if (i not in j) and (j not in i):
                print('NO')
                return
    
    print('YES')
    s = sorted(s, key=lambda x : len(x))
    for pal in s:
        print(pal)

main()
		   	 	 	 	 	   	 	 	      		