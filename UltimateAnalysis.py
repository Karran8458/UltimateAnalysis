def ultimate_analysis(arr):
	sum = 0
	for x in range(0,len(arr),1):
		sum = sum + arr[x]	
	
	minimum = min(arr)
	maximum = max(arr)
	length = len(arr)
	avg = sum/length
	analysis = {
		"sumTotal":sum,
		"average":avg,
		"minimum":minimum,
		"maximum":maximum,
		"length":length
	}
	return analysis
	
