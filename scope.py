# LEGB
# Local Scope, Enclosing Scope, Global Scope, Built-In Scope

x = "global level"

def enclosing():
    x = "enclosing level"
    def innerfunc():
        x = "local level"
        print(x)
    innerfunc()

enclosing()