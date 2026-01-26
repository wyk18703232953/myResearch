import math

inp = input().strip()
dec = input().strip()
inp_dict = {"+":0,"-":0}
dec_dict = {"+":0,"-":0,"?":0}

for i in range(len(inp)):
	if inp[i]=="+":
		inp_dict["+"] += 1
	elif inp[i]=="-":
		inp_dict["-"] += 1

for i in range(len(dec)):
	if dec[i]=="+":
		dec_dict["+"] += 1
	elif dec[i]=="-":
		dec_dict["-"] += 1
	elif dec[i] == "?":
		dec_dict["?"] += 1

if(dec_dict["+"] == inp_dict["+"] and dec_dict["-"] == inp_dict["-"]):
	print(1.0000000000)
else:
	temp = inp_dict["+"] - dec_dict["+"]
	temp1 = inp_dict["-"] - dec_dict["-"]
	#print(temp,temp1)
	if temp + temp1 == dec_dict["?"] and temp>=0 and temp1 >= 0:
		temp2 = math.factorial(temp+temp1)/(math.factorial(temp)*math.factorial(temp1))
		for i in range(temp1+temp):
			temp2 = temp2 * 0.5
		print(temp2)
	else:
		print(0.000000000)



