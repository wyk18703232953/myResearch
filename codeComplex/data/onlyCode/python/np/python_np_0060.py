"""
██╗ ██████╗ ██╗    ██████╗  ██████╗  ██╗ █████╗
██║██╔═══██╗██║    ╚════██╗██╔═████╗███║██╔══██╗
██║██║   ██║██║     █████╔╝██║██╔██║╚██║╚██████║
██║██║   ██║██║    ██╔═══╝ ████╔╝██║ ██║ ╚═══██║
██║╚██████╔╝██║    ███████╗╚██████╔╝ ██║ █████╔╝
╚═╝ ╚═════╝ ╚═╝    ╚══════╝ ╚═════╝  ╚═╝ ╚════╝
"""
from math import factorial as f
n = input()
s = input()
quest = s.count("?")
plusn = n.count("+")
plus = s.count("+")
try:
	comb = f(quest)/(f(plusn - plus) * f(quest - (plusn - plus)))
	print("%.12f" %(comb/2 ** quest))
except:
	print("%.12f" %0)
