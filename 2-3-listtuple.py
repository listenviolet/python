#list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

print(len(classmates))

print(classmates[0])
print(classmates[1])

print(classmates[-1])
print(classmates[-2])

classmates.append('Adam')
print(classmates)

classmates.insert(1,'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates.pop(-1)
print(classmates)

classmates[1] = 'Sarah'
print(classmates)

L = ['Apple', 123, True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2])
print(s[2][0])

L = []
print(len(L))

#tuple --once initialized can not be changed --get method same as list's
classmates = ('Michael', 'Bob', 'Tracy')
#when there is only one number inside, add ",",
#else the parenthese will be treat as a math operator character
t = (1,)
print(t)
t = ('a', 'b', ['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

#exercise
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])