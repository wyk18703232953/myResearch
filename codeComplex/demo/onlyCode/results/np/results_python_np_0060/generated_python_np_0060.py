from math import factorial as f

def main(n):
    s = "?" * n
    plusn = n // 2
    quest = s.count("?")
    plus = s.count("+")
    try:
        comb = f(quest) / (f(plusn - plus) * f(quest - (plusn - plus)))
        return float("%.12f" % (comb / 2 ** quest))
    except:
        return float("%.12f" % 0)


if __name__ == "__main__":
    print(main(10))