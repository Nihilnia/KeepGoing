
class P3w():

        def __init__(self, maxPow):

                self.maxPow = maxPow
                self.currentPow = 0

        def __iter__(self):

                return self

        def __next__(self):

                if self.currentPow <= self.maxPow:
                        result = 3 ** self.currentPow
                        self.currentPow += 1
                        return result
                else:
                        self.currentPow = 0
                        raise StopIteration

example = P3w(6)

# print(next(example))
# print(next(example))
# print(next(example))
# print(next(example))

for f in example:
        print(f)

for f in example:
        print(f)


def fibonacciSq():

        firstNumber = 1
        secondNumber = 1

        yield firstNumber
        yield secondNumber

        while True:
                firstNumber, secondNumber = secondNumber, firstNumber + secondNumber
                yield secondNumber


for number in fibonacciSq():
        
        if number < 1000:
                print(number)
        else:
                break