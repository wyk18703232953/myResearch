line1 = str(input());
line2 = str(input());

truePosition = 0;
fakePosition = 0;
questionMarks = 0;
for i in range(len(line1)):
	if line1[i] == "+":
		truePosition += 1;
	if line1[i] == "-":
		truePosition -= 1;
	if line2[i] == "+":
		fakePosition += 1;
	if line2[i] == "-":
		fakePosition -= 1;
	if line2[i] == "?":
		questionMarks += 1;
		
distanceToMove = abs(truePosition - fakePosition);
#print("Distance: ", distanceToMove);


def factorial(x):
	if x == 0:
		return 1;
	else:
		return x * factorial(x-1);
		
def probToMove(dist, questionMarks):
	if(dist > questionMarks):
		return float(0);
	reducedDist = questionMarks - dist;
	if(reducedDist % 2 != 0):
		return float(0);
	dist = reducedDist//2 + dist;
	headsFlips = 1;
	headsOrders = factorial(questionMarks) / ((factorial(dist) *factorial(questionMarks-dist)));
	#print("HeadsFlips:", headsFlips);
	#print("headsOrders:", headsOrders);
	totalPossibilities = 2**questionMarks;
	#print("totalPossibilities:", totalPossibilities);
	return headsFlips * headsOrders / totalPossibilities;
	
print(probToMove(distanceToMove, questionMarks));