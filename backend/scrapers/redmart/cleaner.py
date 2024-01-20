import json

REDMART_ENUM = 4
clean = []
names = set({})

with open("redmart_data.json") as f:
  data = json.load(f)

def convertNones(item):
  for key, value in item.items():
    if value == '':
      item[key] = None

  return item

def checkNullableType(value, type):
  return value == None or isinstance(value, type)

def checkTypes(item):
  if not checkNullableType(item['name'], str):
    raise Exception("Invalid type detected for ", item['name'])

  if not checkNullableType(item['brand'], str):
    raise Exception("Invalid type detected for " + item['name'], item['brand'])
  
  if not checkNullableType(item['price'], float):
    try:
      item['price'] = float(item['price'])
    except:
      raise Exception("Invalid type detected for " + item['name'], item['price'])
  
  if not checkNullableType(item['in_stock'], bool):
    raise Exception("Invalid type detected for " + item['name'], item['in_stock'])
  
  if not checkNullableType(item['package_info'], str):
    raise Exception("Invalid type detected for " + item['name'], item['package_info'])
  
  if not checkNullableType(item['promo_price'], float):
    try:
      item['promo_price'] = float(item['promo_price'])
    except:
      raise Exception("Invalid type detected for " + item['name'], item['promo_price'])

  if not checkNullableType(item['discount'], str):
    raise Exception("Invalid type detected for " + item['name'], item['discount'])
    
  if not checkNullableType(item['image_url'], str):
    raise Exception("Invalid type detected for " + item['name'], item['image_url'])
  
  if not checkNullableType(item['product_url'], str):
    raise Exception("Invalid type detected for " + item['name'], item['product_url'])

  return item

def extractValues(item):
  product = {}
  product['market_id'] = REDMART_ENUM
  product['barcodes'] = None
  product['brand'] = item['brand']
  product['price'] = item['price']
  product['availability'] = item['in_stock']
  product['name'] = item['name']
  product['image'] = item['image_url']
  product['quantity'] = item['package_info']
  product['offer_qty'] = None
  product['offer_price'] = item['promo_price']
  product['offer_desc'] = item['discount']
  product['product_url'] = item['product_url'].lstrip("/")

  return product

print("Checking types and converting Nones...")

for item in data:
  item = convertNones(item)
  item = checkTypes(item)

print("Extracting values...")

for item in data:
  product = extractValues(item)
  clean.append(product)

print("Writing cleaned values...")

with open("clean_redmart_data.json", "w") as f:
  json.dump(clean, f)
