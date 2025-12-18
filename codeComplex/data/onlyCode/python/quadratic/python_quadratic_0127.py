if __name__ == '__main__':
		n,m = map(int, input().split())
		l = list(map(int, input().split()))
		d = dict()
		if len(set(l)) < n:
			print(0)
		else:
			for i in range (m):
				d.setdefault(l[i],0)
				d[l[i]]+=1
			min1 = 999999999
			for i in d.values():
				if i < min1 :
					min1 = i
			print(min1)