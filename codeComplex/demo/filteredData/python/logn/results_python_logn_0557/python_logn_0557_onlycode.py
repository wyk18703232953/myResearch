

import bisect

    
b = []
a = []
b.append(0)

for i in range(1, 15):
	b.append(9 * i * (10 ** (i - 1)))


a.append(b[0])
for i in range(1, 15):
	a.append(a[i - 1] + b[i])

k = int(input())

th = bisect.bisect_left(a, k)
th -= 1;
k = k - a[th];
start = 10 ** th;
now = th + 1;
rem = k % now;
iss = k / now;
end = start + (k / now);
temp = str(end - 1);
s = "";
s += temp[now - 1] + str(end) + str(end + 1);



print(s[0 + rem])

 