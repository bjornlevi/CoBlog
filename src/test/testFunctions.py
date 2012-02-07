from datetime import datetime
import random
import string

def now():
    return datetime.now()

def random_word():
    return ''.join(random.sample(string.ascii_lowercase, random.randint(1, 12))) + ' '

def random_data(keys):
    results = {}
    for key in keys:
        results[key] = random_word()
    return results