# TradingProject
1 . Accepts a Name,a CSV file and timeframe(will be a Integer and unit will be Minute).

2. Store the CSV file on the Django server.

3. Store the data present in the file in the python list of candle objects.

4. The candle object have attributes: [id, open, high, low, close, date]

5. It converts the list of candles that is one minute into a given timeframe. [Using async operations]

6. Store this converted data into a JSON file and store it in the file system.

7. In the response, the user gets the option to download the JSON file.
