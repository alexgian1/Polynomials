_coefficients = raw_input("Enter coefficients: ")
coefficients = _coefficients.split()
coefficients = [int(coefficient) for coefficient in coefficients]  #Convert every str to int in list
a0 = coefficients[len(coefficients)-1]
rational_roots = [1,-1]
for num in range(1,abs(a0)):
	div = a0/float(num)
	if div.is_integer():
		rational_roots.append(int(div))
		rational_roots.append(int(-div))
for root in rational_roots:
	print "Root: ",root
	result = coefficients[0]
	coeffsFactorised = [result]
	for coefficient in coefficients[1:]:
		result = result * root + coefficient
		coeffsFactorised.append(result)
		print result
	print "\n"
	if result == 0:
		rootExists = True
		print "==============\nFound root: %s\n==============" %str(root)
		print "New Coeffs: ",coeffsFactorised
		print "(",
		maxIndex = len(coeffsFactorised) - 2
		for i in coeffsFactorised[:-1]:
			coeffFinal = int(coeffsFactorised[::-1].index(i) - 1) 
			
			if coeffFinal == maxIndex:            #remove the plus from 1st variable (+x+1 --> x+1)
				if i == 1:
					print "x^%d" %coeffFinal,
				elif i > 0:
					print "%dx^%d" %(i,coeffFinal),
				elif i == 0:
					pass
				elif i == -1:
					print "-x^%d" %coeffFinal,
				else:
					print "%dx^%d" %(i,coeffFinal),
			
			elif coeffFinal != 1 and coeffFinal != 0:
				if i == 1:
					print "+x^%d" %coeffFinal,
				elif i > 0:
					print "+%dx^%d" %(i,coeffFinal),
				elif i == 0:
					pass
				elif i == -1:
					print "-x^%d" %coeffFinal,
				else:
					print "%dx^%d" %(i,coeffFinal),
			
			elif coeffFinal == 1:      #exponentiation of 1 omitted (5x^1 --> 5x)
				if i == 1:
					print "+x",
				elif i > 0:
					print "+%dx" %i,
				elif i == 0:
					pass
				elif i == -1:
					print "-x",
				else:
					print "%dx" %i,
			
			else:                  #remove x from a0
				if i >= 0:
					print "+%d" %i,
				else:
					print i,
		if root > 0:
			print ")","(x-%d)"%root
		elif root < 0:
			root2 = str(root)[1:]      #Remove the minus (-x --> x)
			print ")(x+%s)" %root2
		break
	else :
		rootExists = False
if not rootExists:
	print "==============\nNo Root Found\n=============="
	
raw_input()
		
		
		
	
	
