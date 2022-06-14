import requests
from bs4 import BeautifulSoup

def get_prices(name):
  url = 'https://www.g2a.com/search'
  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-GPC": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
  }
  r = requests.get(url, headers=headers, params={"query": name})

  soup = BeautifulSoup(r.text, 'html.parser')

  root = soup.find(class_="indexes__StyledWrapper-wklrsw-202 hknbAv")
  ul_normal = root.contents[1]

  results = []
  for li_children in ul_normal.children:
    results.append({
        "name": li_children.h3.a.text,
        "price": "$" + li_children.span.span.text,
        "discount": int(li_children.contents[1].div.contents[2].contents[1].text[1:-1]) if len(li_children.contents[1].div.contents) > 2 else 0
    })

  data = results[0]
  price = data['price']
  discount = data['discount']
  return price, discount