def fibonacci1 (n) :
	if n == 1 or n == 2 :
		return 1
	return fibonacci1 (n-1) + fibonacci1 (n-2)

for i in range (1, 30) :
	print (fibonacci1 (i))
