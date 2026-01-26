n = int(input())
s = ['']
for i in range(n):
	inp = input()
	s.append(inp)
	pos = len(s) - 1
	while len(s[pos]) < len(s[pos-1]):
		s[pos], s[pos-1] = s[pos-1], s[pos]
		pos -= 1
out = 'YES'
for i in range(n):
	if not s[i] in s[i+1]:
		out = 'NO'
		s = []
		break
print(out + '\n'.join(s))
	 			   			  	 					  		    		