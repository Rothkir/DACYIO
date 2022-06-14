import requests

def getID(name):
  r = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/")
  data = r.json()
  entry = next((item for item in data["applist"]["apps"] if item["name"].lower() == name.lower()), None)
  return entry["appid"] if entry else None

def getPrice(ID):
  r = requests.get("http://store.steampowered.com/api/appdetails?appids=" + str(ID) + "&filters=price_overview")
  data = r.json()
  discount = data[str(ID)]['data']['price_overview']['discount_percent']
  price = data[str(ID)]['data']['price_overview']['final_formatted']
  return price, discount

def scrape(game):
  id = getID(game)
  if id == None:
    print("Error! Please write the name of the game correctly")
  else:
    price, discount = getPrice(id)
    return id, price, discount
