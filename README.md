
# Stock selector

#### Video Demo: <URL HERE>

#### Description:

For this project, I wanted to define a program that selects stocks that seems good to invest in according to:

 - A specific market, like France, US,...
 - Select a stock that follows a normal distribution for the close price
 - Select a stock that the last close value is lower than the mean by at least 5%
 - Save the market information for the given market in a CSV file

## **def get_symbol(mkt):**

To define the specific market, the library **stocksymbol** is used. It can give make a list of all the tickers from a specific market. an API key is required. The list of tickers needs to be transformed into a single string, single space separated for later use.

## **def get_close_volume(list_symbols, duration, frequence):**

To retrieve all the market information, the library yfinance is used. It can give back a panda data frame for all the given tickers, on a specific duration and frequency.
Extra online tutorial for the panda library was required. Once the raw data frame is imported, data cleaning is required to:

 - Removed unwanted info to keep the closed value column
 - Removed columns and rows with missing data

Then the cleaned data is saved to a CVS file

## **def is_normal(df):**

To check if the close values are following a normal distribution, we used the library **scipy** that allows us to perform a Shapiro test.

## **def is_profitable_5(df):**

To check if the stock could be profitable, we checked if the current value was lower than the mean by at least 5%.

Once everything is tested, the program prints the tickers that passed the tests

