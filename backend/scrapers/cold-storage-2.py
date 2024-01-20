import requests
import json
from bs4 import BeautifulSoup, Tag


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
    return temp
    # name


def scrape(category):
    first = requests.get(get_url(category))
    # <li class="last"><a href="/fruits-vegetables/?Product_page=11">

    soup = BeautifulSoup(first.text, features="html.parser")
    print(soup)
    print(soup.select_one(".last > a"))
    print(soup.select_one(".last > a")['href'])
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
    json.dump(scrape("fruits-vegetables"), f)
