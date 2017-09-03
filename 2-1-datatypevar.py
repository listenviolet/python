print('I\'m \"OK\"!')

#the content inside r'' will not be tranferred
print(r'\\\t\\')
print('\\\t\\')

print('''line1
line2
line3''')

print(True)
print(False)
print(3>2)
print(3 > 5)

#and
print('True and True:',True and True)
print('True and False:',True and False)
print('5 > 3 and 3 > 1:',5 > 3 and 3 > 1)

#or
print('True or True:',True or True)
print('True or False:',True or False)
print('False or False:',False or False)
print('5 > 3 or 1 > 3:',5 > 3 or 1 > 3)

#judgement
age=int(input('age:')) #string->int
if age >=18:
	print('adult')
else:
	print('teenager')

#None
print(None)

print(10/3)
print(10//3)
print(10%3)

#exercise
n = 123
f = 456.789
s1 = 'Hello,world'
s2 = 'Hello,\'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print('n:',n)
print('f:',f)
print('s1:',s1)
print('s2:',s2)
print('s3:',s3)
print('s4:',s4)
