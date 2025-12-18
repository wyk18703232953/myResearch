def main():
	s = list(input())
	t = list(input())
	if len(s) < len(t):
		s.sort(reverse=True)
		print(''.join(s))
	else:
		count = [0] * 10
		for elm in s:
			count[ord(elm) - ord('0')] += 1
		ans = []
		less = False
		for i in range(len(s)):
			for j in range(9, -1, -1):
				if not less:
					if j <= ord(t[i]) - ord('0') and count[j] > 0:
						if j < ord(t[i]) - ord('0'):
							ans.append(chr(j + ord('0')))
							count[j] -= 1
							less = True
							break
						else:
							curr_num = 0
							for k in range(10):
								if j == k:
									for tmp in range(count[k] - 1):
										curr_num = curr_num * 10 + k
								else:
									for tmp in range(count[k]):
										curr_num = curr_num * 10 + k
							rest_num = 0
							for k in range(i + 1, len(s)):
								rest_num = rest_num * 10 + (ord(t[k]) - ord('0'))
							if rest_num >= curr_num:
								ans.append(chr(j + ord('0')))
								count[j] -= 1
								break
							else:
								continue
				else:
					if count[j] > 0:
						ans.append(chr(j + ord('0')))
						count[j] -= 1
						break
		print(''.join(ans))


if __name__ == '__main__':
	main()
