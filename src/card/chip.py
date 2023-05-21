import random
import string
import datetime
import hashlib
import colorama
from colorama import Fore, Back, Style
import requests
import json

# Chip
version = "0.0.1"
privateIdentifier = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
publicIdentifier = hashlib.sha256(privateIdentifier.encode()).hexdigest()
transactions = 0
time = datetime.datetime.now()

#cardData
cdata = [
    {
        "cnum" : "1234 5678 9123 4567",
        "cexpire" : "12/24",
        "cvv" : "657",
        "cname" : "John Wood"
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

class silent():

    def warn():
        print("Silent warning")

class tap():

    def transaction():
        transaction.send()

class approval():

    def send():
        response = requests.get(url="https://63e23126-b363-4c17-9ee4-18a2992411d7.mock.pstmn.io/approval")
        
        if response.status_code == 200:
            approved = True
        else:
            approved = False
        return approved

class transaction():

    def passdata(cdata):
        pass

    def send():
        print("Passing cdata...")
        transaction.passdata(cdata)
        print("Sending approval request...")
        approval.send()
        approved = approval.send()
        if approved == True:
            print("Transaction approved")
        else:
            print("Transaction denied")
