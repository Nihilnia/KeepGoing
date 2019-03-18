


def exPow():

    for f in range(1, 6):
        yield f ** 2

exIterable = iter(exPow())

for f in exIterable:
    print(f)



# lits comprehension to generator

myList = (i * 3 for i in range(1, 6))

iterMylist = iter(myList)

print(myList)
print(iterMylist)

for f in myList:
    print(f)

# Another example


def multiplicationTable():

    for f in range(1, 11):
        for x in range(1, 11):
            yield "{} x {} = {}".format(f, x, f * x)
        print("\n")

# makeIterable = iter(multiplicationTable())

for f in multiplicationTable():
    print(f)

#NOTE: Actually range() function is a good example for generator.