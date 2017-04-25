import random

while True:
    name = input("Name: ")
    print('{}: {} {} {} {}'.format(name, random.randrange(1, 25), random.randrange(1, 35), random.randrange(1, 18), random.randrange(1, 9)))
