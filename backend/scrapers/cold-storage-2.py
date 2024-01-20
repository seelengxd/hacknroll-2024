import requests
import json
from bs4 import BeautifulSoup, Tag

CATEGORIES = ["delicatessen", "our-exclusive-brands", "mum-baby", "health-beauty", "home-kitchen-cleaning", "meat-seafood", "fruits-vegetables", "snacks-drinks", "ready-meals",
              "dairy-chilled-frozen", "bakery-cereal-spreads", "beers-wines-spirits", "food-pantry", "organic-sustainable"]  # "art-kit-sale", "australia-fair", "organic-produce"]


def get_url(category, page_number=1):
    return f"https://coldstorage.com.sg/{category}/?Product_page={page_number}"


def parse_product(product: Tag, category: str):
    temp = {}
    temp["name"] = product.select_one(".product_name").text.strip()
    if product.select_one(".category-name"):
        temp["brand"] = product.select_one(".category-name").text.strip()
    else:
        temp["brand"] = None
    temp["price"] = product.select_one(".price_now").text.strip()
    if product.select_one(".price_promo"):
        temp["offer_display"] = product.select_one(".price_promo").text.strip()
    else:
        temp["offer_display"] = None
    temp["image_url"] = product.select_one("img")["src"]
    temp["url_to_product"] = product.select_one(
        ".product_box > a")["href"]
    temp["category"] = category
    if product.select_one(".price_discount > span"):
        temp["prev_price"] = product.select_one(
            ".price_discount > span").text.strip()
    if product.select_one(".size"):
        temp["size"] = product.select_one(".size").text
    return temp


def scrape(category):
    first = requests.get(get_url(category))

    soup = BeautifulSoup(first.text, features="html.parser")
    page_limit = int(soup.select_one(".last > a")['href'].split("=")[-1])
    data = []
    for i in range(1, page_limit + 1):
        resp = requests.get(get_url(category, i))
        soup = BeautifulSoup(resp.text, features="html.parser")
        for product in soup.select(".product_box"):
            data.append(parse_product(product, category))
    return data
    # name


with open("cs.json", "w") as f:
    data = {}
    for category in CATEGORIES:
        print("Scraping Category:", category)
        data[category] = scrape(category)
    json.dump(data, f)
