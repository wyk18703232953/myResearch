def subsets(L, i):
    if i == len(L):
        yield []
    else:
        for s in subsets(L, i+1):
            yield s
            yield [L[i]] + s

def computeValidProblemsets(problems, l, r, x):
    isValid = lambda ps: (len(ps) > 1) and (l <= sum(ps) <= r) and (ps[-1]-ps[0] >= x)
    print(sum(isValid(problemset) for problemset in subsets(sorted(problems), 0)))

if __name__ == '__main__':
    n, l, r, x = map(int, input().split())
    problems = list(map(int, input().split()))
    computeValidProblemsets(problems, l, r, x)

