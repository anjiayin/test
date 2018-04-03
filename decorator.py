def log(text):
    def decorators(func):
        def wrapper3(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper3
    return decorators
@log("text")
def new():
    print("2015-2-23")

#n = new
new()
#print(n)
