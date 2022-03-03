from bs4 import BeautifulSoup
import requests


"""
- Enter name of product
- Searching for it in newegg website 
- Return results in a dictionary
- Sort by price --> LOWER TO HIGHER
- Write all related Products in a file  
"""

search_text = input("What Item Do You Want Search? \n")

url = f"https://www.newegg.ca/p/pl?d={search_text}&N=4131"
r = requests.get(url).text
doc = BeautifulSoup(r, "html.parser")

# return all related pages
pages_number = doc.find(class_="list-tool-pagination-text").strong
sp_number = str(pages_number).split("/")
pages = int(sp_number[1].split("<")[1].split(">")[1])

results = {}  # all results

for page in range(1, pages+1):
    """
    Iterate on all related pages
    """
    url = f"https://www.newegg.ca/p/pl?d={search_text}&N=4131&page={page}"
    r = requests.get(url).text
    doc = BeautifulSoup(r, "html.parser")

    div = doc.find(
        class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(class_="item-cell")
    for item in items:
        try:
            link = item.a["href"]
            price = item.find(class_="price-current").strong.string
            title = item.find(class_="item-title").string
            results[title] = {"price": price.replace(",", ""), "link": link}
        except:
            pass

sorted_dict = sorted(results.items(), key=lambda x: x[1]["price"])  # sort results by price

# write all sorted products in a file
with open(search_text.replace(" ", "-")+".txt", "w") as f:
    f.write(str(sorted_dict))
