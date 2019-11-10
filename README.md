# Binance Account Monitor - Python Implemetaoin

This is a basic implementation of the binance.com API. On running, it builds a local database of withdrawls and deposits, and begins listening for new withdraws, deposits, or changes to balance, on which it will alert to console with new data, and save the new data to its database.

This is for a trading club that wishes to track their outcomes vs contributions to the club account.

## Dependencies

    python -m pip install python-binance
    python -m pip install schedule
    

^^ The above packages are required to run the script. The script will look for a file in the same directory named ".keys", and pull the first two lines and use them as API keys. That file should be formatted thusly:

    43242351hioho3h5helloimtheapitoken2t32i3ht3loj
    54j54j3lk5helloimtheapisecret32h5;lk32j53kl4j

with your actual api values. Access token on line one, api secret on line two. Do not share these keys! Others can use them to access your exchange data, or even worse, trade your coins. API keys can be accessed from Binance. Click your profile tab and select "API Management", and request your own keys.

### Script functionality:

This script can be run by typing "python binance-api.py" in the terminal. When run, it will listen for new deposits or withdrawls. When one happens, the console will print an alert with new information, and save the deposit info to deposit-database.txt or withdraw-database.txt as appropriate.

The script writes to file databases, but it's technically redundant to list processing. It allows for cleaner startup and easier debugging, but is not core to the functioality. Inasmuch as this project is made as a generic bootstrap to other's python binance API projects, the debug-friendly output files remain. Be warned that this will put the Binance account's history in plaintext on your drive. 

Remvoing these db files is a potential future todo. You can expand functionality using the API functions listed here: https://python-binance.readthedocs.io/en/latest/account.html

#### Contact:

I can be reached at twitter.com/michaelharms70
