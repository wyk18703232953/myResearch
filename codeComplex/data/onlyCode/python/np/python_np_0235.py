def suma_o_resta(a, b):
	return (a & (1<<b))

def diferencia(s1, d):
	if s1:
		s1.sort()
		#print(*s1, sep=" - ")
		if s1[-1] - s1[0] >= d:
			#print(str(s1[-1]) + " - " + str(s1[0]) + " = " + str(s1[-1] - s1[0]))
			return s1
		else:
			return diferencia(s1.remove(s1[-1]), d)	
	return s1

def no_sets(v, n, l, r, d):
	s = []
	cont = 0
	for x in range(1<<n):
		for i in range(n):
			#print("(" + str(x) + ", " + str(i) + ")")
			if suma_o_resta(x, i) > 0:
				#print(str(suma_o_resta(x, i)))
				s.append(v[i])
		s = diferencia(s, d)
		if s:
			if sum(s) >= l and sum(s) <= r:
				cont += 1
		s = []
	return cont;
	

n, l, r, x = map(int, input().split())

v = list(map(int, input().split()))

print(str(no_sets(v, n, l, r, x)))


				 			  				   	  	 		 	