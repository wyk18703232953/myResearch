#a, b = map(int, input().split())
def interact(c, d): return max(min((a ^ c) - (b ^ d), 1), -1)

def main():
	def ask(c, d):
		#return interact(c, d)
		print("?", c, d, flush = True)
		return int(input())

	relative = ask(0, 0)
	curA = 0
	curB = 0

	for i in range(29, -1, -1):
		q1 = ask(curA ^ 2 ** i, curB)
		q2 = ask(curA, curB ^ 2 ** i)
	
		if q1 == q2:
			if relative == 1:
				curA ^= 2 ** i
			else:
				curB ^= 2 ** i
			relative = q1
		elif q2 == 1:
			curA ^= 2 ** i
			curB ^= 2 ** i
	return curA, curB
print("!", *main())