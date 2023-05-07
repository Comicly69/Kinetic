import os
from forex_python.converter import CurrencyRates
import time
import colorama
from colorama import *

# specify the path to the directory
directory = 'currency/'

print(f"{Fore.GREEN}{Style.BRIGHT}Starting updater...{Style.RESET_ALL}")

# create directories for currencies
currencies = ['AUD', 'CAD', 'CNY', 'EUR', 'USD']
for currency in currencies:
    os.makedirs(os.path.join(directory, currency), exist_ok=True)

print(f"{Fore.GREEN}{Style.BRIGHT}Completed making dirs{Style.RESET_ALL}")
time.sleep(0.5)
print(f"{Fore.RED}{Style.BRIGHT}Starting Conversions...")

# create conversion files for each currency
c = CurrencyRates()
for currency1 in currencies:
    with open(os.path.join(directory, currency1, f'conversions.txt'), 'w') as f:
        # create conversion rates for each currency to every other currency
        for currency2 in currencies:
            if currency1 != currency2:
                conversion_rate = c.get_rate(currency1, currency2)
                f.write(f"{currency1} > {currency2} ({conversion_rate})\n")
                f.write("1")
                print(f"{Fore.GREEN}Completed {currency1}")
