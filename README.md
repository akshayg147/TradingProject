# TradingProject
Accepts a Name,a CSV file and timeframe(will be a Integer and unit will be Minute). 
Store the CSV file on the Django server.
Store the data present in the file in the python list of candle objects.
The candle object have attributes: [id, open, high, low, close, date]
It converts the list of candles that is one minute into a given timeframe. [Using async operations]
Store this converted data into a JSON file and store it in the file system.
In the response, the user gets the option to download the JSON file.
