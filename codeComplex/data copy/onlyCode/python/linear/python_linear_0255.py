s = input()
while s!="":
	if s==s[::-1]:
		s=s[:(len(s)-1)]
	else:
		break
print(len(s))