from sys import stdout

class Digit:
    def __init__(self):
        self.count = {}

    def increment(self, k):
        if k in self.count:
            self.count[k] += 1
        else:
            self.count[k] = 1

    def found(self, k):
        if k in self.count:
            return self.count[k]
        else:
            return 0

def main(n):
    # Deterministic generation of n and mod, and the array
    # Here: n is the size of the array, mod is chosen as n+1 (at least 2 when n>=1)
    if n <= 0:
        stdout.write("0\n")
        return

    mod = n + 1
    array = [i * 7 + 3 for i in range(n)]

    ans = 0
    digits = [None] * 11
    for i in range(11):
        digits[i] = Digit()

    for i in range(n):
        temp = array[i] % mod
        for j in range(10):
            temp *= 10
            temp %= mod
            digits[j + 1].increment(temp)

    for i in range(n):
        temp = array[i]
        count = 0
        while temp > 0:
            temp //= 10
            count += 1

        find = mod - array[i] % mod
        find %= mod
        ans += digits[count].found(find)

    for i in range(n):
        temp1 = array[i] % mod
        temp2 = array[i]
        while temp2 > 0:
            temp2 //= 10
            temp1 *= 10
            temp1 %= mod

        if (temp1 + array[i]) % mod == 0:
            ans -= 1

    stdout.write(str(ans) + "\n")

if __name__ == "__main__":
    main(10)