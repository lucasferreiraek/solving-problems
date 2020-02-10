def decision_trade(array):
	less, position = array[0], 0

	for i in range(1, len(array)):
		if array[i] < less:
			less = array[i]
			position = i
			
	if position+1 == len(array):
		return 0
	else:
		higher = array[position+1]
		
		for i in range(position, len(array)):
			if array[i] > higher:
				higher = array[i]
		
		return abs(less-higher)
		


array_1 = [7, 1, 5, 3, 6, 4]
array_2 = [7, 6, 4, 3, 1]

print(decision_trade(array_1))

print(decision_trade(array_2))

