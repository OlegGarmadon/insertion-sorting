def  insert_cabinet(cabinet, to_insert):
	check_location = len(cabinet) - 1
	check_location = 0
	while(check_location >= 0):
		if to_insert > cabinet[check_location]:
			insert_location = check_location +1
			check_location = -1
		check_location = check_location - 1
	cabinet.insert(insert_location, to_insert,)
	return(cabinet)

cabinet = [1, 2, 3, 3, 4, 5, 6, 8, 12,]
newcabinet = insert_cabinet(cabinet, 5)
print(newcabinet)