_coefficients = raw_input("Enter coefficients: ")
coefficients = _coefficients.split()
coefficients = [int(coefficient) for coefficient in coefficients]  #Convert str to int
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
		break
	else :
		rootExists = False
if not rootExists:
	print "==============\nNo Root Found\n=============="
	
input()
		
		
		
	
	
