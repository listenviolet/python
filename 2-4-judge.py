#is elif else
age = 20
if age >= 6:
	print('teenager')
elif age >=18:
	print('adult')
else:
	print('kid')

#exercise
height = 1.75
weight = 80.5
bmi = weight/(height*height)
print(bmi)
if bmi < 18.5:
	print('1')
elif bmi >=18.5 and bmi <25:
	print('2')
elif bmi >=25 and bmi <28:
	print('3')
elif bmi >=28 and bmi <=32:
	print('4')
elif bmi > 32:
	print('5')
