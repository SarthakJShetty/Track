'''Hello! This is the first script to trial run tracking financial data from Yahoo! Finance.
Not sure where this is going to go, but seems exciting.
First project of 2019.

Happy New Year 2019!
- Sarthak J Shetty (02/01/2019)'''

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url="https://finance.yahoo.com/quote/AAPL/"
page=urlopen(url)
soup=bs(page, 'html.parser')
print(soup.find('span', {'class':'Trsdu(0.3s)'}).text)