def ft_count_harvest_iterative():
	count = int(input("Days until harvest: "))
	days_left = range(1, count + 1, 1)
	for i in days_left:
		print("Day", i)
	print("Harvest time!")