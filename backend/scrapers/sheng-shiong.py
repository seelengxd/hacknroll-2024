#!/usr/bin/env python

import asyncio
import json
from websockets.sync.client import connect

# ["{\"msg\":\"connect\",\"version\":\"1\",\"support\":[\"1\",\"pre2\",\"pre1\"]}"]
categories = [
    "fruits",
    "vegetables",
    "meat-poultry-seafood",
    "breakfast-spreads",
    "dairy-chilled-eggs",
    "snacks-confectioneries",
    "beverages",
    "alcohol",
    "rice-noodles-pasta",
    "cooking-baking-needs",
    "convenience-food-113",
    "frozen-goods",
    "dried-food-herbs",
    "mum-baby-kids",
    "health-beauty",
    "household",
    "lifestyle-outdoors",
    "pet-care",
    "carton-deals"
]

CONNECTION = {"msg": "connect", "version": "1",
              "support": ["1", "pre2", "pre1"]}

TEST = {"msg": "method", "id": "6", "method": "Sessions.getSessionDataByKey",
        "params": [{"sessionKey": "p2GS77PS6k8oDN4RLQjuxOpEq3DAoo"}]}

FRUITS_COUNT = {"msg": "method", "id": "35", "method": "Products.getCountByAllSlugs", "params": [{"categoryFilter": {"slugs": ["fruits"]}, "campaignPageFilter": {"slug": "", "category": {"slug": ""}}, "shoppingListFilter": {"slug": "", "category": {"slug": ""}, "search": {
    "slug": ""}, "showKeptForLater": False}, "searchFilter": {"slug": "", "category": {"slug": ""}}}, {"brands": {"slugs": []}, "prices": {"slugs": []}, "countryOfOrigins": {"slugs": []}, "dietaryHabits": {"slugs": []}, "tags": {"slugs": []}, "sortBy": {"slug": ""}}]}

# FRUITS2 = {"msg": "method", "id": "36", "method": "Products.getByAllSlugs", "params": [{"categoryFilter": {"slugs": ["fruits"]}, "campaignPageFilter": {"slug": "", "category": {"slug": ""}}, "shoppingListFilter": {"slug": "", "category": {"slug": ""}, "search": {
#     "slug": ""}, "showKeptForLater": False}, "searchFilter": {"slug": "", "category": {"slug": ""}}}, {"brands": {"slugs": []}, "prices": {"slugs": []}, "countryOfOrigins": {"slugs": []}, "dietaryHabits": {"slugs": []}, "tags": {"slugs": []}, "sortBy": {"slug": ""}}, 1, ]}

TEST2 = {"msg": "method", "id": "36", "method": "Products.getByAllSlugs", "params": [{"campaignPageFilter": {"slug": "", "category": {"slug": ""}}, "shoppingListFilter": {"slug": "", "category": {"slug": ""}, "search": {
    "slug": ""}, "showKeptForLater": False}, "searchFilter": {"slug": "", "category": {"slug": ""}}}, {"brands": {"slugs": []}, "prices": {"slugs": []}, "countryOfOrigins": {"slugs": []}, "dietaryHabits": {"slugs": []}, "tags": {"slugs": []}, "sortBy": {"slug": ""}}, 1, 80]}


def prepare_message(data: dict):
    return json.dumps([json.dumps(data)])


def extract_message(message: str):
    data = json.loads(json.loads(message[1:])[0])
    if "result" in data:
        return data["result"]
    else:
        return data


def scrape_category(websocket, category: str):
    print("scraping category", category)
    count_msg = {"msg": "method", "id": "35", "method": "Products.getCountByAllSlugs", "params": [{"categoryFilter": {"slugs": [category]}, "campaignPageFilter": {"slug": "", "category": {"slug": ""}}, "shoppingListFilter": {"slug": "", "category": {"slug": ""}, "search": {
        "slug": ""}, "showKeptForLater": False}, "searchFilter": {"slug": "", "category": {"slug": ""}}}, {"brands": {"slugs": []}, "prices": {"slugs": []}, "countryOfOrigins": {"slugs": []}, "dietaryHabits": {"slugs": []}, "tags": {"slugs": []}, "sortBy": {"slug": ""}}]}
    while True:
        websocket.send(prepare_message(count_msg))
        while True:
            msg = extract_message(websocket.recv())
            if "count" in msg:
                count = msg["count"]
                break
        request_msg = {"msg": "method", "id": "36", "method": "Products.getByAllSlugs", "params": [{"categoryFilter": {"slugs": [category]}, "campaignPageFilter": {"slug": "", "category": {"slug": ""}}, "shoppingListFilter": {"slug": "", "category": {"slug": ""}, "search": {
            "slug": ""}, "showKeptForLater": False}, "searchFilter": {"slug": "", "category": {"slug": ""}}}, {"brands": {"slugs": []}, "prices": {"slugs": []}, "countryOfOrigins": {"slugs": []}, "dietaryHabits": {"slugs": []}, "tags": {"slugs": []}, "sortBy": {"slug": ""}}, 1, count]}
        websocket.send(prepare_message(request_msg))
        while True:
            msg = extract_message(websocket.recv())
            if type(msg) == list and len(msg) and "_id" in msg[0]:
                return msg
            else:
                print(msg)


def hello():

    with connect("wss://shengsiong.com.sg/sockjs/931/kkffcydo/websocket") as websocket:
        # msg = json.dumps({"msg": "method", "id": "6", "method": "Sessions.getSessionDataByKey", "params": [
        #                  {"sessionKey": "p2GS77PS6k8oDN4RLQjuxOpEq3DAoo"}]})
        # print(msg)
        websocket.send(prepare_message(CONNECTION))

        websocket.recv()
        session_msg = websocket.recv()
        print(session_msg)
        session_key = extract_message(session_msg)["session"]
        print(session_key)

        with open("ss.json", "w") as f:
            all = {}
            for category in categories:
                data = scrape_category(websocket, category)
                all[category] = data
            json.dump(all, f)

        # websocket.send(prepare_message(TEST))

        # websocket.send(prepare_message(FRUITS_COUNT))

        # websocket.send(prepare_message(FRUITS2))
        # # websocket.send(
        # #       [{"msg":"connect\",\"version\":\"1\",\"support\":[\"1\",\"pre2\",\"pre1\"]}])
        # #     json.dumps([msg]))
        # while True:
        #     message = websocket.recv()
        #     # print(type(message))
        #     # print(f"Received: {message}")
        #     print(extract_message(message))
        #     msg = extract_message(message)
        #     if isinstance(msg, list):
        #         msg = msg[0]

        #     if "price" in str(msg):
        #         with open("ss.json", "w") as f:
        #             json.dump(msg, f)
# {"msg":"method","id":"6","method":"Sessions.getSessionDataByKey","params":[{"sessionKey":"p2GS77PS6k8oDN4RLQjuxOpEq3DAoo"}]}


hello()
