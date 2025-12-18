v = input().split()
n = int(v[0])
k = int(v[1])

s = input()
ap = 0

i = 1
while i < n:
    if s[:i] == s[-i:]:
        ap = i

    i += 1

print(s + s[ap:]*(k-1))
  	    					  		 	   			 	  		