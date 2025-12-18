# from itertools import combinations

CANDNUM = 5

I = lambda: [int(x) for x in raw_input().split()]
T = lambda x1, y1, x2, y2: (x1-x2)**2+(y1-y2)**2
			
def getCandidates(tsLst, curN, notSeen):
	r = []
	curD = {}
	k = 0
	cand = None
	curSet = set()
	for x in tsLst:
		i, j = x
		curSet.add(i)
		if len(curSet) == curN-1:
			cand = list(notSeen - curSet)[0]
			break
		curSet.add(j)
		if len(curSet) == curN-1:
			cand = list(notSeen - curSet)[0]
			break
	i = 0
	for x in tsLst:
		if cand in x:
			r.append(x)
			i += 1
			if i == CANDNUM:
				break
	return r

def solve(xs, ys, n, oLst):
	def solveEven(seen):
		def solveEvenRec(notSeen, tsLst):
			if len(notSeen) == 0:
				return 0, []
			ns = tuple(notSeen)
			if ns in solveEvenRec.d:
				return solveEvenRec.d[ns]
			minLst = []
			minT = 10000000

			cands = getCandidates(tsLst, len(notSeen), notSeen)
			for x in cands:
				i, j = x
				newNotSeen = notSeen.copy()
				if i in newNotSeen:
					newNotSeen.remove(i)
				if j in newNotSeen:
					newNotSeen.remove(j)
				newTsLst = []
				for x1 in tsLst:
					i1, j1 = x1
					if i1 in newNotSeen and j1 in newNotSeen:
						newTsLst.append(x1)
				rT, rLst = solveEvenRec(newNotSeen, newTsLst)
				rT += ts[x]
				if rT < minT:
					minT = rT
					minLst = [x] + rLst
			r = minT, minLst
			solveEvenRec.d[ns] = r
			return r
		solveEvenRec.d = {}
			
		newLst = []
		for i in range(n):
			if i not in seen:
				newLst.append(i)
		newN = n - len(seen)
		if newN == 2:
			minT = 10000000
			minLst = []
			for a in ts:
				if ts[a] < minT:
					minT = ts[a]
					minLst = [a]
			rT = minT
			rLst = minLst
		else:
			newTsLst = []
			for x in tsLst:
				a, _ = x
				i, j = a
				if i not in seen and j not in seen:
					newTsLst.append(a)
			notSeen = set(range(n)) - set(seen)
			rT, rLst = solveEvenRec(notSeen, newTsLst)
		return rT, rLst
	ts = {}
	tss = {}
	for i in range(n-1):
		x1, y1 = oLst[i]
		for j in range(i+1, n):
			x2, y2 = oLst[j]
			t = T(x1, y1, x2, y2)
			t1 = T(x1, y1, xs, ys)
			t2 = T(xs, ys, x2, y2)
			if t1+t2 >= t:
				ts[(i, j)] = t
				tss[(i, j)] = True
			else:
				ts[(i, j)] = t1+t2
				tss[(i, j)] = False
	tsLst = []
	for x in ts:
		tsLst.append((x, ts[x]))
	tsLst.sort(key=lambda x:x[1])
	if n%2:
		if n > 1:
			resT = 10000000
			resLst = []
			for i in range(n):
				x, y = oLst[i]
				t = 2*T(x, y, xs, ys)
				rT, rLst = solveEven([i])
				for a in rLst:
					i1, i2 = a
					x1, y1 = oLst[i1]
					x2, y2 = oLst[i2]
					rT += T(xs, ys, x1, y1)
					rT += T(xs, ys, x2, y2)
				rT += t
				if rT < resT:
					resT = rT
					newRLst = ['0']
					for a in rLst:
						w, v = a
						if tss[(w, v)]:
							newRLst.append(str(w+1))
							newRLst.append(str(v+1))
							newRLst.append('0')
						else:
							newRLst.append(str(w+1))
							newRLst.append('0')
							newRLst.append(str(v+1))
							newRLst.append('0')
					newRLst.append(str(i+1))
					newRLst.append('0')
					resLst = newRLst
		else:
			x, y = oLst[0]
			resT = 2*T(x, y, xs, ys)
			resLst = ['0', '1', '0']
	else:
		resT, rLst = solveEven([])
		for a in rLst:
			i1, i2 = a
			x1, y1 = oLst[i1]
			x2, y2 = oLst[i2]
			resT += T(xs, ys, x1, y1)
			resT += T(xs, ys, x2, y2)
		newRLst = ['0']
		for a in rLst:
			w, v = a
			if tss[(w, v)]:
				newRLst.append(str(w+1))
				newRLst.append(str(v+1))
				newRLst.append('0')
			else:
				newRLst.append(str(w+1))
				newRLst.append('0')
				newRLst.append(str(v+1))
				newRLst.append('0')
		resLst = newRLst
	return resT, resLst

xs, ys = I()
n = input()
oLst = []
for _ in range(n):
	x, y = I()
	oLst.append((x, y))
resT, resLst = solve(xs, ys, n, oLst)
print(resT)
print(' '.join(resLst))	