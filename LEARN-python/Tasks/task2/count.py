string="data analytics"
print("string: ", string)
n=string.count("a")
print("Count of 'a': ", n)

# looping
count=0
for char in string:
    if char=="a":
        count+=1
print("Count of 'a' using loop: ", count)