n = int(input())
a = input()
zero = 0
for i in range(len(a)):
    if (a[i] == "0"):
        zero += 1
if ("1" in a):
    print("1", end="")
    print("0"*zero)
else:
    print("0"*zero)