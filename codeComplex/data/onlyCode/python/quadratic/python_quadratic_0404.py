from sys import stdin,stdout
def main():
	n,k=map(int,stdin.readline().split( ))
	s=stdin.readline()
	start=-1
	i=0;j=1;prev=1
	while i<n-1:
		while j<n:
			if s[i]==s[j]:
				if start==-1:
					start=j
					prev=j
				i+=1
				j+=1
			else:
				i=0
				j=prev+1
				prev=j
				start=-1
		break
	if start==-1:
		stdout.write("%s\n"%(s[:n]*k))
	else:
		j = n - start
		stdout.write("%s\n"%(s[:n]+s[j:n]*(k-1)))
main()

