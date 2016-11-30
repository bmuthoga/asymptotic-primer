Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Function to generate prime numbers from 0 to n.
>>> 
>>> def prime_numbers(number):
	list=[]
	for i in range(2,number+1):
		if i>1:
			for x in range(2,i):
				if(i%x)==0:
					break
			else:
				list.append(i)
	return list

>>> 
