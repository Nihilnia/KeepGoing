





def perfectNumbers(func):
    
    def wrapper


def primeNumbers(numbers):

    primeOnes = list()
    for f in numbers:
        divs = list()

        for x in range(1, f):
            if f % x == 0:
                divs.append(x)

        if len(divs) == 1:
            primeOnes.append(f)
            
    print("Prime numbers 1 - 1000:\n", *primeOnes, sep = "")