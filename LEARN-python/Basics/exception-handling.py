d=0
try:
    div=10/d
    print(div)
    print('try completed')
except ZeroDivisionError:
    print("can't divide using zero")
print('program completed')