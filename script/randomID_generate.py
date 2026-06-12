import random

def generate_random_id(length : int = 10):
    id = ""
    for i in range(length):
        r = random.randint(0,2)
        if r == 0:
            id = id + str(chr(random.randint(65, 90)))
        elif r == 1:
            id = id + str(chr(random.randint(97, 122)))
        else:
            id = id + str(random.randint(0, 9))

    return id