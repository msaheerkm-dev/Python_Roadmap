# nested function
def welcome(name):
    print('welcome '+ name )
def print_name(name): # parameter passing fn
    print('hello, '+ name)
    welcome('saheer')# nested fn
print_name('saheer')