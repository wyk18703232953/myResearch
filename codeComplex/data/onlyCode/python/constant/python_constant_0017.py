from math import sqrt


def dist(speed, time):
	""" 
	Calculates the distance will be covered in specified time, 
	if car's current speed is speed. 
	This function will not take car's speed limit into account. 
	Also it assumes, that car is always driven with maximum acceleration a
	"""
	return speed * time + a * time**2 / 2


def travelTime(distance, speed):
	"""
	Calculates the time, required to travel specified distance, 
	if car have starting speed equal to speed. 
	This function will also take care about car's speed limit.
	"""
	tAll = (- speed + sqrt(speed**2 + 2 * distance * a)) / a

	tMax = (v - speed) / a

	if tMax >= tAll:
		return tAll
	else:
		return tMax + (distance - dist(speed, tMax)) / v


a, v = map(int, input().split())
l, d, w = map(int, input().split())

if v <= w:
	print(travelTime(l, 0))
else:
	tw = w / a  # time to gain speed w

	dw = dist(0, tw)

	if dw >= d:
		print(travelTime(l, 0))
	else:
		print(tw + 2 * travelTime((d - dw) / 2, w) + travelTime(l - d, w))
