from codecs import utf_16_be_decode
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.brainyquote.com/quote_of_the_day').text
soup = BeautifulSoup(source, "lxml")

print(
    """▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄ █ ██ █▀▄▄▀█▄ ▄█ ▄▄████ ▄▄▄ █ ▄▄███▄▄ ▄▄█ ████ ▄▄████ ▄▄▀█ ▄▄▀█ ██ 
██ ██ █ ██ █ ██ ██ ██ ▄▄████ ███ █ ▄██████ ███ ▄▄ █ ▄▄████ ██ █ ▀▀ █ ▀▀ 
██▄▄ ▀██▄▄▄██▄▄███▄██▄▄▄████ ▀▀▀ █▄███████ ███▄██▄█▄▄▄████ ▀▀ █▄██▄█▀▀▀▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

"""
)

quote = soup.find("div", class_="grid-item qb clearfix bqQt").text
qt = str(quote).replace('\n\n', ' ')
print("\033[1m" + qt + "\033[0m")
