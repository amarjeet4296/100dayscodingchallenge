#1 Order
Str = 'I am very cool person'
l = Str.split()
L = l[::-1]
output = ' '.join(L)
print(output)

#Reverse Internal contentof each word
s = 'I am very cool person'
l = s.split()
l1 = []
for word in l:
    l1.append(word[::-1])
output = ' '.join(l1)
print(output)
