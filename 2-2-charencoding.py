#ord
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

#unicode -u
print('\u4e2d\u6587')

#bytes -b
x=b'ABC'
y='ABC'
print('x:',x," y:",y)

#encode
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))  #to bytes
#print('中文'.encode('ascii'))

#decode
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#len str-length of characters
print(len('ABC'))
print(len('中文'))

#len bytes-length of bytes
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

#python contains chhinese characters-UTF-8
#uft-8 without BOM
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#format
print('Hello,%s' % 'world')
print('Hi,%s,you have $%d.' % ('Michael',1000000))
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)

print('Age: %s.Gneder: %s' % (25,True))

print('growth rate : %d %%' % 7)

#excercise
s1 = 72
s2 = 85
r = (s2-s1)/s2 * 100
print(r)
print('%2.1f %%' % r)