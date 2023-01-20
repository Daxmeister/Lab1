import random
def one_coin():
    for i in range(10):
        if random.randrange(0, 2) == 0:
            return False
    return True
print(one_coin())

for i in range(20):
    print(random.randrange(0, 2))