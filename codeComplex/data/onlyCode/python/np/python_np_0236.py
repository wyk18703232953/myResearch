def isValidSet(problemSet: list, minTotalDif: int, maxTotalDif: int, minDelta: int) -> bool:
    if len(problemSet) >= 2:
        total = sum(problemSet)
        myDelta = max(problemSet) - min(problemSet)
        if minTotalDif <= total <= maxTotalDif and myDelta >= minDelta:
            return True
    return False

def countValidSubsets(problems: list, minTotalDif: int, maxTotalDif: int, minDelta: int) -> int:
    
    def subsetBuilder (problems: list, currentSubset: list, nextElementIndex: int) -> None:
        if isValidSet(currentSubset, minTotalDif, maxTotalDif, minDelta):
            validSubsets.append(currentSubset)
        for i in range(nextElementIndex, len(problems)):
            currentSubset.append(problems[i])
            subsetBuilder(problems, currentSubset, i+1)
            currentSubset.pop(-1)
    
    index = 0
    currentSubset = []
    validSubsets = []

    subsetBuilder(problems, currentSubset, index)
    return len(validSubsets)

n, l, r, x = input().split()
n = int(n)
l = int(l)
r = int(r)
x = int(x)

probs = [int(prob) for prob in input().split()]

print(countValidSubsets(probs, l, r, x))


		  		 	 			 	  	  	 	 		 	 	