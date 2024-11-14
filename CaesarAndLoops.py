text = 'ANTON'
for c in text:
    print(c)
    print(ord(c))
    print(chr(ord(c)+2))

for i,c in enumerate(text):
    print (f'An der Position {i}: {c}')

for c in text[3:]:
    print(c)

text = "Hello"

#Kaboom
text[1] = 'a'
a = 3
print(text)
print(a)
text = 'Hallo'
a = 3+20
print(text)
print(a)
