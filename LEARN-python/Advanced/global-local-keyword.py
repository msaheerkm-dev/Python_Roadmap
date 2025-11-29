# global nonlocal keywords
def check_scope():
    def do_local():
        test='local test'
    def do_non_local():
        nonlocal test
        test='non local test'
    def do_global():
        global test
        test='global test'
    test='default'
    do_local()
    print("test value after do_local "+test)
    do_non_local()
    print("test value after do_non_local "+test)
    do_global()
    print("test value after do_global "+test)
check_scope()
print("test value after main "+test)

# simple example of global local nonlocal
# LEGB rule Local Enclosed(nonlocal) Global  Built in rule
a=10 # global variable
def outer_fn():
    global a 
    b=20 
    print("inside the enclosed fn: ",b)
    a+=1 # we can't modify the global variable inside the fn until uses global keyword
    print("global variable: ",a)
    def inner_fn():
        nonlocal b # nonlocal variale 
        c=30 # local variable
        print("local variable: ",c)
        b+=1
        print("print nonlocal keyword inside the :",b)
    inner_fn()
outer_fn()
