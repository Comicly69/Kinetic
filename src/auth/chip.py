import random
import string
import datetime
import hashlib

# Chip
version = "0.0.1"
privateIdentifier = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
publicIdentifier = hashlib.sha256(privateIdentifier.encode()).hexdigest()
transactions = 0
time = datetime.datetime.now()

#cardData
cdata = [
    {
        "cnum" : "1"
    }
]


def get():
    return {
        "version": version,
        "privateIdentifier": privateIdentifier,
        "publicIdentifier": publicIdentifier,
        "transactions": transactions,
        "time": time
    }

class transaction():

    def send():
        pass