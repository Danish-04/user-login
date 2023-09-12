
import random

def Generatebookid():
    for i in range (1,6):
        yield random.randint(1111,9999)

    
numbers=Generatebookid()
for i in range (1,6):
    print(next(numbers))