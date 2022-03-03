from bs4 import BeautifulSoup
import requests


"""
Everything is Clear. Just a Simple Beautiful Soup Project :)
"""

url = "https://coinmarketcap.com/"
r = requests.get(url).text
doc = BeautifulSoup(r, "html.parser")

trs = doc.tbody.contents

prices = {}

for tr in trs:
    name, price = tr.contents[2:4]
    if name.p is not None:
        name_cr = name.p["class"] == ['sc-1eb5slv-0', 'iworPT']
        if name_cr:
            prices[name.p.string] = price.span.string

print(prices)
