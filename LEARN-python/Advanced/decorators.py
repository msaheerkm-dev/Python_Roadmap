# decorators are used to modify a function or class
def str_upper(fn):
    def inner():
        dec=fn()
        return dec.upper()
    return inner
def print_str():
    return "hello world"
print("normal string: ",print_str())
d=str_upper(print_str)
print("decorated string: ",d())