def fibonacci2 (n) :
	a, b = 1, 1
	for i in range (n-1) :
		a, b = b, a+b
	return a

#change the "30" to whatever positive integer you'd like it to calculate up to.
for i in range (1, 30) :
	print (fibonacci2 (i))
