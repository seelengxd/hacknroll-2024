# importing the requests library
import requests
import json
import time
from random import random

categories = [
  "shop-Groceries-FoodStaplesCookingEssentials",
  "shop-groceries-fresh-produce",
  "meat-and-seafood",
  "beverages",
  "shop-household-supplies",
  "mother-baby",
  "shop-Groceries-DairyChilled",
  "shop-groceries-frozen",
  "breakfast",
  "shop-Groceries-ChocolateSnacksSweets",
  "wines-beers-spirits",
  "shop-health-beauty",
  "shop-health",
  "shop-pet-supplies",
  "shop-party-supplies",
  "shop-kitchen-dining"
]

category_displays = [
  "Food Staples & Cooking Essentials",
  "Fresh Produce",
  "Meat & Seafood",
  "Beverages",
  "Household Supplies",
  "Mother & Baby",
  "Dairy",
  "Frozen",
  "Bakery",
  "Snacks and Sweets",
  "Wines Beers & Spirits",
  "Beauty",
  "Health",
  "Pet Supplies",
  "Party Supplies",
  "Kitchen & Dining"
]

end_page = [102, 28, 24, 102, 102, 102, 93, 102, 52, 102, 102, 102, 102, 102, 89, 102]
 
# api-endpoint
URL = "https://redmart.lazada.sg/{category}/?ajax=true&isFirstRequest=true&m=redmart&page={page}&spm=a2o42.redmart_home.nav_category_tree.119.e7ea9917bbKPdX"
NUM = 16
INDEX = NUM - 1
CATEGORY = categories[INDEX]
CATEGORY_DISPLAY = category_displays[INDEX]
PAGE_END = end_page[INDEX]
PAGE_START = 1

data = []
names = set({})
new_names = []
count = 0

# append current items
with open("redmart_names.txt", "r") as f:
  for line in names:
    names.add(line)

# sending get request and saving the response as response object
for page in range(PAGE_START, PAGE_END + 1):
  time.sleep(random() + 0.5)
  try:
    r = requests.get(url = URL.format(category = CATEGORY, page = page))
    # extracting data in json format
    response = r.json()
  except:
    print(r.text)
    print('error', URL.format(category = CATEGORY, page = page))
    quit()

  if 'listItems' not in response['mods']:
    break

  # extracting data
  items = response['mods']['listItems']
  
  # printing the output
  print(page)

  for item in items:
    # print(item['name'])
    if item['name'] in names:
      continue
    names.add(item['name'])
    obj = {
      "name": item['name'],
      "image_url": item['image'],
      "product_url": item['productUrl'],
      "category": CATEGORY_DISPLAY,
      "brand": item['brandName'],
      "in_stock": item['inStock'],
    }
    if 'originalPrice' in item :
      obj['price'] = item['originalPrice']
      obj['promo_price'] = item['price']
      obj['discount'] = item['discount']
    else:
      obj['price'] = item['price']
      obj['promo_price'] = ''
      obj['discount'] = ''
    
    if 'packageInfo' in item:
      obj['package_info'] = item['packageInfo']
    else:
      obj['package_info'] = ''

    data.append(obj)
    new_names.append(obj['name'])
    count += 1

with open("redmart_data.json") as f:
    all = json.load(f)

with open("redmart_data.json", "w") as f:
    all.append(data)
    json.dump(all, f)

with open("redmart_names.txt", "a") as f:
  for line in new_names:
    f.write(line + "\n")
  
print("new:", count)
print("current:", len(all))

# names = []

# with open('redmart_data.json') as f:
#   d = json.load(f)

# with open('redmart_data.json', 'w') as f:
#   for value in d:
#     d.append(data)
#   json.dump(d, f)
    
# with open("redmart_names.txt", "w") as f:
#     for line in names:
#        f.write(line + "\n")
