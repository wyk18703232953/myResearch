def quadrant(x, y, rx, ry):
	if x > rx and y > ry:
		return 1
	elif x < rx and y > ry:
		return 2
	elif x < rx and y < ry:
		return 3

	else:
		return 4

def main(n):
	# 确定性生成 qx, qy, kx, ky, cx, cy
	qx = n
	qy = n * 2
	kx = n // 2
	ky = (n // 2) * 3
	cx = n * 3 // 2
	cy = n * 4 // 3

	if quadrant(kx, ky, qx, qy) == quadrant(cx, cy, qx, qy):
		# print("YES")
		pass

	else:
		# print("NO")
		pass
if __name__ == "__main__":
	main(10)