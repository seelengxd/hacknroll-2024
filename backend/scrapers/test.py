import sys
from tqdm import tqdm
import spacy
import difflib
import json

with open("full_data.json") as f:
    data = json.load(f)
    data = [i for i in data if i['market_id'] != 4]

# Brand logic:
brands = set(i["brand"].lower() if i["brand"] else i["brand"] for i in data)
# brands

# difflib.SequenceMatcher(None, a, b).ratio()
n = len(brands)
brands = list(brands)
# combis = []
# for i in range(n):
#     for j in range(i + 1, n):
#         if brands[i] and brands[j]:
#             combis.append((brands[i], brands[j], difflib.SequenceMatcher(
#                 None, brands[i], brands[j]).ratio()))


x = [brand for brand in brands if brand]
x.sort()

with open("brands.txt", "w") as f:
    for brand in x:
        f.write(brand + "\n")

for d in data:
    if d["brand"]:
        d["treated_brand"] = d["brand"].lower().replace(
            " ", "").replace("-", "").replace("'", "")
    else:
        d["treated_brand"] = "NONE"


nlp = spacy.load("en_core_web_lg")

similarity_mat = []


def sim_score(a, b):
    # a_s = f"{a['brand']} {a['name']}".lower()
    # b_s = f"{a['brand']} {b['name']}".lower()
    a_s = f"{a['name']}".lower()
    b_s = f"{b['name']}".lower()
    doc1 = nlp(a_s)
    doc2 = nlp(b_s)
    return doc1.similarity(doc2)


b2d = {}
for d in data:
    b2d.setdefault(d["treated_brand"], [])
    b2d[d["treated_brand"]].append(d)


class UFDS:
    def __init__(self, n, products):
        self.par = [-1] * n
        self.rank = [0] * n
        self.one = [0] * n
        self.two = [0] * n
        self.three = [0] * n
        for index, product in enumerate(products):
            if product["market_id"] == 1:
                self.one[index] = 1
            elif product["market_id"] == 2:
                self.two[index] = 1
            else:
                self.three[index] = 1

    def root(self, i):
        if self.par[i] == -1:
            return i
        else:
            self.par[i] = self.root(self.par[i])
            return self.par[i]

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def union(self, i, j):
        if self.is_connected(i, j):
            return

        pi = self.root(i)
        pj = self.root(j)

        # if same merchant linked already, ABORT
        if (self.one[pi] and self.one[pj]) or (self.two[pi] and self.two[pj]) or (self.three[pi] and self.three[pj]):
            return
        if self.rank[pi] <= self.rank[pj]:
            self.par[pi] = pj
            self.rank[pj] += 1
            # OR
            self.one[pj] = self.one[pi] or self.one[pj]
            self.two[pj] = self.two[pi] or self.two[pj]
            self.three[pj] = self.three[pi] or self.three[pj]
            self.one[pi] = self.one[pi] or self.one[pj]
            self.two[pi] = self.two[pi] or self.two[pj]
            self.three[pi] = self.three[pi] or self.three[pj]
        else:
            self.par[pj] = pi
            self.rank[pi] += 1

            # OR
            self.one[pi] = self.one[pi] or self.one[pj]
            self.two[pi] = self.two[pi] or self.two[pj]
            self.three[pi] = self.three[pi] or self.three[pj]
            self.one[pj] = self.one[pi] or self.one[pj]
            self.two[pj] = self.two[pi] or self.two[pj]
            self.three[pj] = self.three[pi] or self.three[pj]


# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         length = len(accounts)
#         ufds = UFDS(length)
#         emails = {}
#         for index, account in enumerate(accounts):
#             name, *acc_emails = account
#             for email in acc_emails:
#                 if email in emails:
#                     ufds.union(emails[email], index)
#                 else:
#                     emails[email] = index

#         to_merge = [ufds.root(i) for i in range(length)]
#         merged = {}
#         for index, parent in enumerate(to_merge):
#             if parent not in merged:
#                 merged[parent] = (accounts[index][0], set(accounts[index][1:]))
#             else:
#                 merged[parent] = (merged[parent][0], merged[parent][1].union(set(accounts[index][1:])))
#         return [[name] + sorted(email) for name, email in merged.values()]
print(len(b2d))

process_index = int(sys.argv[1])

out = []
count = 0
# l = 0
keys = sorted(b2d.keys())
for index, key in enumerate(keys):
    if index % 10 == process_index:
        print(count)
        brand_data = b2d[key]
        if key == "NONE":
            continue
        n = len(brand_data)
        ufds = UFDS(n, brand_data)
        print(key, n)
        for i in range(n):
            print(i)
            highest_sim = -1
            paired = None
            for j in range(i + 1, n):
                a = brand_data[i]
                b = brand_data[j]
                # if same merchant, skip
                if a["market_id"] == b["market_id"]:
                    continue
                else:
                    ratio = sim_score(a, b)
                    if ratio > highest_sim:
                        highest_sim = ratio
                        paired = j
            if highest_sim > 0.75 and paired != None:
                ufds.union(i, paired)
        for i in range(n):
            brand_data[i]["key"] = (key, ufds.root(i))
        out.append(brand_data)
        count += 1
        # if count == 15:

with open(f"dumb-out-{process_index}.json", "w") as f:
    json.dump(out, f)


# print(b2d)
# for brand, brand_data in b2d.items():
#     if brand == "NONE":
#         continue
#     n = len(brand_data)
#     ufds = UFDS(n)
#     print(brand, n)
#     for i in range(n):
#         print(i)
#         for j in range(i + 1, n):
#             a = brand_data[i]
#             b = brand_data[j]
#             # if same merchant, skip
#             if a["market_id"] == b["market_id"]:
#                 continue
#             else:
#                 ratio = sim_score(a, b)
#                 if ratio > 0.67:
#                     ufds.union(i, j)
#     for i in range(n):
#         brand_data[i]["key"] = (brand, ufds.root(i))

# else use comparator
