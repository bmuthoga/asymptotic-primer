def prime_numbers(number):
	list=[]
	if number < 0:
        return "Only positive numbers allowed."
    if type(number) != int:
        return "Only integers allowed."
	for i in range(2,number+1):
		if i>1:
			for x in range(2,i):
				if(i%x)==0:
					break
			else:
				list.append(i)
	return list