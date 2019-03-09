import time

def calculateTime(function):

    def wrapper(numbers):
        start = time.time()

        result = function(numbers)

        finish = time.time()

        print(function.__name__, "- It's been {} seconds..".format(finish - start))
        return result
    return wrapper

@calculateTime
def x2(numbers):
    result = list()

    for f in numbers:
        result.append(f * 2)

    return result

print(x2(range(10)))



#another example

def nihilWasHere(x):

    def wrapper(y):

        result = x(y)
        print("nihil was here!")
        return result

    return wrapper

@nihilWasHere
def x3(numbers):
    numberList = list()
    for f in numbers:
        numberList.append(f * 3)
    return numberList

print(x3(range(10)))

def decorator(func):
    def wrapper(*args, **kwargs):
        print('Fonksiyon çalışacak...')
        func()
    return wrapper


@decorator
def func():
    print('Fonksiyon çalıştı.')


func()



# Another one!


def calculateIt(functionName):

    def wrapper(parameters):
        startTime = time.time()

        result = functionName(parameters)

        finishTime = time.time()

        print("Time:", finishTime - startTime)
        return result
    return wrapper

@calculateIt
def writeMyName(functionNihil):

    def wrapper(parameterNihil):

        resultNihil = functionNihil(parameterNihil)
        print("Nihil was here..")
        return(resultNihil)
    return wrapper

@writeMyName
def oneTo100(numbers):
    primeOnes = list()
    for f in numbers:
        divs = list()
        for x in range(1, f):
            if f % x == 0:
                divs.append(f)
        if len(divs) != 1:
            pass
        else:
            primeOnes.append(f)

    return primeOnes

print(oneTo100(range(1, 1000)))