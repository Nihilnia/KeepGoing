# sys Module

# sys module is simply system module of python.
#We can manage our python software with sys module.

import sys

# what is in sys

for f in dir(sys):
        print(f)

# exit()

userInput1 = input("What's your name: ")
userInput2 = input("What's your surname: ")
print("Welcome", userInput1, userInput2)
sys.exit()

# stdin "input", stdout "output", stderr "error"

sys.stdout.write("aaayye")
sys.stdout.flush()

sys.stderr.write("Crystal!")
sys.stderr.flush()


# an example for... I am little confused rn.

def exampleOne(a, b, c):
        return a + b + c

if len(sys.argv) == 4:
        print("a + b + c =", exampleOne(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
else:
        print("Try again..")
                                         # when we do process with terminal, we can get inputs like sys.argv

# Look at that example one

print(sys.argv)
# "on the terminal" python sys module.py 1 2 3
# we got a list like that ['sys module.py', '1', '2', '3],
"SO, this inputs coming to in sys.argv"