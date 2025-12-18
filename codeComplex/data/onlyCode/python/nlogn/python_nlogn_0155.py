import sys
def fi():
	return sys.stdin.readline()
if __name__ == '__main__':
	n,k = map(int, fi().split())
	# k = int(fi())
	l = list(map(int, fi().split()))
	d = dict()
	c = set()
	l.sort()
	for i in range (n):
		if not d.get(l[i]):
			c.add(l[i])
			d.setdefault(l[i]*k,1)
	print(len(c))