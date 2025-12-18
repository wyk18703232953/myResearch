from sys import stdin, stdout
ti = lambda : stdin.readline().strip()
os = lambda i : stdout.write(str(i) + '\n')
ma = lambda fxn, ti : map(fxn, ti.split())
ol = lambda arr : stdout.write(' '.join(element for element in arr) + '\n')
olws = lambda arr : stdout.write(''.join(element for element in arr) + '\n')



class Digit:
	def __init__(self):
		self.count = {}

	def increment(self, k):
		if self.count.has_key(k):
			got = self.count[k]
			self.count[k] += 1
		else:
			self.count[k] = 1

	def found(self, k):
		if self.count.has_key(k):
			return self.count[k]
		else:
			return 0

n, mod = ma(int, ti())
array = ma(int, ti())


ans = 0
digits = [None]*11
for i in range(11):
	digits[i] = Digit()

for i in range(n):
	temp = array[i]%mod

	for j in range(10):
		temp *= 10
		temp %= mod

		digits[j+1].increment(temp)

for i in range(n):
	temp = array[i]
	count = 0
	while temp>0:
		temp /= 10
		count += 1

	find = mod-array[i]%mod
	find %= mod
	ans += digits[count].found(find)

for i in range(n):
	temp1 = array[i]%mod
	temp2 = array[i]

	while temp2 > 0:
		temp2 /= 10
		temp1 *= 10
		temp1 %= mod

	if ((temp1 + array[i])%mod == 0):
		ans -= 1

os(ans)