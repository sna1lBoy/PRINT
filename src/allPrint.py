pythonPrint = print

# javascript's console.log
class console:
    def log(self):
        pythonPrint(self)

# java's System.out.println
class System:
    class out:
        def println(self):
            pythonPrint(self)

# C#'s Console.write
class Console:
    def write(self):
        pythonPrint(self)

# C's printf
def printf(self):
    pythonPrint(self)

# making print better
def print(this):
    print(this)