import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("POLYGON_API_KEY")


url=f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit=100&sort=ticker&apiKey={API_KEY}'
response=requests.get(url)
print(response.json())

data=response.json()
print(data.keys()) #print the keys of the json file.

#Extra Exercise :: Modify the script to increase the ticker limit to 1000.
#               :: Save the JSON file of the 1000 tickers to CSV for use by data scientists and analysts 