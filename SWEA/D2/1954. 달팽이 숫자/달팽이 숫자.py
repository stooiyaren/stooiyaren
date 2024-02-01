T = int(input())
for t in range(1,T+1):
	N= int(input())
	matrix = [[0]*N for _ in range(N)]
	line_cnt = 1
	cnt = 1
	p = 0
	q = 0
	# di = [0,1,0,-1]
    # dj = [1,0,-1,0]
	while cnt <= N**2:
		if line_cnt % 4 == 1:
			for i in range(N):
				if matrix[p][i] == 0:
					matrix[p][i] = cnt				
					cnt += 1
					q = i
			line_cnt += 1
		elif line_cnt % 4 == 2:
			for i in range(N):
				if matrix[i][q] == 0:
					matrix[i][q] = cnt				
					cnt += 1
					p = i
			line_cnt += 1
		elif line_cnt % 4 == 3:
			for i in range(N-1,-1,-1):
				if matrix[p][i] == 0:
					matrix[p][i] = cnt				
					cnt += 1
					q = i
			line_cnt += 1
		elif line_cnt % 4 == 0:
			for i in range(N-1,-1,-1):
				if matrix[i][q] == 0:
					matrix[i][q] = cnt				
					cnt += 1
					p = i
			line_cnt += 1
	print(f'#{t}')
	for i in range(N):
		for j in range(N):
			print(matrix[i][j], end=' ')
		print()