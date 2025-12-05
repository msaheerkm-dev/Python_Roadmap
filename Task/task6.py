text=input('Enter a string: ')
rev=''
for ch in text:
    rev=ch+rev
if rev==text:
    print('polindrome')
else:
    print('not polindrome')

print('polindrome' if text==text[::-1] else 'not polindrome')