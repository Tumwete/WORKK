n=int(input('please enter your number: '))
if n <=0:
	print('sorry,that factorial doesnt exist')
elif n==1:
	print('the factorial of 1 is 1')
else:
	facto=1
	for i in range(2,n+1):
		facto=facto*i
	print(facto)
						
				
