def exampleOne(*args):
    for f in args:
        print(f)

exampleOne(1, "a", 2, "b")




def exampleTwo(**kwargs):
    print(kwargs)

exampleTwo(name = "nihil", language = "python")



def exampleThree(**parameters):
    for keys, values in parameters.items():
        print("Key:", keys)
        print("Values:", values)

exampleThree(nick = "okan", language = "Python")



def exampleFour(*args, **kwargs):
    theArgs = list()
    theKwargs= list()
    for f in args:
        theArgs.append(f)

    for f, x in kwargs.items():
        theKwargs.append((f, x))

    print("Args:", theArgs)
    print("Kwargs", theKwargs)

exampleFour(1, 2, 3, 4, name = "Rasputin", song = "Funk Overload")

# [1, 2, 3, 4]
#  [('name', 'Rasputin'), ('song', 'Funk Overload')]


def sayHi(name = "Unknown"):
    print("Hi", name)

sayHi("Rasputin")

hello = sayHi
hello("-- FUNK OVERLOAD --")
# even if you delete the sayHi function, your hello function will work

del sayHi
hello("DELETED BUT STILL WORKS!")
#But sayHi can't work as you know!

# sayHi("asdfas")
# NameError: name 'sayHi' is not defined


def sayHello(*args):
    for f in args:
        print("Hello", f)

sayHello(1, 2, 3, 4, "a", "b", "c", "d")

#or 

rasputin = sayHello

print("Rasputin:")
rasputin(1, 2, 3, 4, "a", "b", "c", "d")



def function1():

    def function2():
        print("Hello from little function!")
    function2()
    print("Hi, it's mother function!")

function1()

#another Example

def function3(*numbers):

    def function4(numbers):
        total = 0
        
        for f in numbers:
            total += f
        return(total)
    print(function4(numbers))

function3(1, 2, 3, 4)


# Let's make some smart things

def gorillaz(question, *Args):

    def plus(Args):
        total = 0
        for f in Args:
            total += f
        return total

    def minus(Args):
        total = 0
        for f in Args:
            total -= f
        return total

    def divide(Args):
        total = 0
        for f in Args:
            total /= f
        return total

    def multiply(Args):
        total = 0
        for f in Args:
            total *= f
        return total

    if question == "+":
        return plus

    elif question == "-":
        print(minus(Args))

    elif question == "/":
        print(divide(Args))

    elif question == "*":
        print(multiply(Args))
        
gorillaz("+", 1, 2, 3, 4, 5) #REALLY SMART..


###################################################################


def nihil1(process):

    def nihil2(*args):
        total = 0

        for f in args:
            total += f
        return total

    
    def nihil3(*args):
        total = 0

        for f in args:
            total *= f
        return total

    if process == "plus":
        return nihil2
    
    else:
        return nihil3

toplamaIslemi = nihil1("plus")
print("toplamaIslemi: ", toplamaIslemi(4, 5))

def tryIt(toplamaIslemi):

    return toplamaIslemi[0] + 1

print(tryIt((2, 3)))


####


def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    return a / b

def anaFonksiyon(fon1, fon2, fon3, fon4, islemAdi = "unknown"):

    if islemAdi == "toplama":
        return fon1(2, 7)
    elif islemAdi == "cikarma":
        return fon2(5, 2)
    elif islemAdi == "bolme":
        return fon3(5, 5)
    elif islemAdi == "carpma":
        return fon4(5, 5)

dortIslem = anaFonksiyon(toplama, cikarma, bolme, carpma, "toplama")
print("Toplama islemi sonucu:", dortIslem)

#or 

dortIslem2 = anaFonksiyon(toplama, cikarma, bolme, carpma, "carpma")
print("Carpma islemi sonucu:", dortIslem2)
