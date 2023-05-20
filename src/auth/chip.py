import random
import string
import datetime

version = "0.0.1"
identifier = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
transactions = 0
time = datetime.datetime.now


def get():
    print(f"Version: {version}")
    print(f"Id: {identifier}")
    print(f"Transactions: {transactions}")
    print(f"Time: {time}")