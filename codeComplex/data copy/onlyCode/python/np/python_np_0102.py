from math import factorial

send = input()
receive = input()

cntP = send.count("+")
cntN = send.count("-")

cnt1 = receive.count("+")
cnt2 = receive.count("-")

mark = receive.count("?")

total = pow(2, mark)

if cntP < cnt1 or cntN < cnt2:
    valid = 0
else:
    valid = factorial(mark) / factorial(mark - cntP + cnt1) / factorial(cntP - cnt1)
print(f"{valid / total:0.12f}")
