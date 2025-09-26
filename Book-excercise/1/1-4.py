#Character Strings

s = 'simple is the best'
print(s.capitalize())
print(s.capitalize().isupper())
print(s.upper())
print(s.upper().isupper())
print(s.split(" "))
print(s[-5:])

words = s.split(" ")
print(words)
print(words[len(words)-1])
print(len(words[len(words)-1]))

print(words[3] + " " + words[1])

# \ escape character
print('Jerry\'s Kids')

selstr3 = """"elev" > 1000"""
print(selstr3)
