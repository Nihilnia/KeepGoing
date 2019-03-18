

class Kareler():

        def __init__(self, maxN):
                
                self.maxN = maxN
                self.start = 1

        def __iter__(self):

                return self

        def __next__(self):

                if self.start < self.maxN:
                        self.start += 1
                        return "{} x 2 = {}".format(self.start, self.start ** 2)
                else:
                        raise StopIteration

sayi = Kareler(5)
print(next(sayi))
print(next(sayi))
print(next(sayi))
print(next(sayi))


def primeNumbers():

        for f in range(2, 1001):
                divs = list()
                for x in range(1, f):
                        if f % x == 0:
                                divs.append(x)
                if len(divs) > 1:
                        pass
                else:
                        yield f



for f in primeNumbers():
        print(f)


