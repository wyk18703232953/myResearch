from string import digits
from collections import Counter
a = input()
b = input()
ca = Counter(a)
l = list()
if len(b) > len(a):
    for i in digits[::-1]:
        if i in ca:
            l.extend(i * ca[i])
else:
    def asd(i, s):
        if i == len(b):
            return True
        if s:
            for j in digits[::-1]:
                if j in ca and ca[j] > 0:
                    l.extend(j * ca[j])
            return True
        else:
            for j in digits[:int(b[i])+1][::-1]:
                if j in ca and ca[j] > 0:
                    ca[j] -= 1
                    l.append(j)
                    if asd(i + 1, j != b[i]):
                        return True
                    ca[j] += 1
                    l.pop()
            return False
    asd(0, False)
print("".join(l))

       		  	 	  	 	 	 	 	   			