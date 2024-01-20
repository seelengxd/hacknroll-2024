from algoliasearch.search_client import SearchClient
import json

client = SearchClient.create('PFCHI1YM66', 'd0c09a40111717aec861992cf8497e71')
index = client.init_index("coldstorage_product_live")
# coldstorage_product_live
# coldstorage_article_live

# there are 12 pages
records = []
for i in range(1, 13):
    records.append(index.search("", {'hitsPerPage': 1000}))

hits = []
for record in records:
    hits += record["hits"]

with open("data2.json", "w") as f:
    json.dump(records, f)

with open("data3.json", "w") as f:
    json.dump(hits, f)
