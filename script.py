import requests, time, json, sys, os


def collect(auth, mineId):
    headers = {
        'accept':
        '*/*',
        'accept-language':
        'en',
        'app-b':
        '7246500f-89c5-4178-bdc3-d265b960b294',
        'authorization':
        auth,
        'content-type':
        'application/json',
        'origin':
        'https://game.goblinmine.game',
        'priority':
        'u=1, i',
        'referer':
        'https://game.goblinmine.game/',
        'sec-ch-ua':
        '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'same-site',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    json_data = {
        'operationName':
        'pickUp',
        'variables': {
            'input': {
                'mineId': mineId,
                'worldId': 1,
            },
        },
        'query':
        'mutation pickUp($input: PickUpMineInput!) {\n  pickUp(input: $input) {\n    total\n    __typename\n  }\n}',
    }
    response = requests.post('https://api.goblinmine.game/graphql',
                             headers=headers,
                             json=json_data)
    print("Coins collected")


def giveBonus(auth):
    headers = {
        'accept':
        '*/*',
        'accept-language':
        'en',
        'app-b':
        '7246500f-89c5-4178-bdc3-d265b960b294',
        'authorization':
        auth,
        'content-type':
        'application/json',
        'origin':
        'https://game.goblinmine.game',
        'priority':
        'u=1, i',
        'referer':
        'https://game.goblinmine.game/',
        'sec-ch-ua':
        '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'same-site',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    json_data = {
        'operationName':
        'giveBonus',
        'variables': {},
        'query':
        'mutation giveBonus {\n  giveBonus {\n    message\n    status\n    volume\n    __typename\n  }\n}',
    }
    response = requests.post('https://api.goblinmine.game/graphql',
                             headers=headers,
                             json=json_data)


def getMiners(auth, MineId):
    minerToUpgrade = []
    headers = {
        'accept':
        '*/*',
        'accept-language':
        'en',
        'app-b':
        '7246500f-89c5-4178-bdc3-d265b960b294',
        'authorization':
        auth,
        'content-type':
        'application/json',
        'origin':
        'https://game.goblinmine.game',
        'priority':
        'u=1, i',
        'referer':
        'https://game.goblinmine.game/',
        'sec-ch-ua':
        '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'same-site',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    json_data = {
        'operationName':
        'mineAndMiners',
        'variables': {
            'mineId': MineId,
        },
        'query':
        'query mineAndMiners($mineId: Int!) {\n  mine(mineId: $mineId) {\n    ...MINE_FRAGMENT\n    __typename\n  }\n  miners(mineId: $mineId) {\n    ...MINERS_FRAGMENT\n    __typename\n  }\n}\n\nfragment MINE_FRAGMENT on MineFool {\n  deposit_day\n  goblin_image\n  id\n  image\n  income_per_day\n  level\n  miner_amount\n  name\n  price\n  user_miners_count\n  volume\n  userMine {\n    auto\n    cart_level\n    deposit_day\n    deposit_day_default\n    extracted_amount\n    extracted_percent\n    id\n    income_hour\n    next_volume\n    updateIn\n    volume\n    updated_at\n    total_day\n    __typename\n  }\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  miningCurrency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}\n\nfragment MINERS_FRAGMENT on Miners {\n  available\n  id\n  level\n  name\n  price\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  minerLevel {\n    available\n    disabled\n    existInventoryLevel\n    id\n    image\n    income_hour\n    level\n    name\n    price\n    inventoryLevel {\n      level\n      name\n      __typename\n    }\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n  __typename\n}',
    }
    response = requests.post('https://api.goblinmine.game/graphql',
                             headers=headers,
                             json=json_data)
    data = json.loads(response.text)
    miners = data["data"]["miners"]
    for slot in miners:
        if slot["available"] == False:
            buySlot(auth, slot["id"], slot["name"], slot["price"])
        else:
            minerLevels = slot["minerLevel"]
            for minerLevel in minerLevels:
                if minerLevel["available"] == False:
                    buyMinerLevel(auth, minerLevel["id"])


def buyMinerLevel(auth, minerLevelID):
    try:
        headers = {
            'accept':
            '*/*',
            'accept-language':
            'en',
            'app-b':
            '7246500f-89c5-4178-bdc3-d265b960b294',
            'authorization':
            auth,
            'content-type':
            'application/json',
            'origin':
            'https://game.goblinmine.game',
            'priority':
            'u=1, i',
            'referer':
            'https://game.goblinmine.game/',
            'sec-ch-ua':
            '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile':
            '?0',
            'sec-ch-ua-platform':
            '"Windows"',
            'sec-fetch-dest':
            'empty',
            'sec-fetch-mode':
            'cors',
            'sec-fetch-site':
            'same-site',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
        json_data = {
            'operationName':
            'buyMinerLevel',
            'variables': {
                'input': {
                    'minerLevelId': minerLevelID,
                },
            },
            'query':
            'mutation buyMinerLevel($input: BuyMinerLevelInput!) {\n  buyMinerLevel(input: $input) {\n    balance\n    message\n    status\n    __typename\n  }\n}',
        }
        response = requests.post('https://api.goblinmine.game/graphql',
                                 headers=headers,
                                 json=json_data)
        data = json.loads(response.text)
        if data["data"]["buyMinerLevel"]["message"].find(
                "Miner successfully hired") >= 0:
            print("Upgrade Miner Success!")
    except Exception as e:
        # print("[ Buy Miner ]",e)
        pass


def buyCart(auth, cartId):
    try:
        headers = {
            'accept':
            '*/*',
            'accept-language':
            'en',
            'app-b':
            '7246500f-89c5-4178-bdc3-d265b960b294',
            'authorization':
            auth,
            'content-type':
            'application/json',
            'origin':
            'https://game.goblinmine.game',
            'priority':
            'u=1, i',
            'referer':
            'https://game.goblinmine.game/',
            'sec-ch-ua':
            '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile':
            '?0',
            'sec-ch-ua-platform':
            '"Windows"',
            'sec-fetch-dest':
            'empty',
            'sec-fetch-mode':
            'cors',
            'sec-fetch-site':
            'same-site',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
        json_data = {
            'operationName':
            'updateCart',
            'variables': {
                'id': cartId,
            },
            'query':
            'mutation updateCart($id: Int!) {\n  updateCart(id: $id) {\n    volume\n    status\n    message\n    __typename\n  }\n}',
        }
        response = requests.post('https://api.goblinmine.game/graphql',
                                 headers=headers,
                                 json=json_data)
        data = json.loads(response.text)
        message = data["data"]["updateCart"]["message"]
        volume = data["data"]["updateCart"]["volume"]
        if message.find("Cart successfully upgraded") >= 0:
            print("Cart upgrade to", volume)
    except Exception as e:
        # print("[ Buy Cart ]",e)
        pass


def getCarts(auth, mineIndex, mineID):
    headers = {
        'accept':
        '*/*',
        'accept-language':
        'en',
        'app-b':
        '7246500f-89c5-4178-bdc3-d265b960b294',
        'authorization':
        auth,
        'content-type':
        'application/json',
        'origin':
        'https://game.goblinmine.game',
        'priority':
        'u=1, i',
        'referer':
        'https://game.goblinmine.game/',
        'sec-ch-ua':
        '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'same-site',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    json_data = {
        'operationName':
        'carts',
        'variables': {
            'mineId': mineIndex,
            'userMineId': mineID,
        },
        'query':
        'query carts($mineId: Int!, $userMineId: Int!) {\n  carts(mineId: $mineId, userMineId: $userMineId) {\n    auto\n    available\n    id\n    image\n    level\n    name\n    price\n    volume\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    miningCurrency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}',
    }
    response = requests.post('https://api.goblinmine.game/graphql',
                             headers=headers,
                             json=json_data)
    data = json.loads(response.text)
    carts = data["data"]["carts"]
    for cart in carts:
        if cart["available"] == False and cart["auto"] == False:
            buyCart(auth, cart["id"])


def buyMines(auth):
    try:
        for i in range(8):
            i += 1
            headers = {
                'accept':
                '*/*',
                'accept-language':
                'en',
                'app-b':
                '7246500f-89c5-4178-bdc3-d265b960b294',
                'authorization':
                auth,
                'content-type':
                'application/json',
                'origin':
                'https://game.goblinmine.game',
                'priority':
                'u=1, i',
                'referer':
                'https://game.goblinmine.game/',
                'sec-ch-ua':
                '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile':
                '?0',
                'sec-ch-ua-platform':
                '"Windows"',
                'sec-fetch-dest':
                'empty',
                'sec-fetch-mode':
                'cors',
                'sec-fetch-site':
                'same-site',
                'user-agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            }
            json_data = {
                'operationName':
                'buyMine',
                'variables': {
                    'input': {
                        'mineId': i,
                    },
                },
                'query':
                'mutation buyMine($input: BuyMineInput!) {\n  buyMine(input: $input) {\n    message\n    status\n    __typename\n  }\n}',
            }
            response = requests.post('https://api.goblinmine.game/graphql',
                                     headers=headers,
                                     json=json_data)
            data = json.loads(response.text)
            if data["data"]["buyMine"]['status'] != "fail":
                print("Mine #", i, "has been purchased!")
    except Exception as e:
        # print("[ Buy Mines ]",e)
        pass


def buySlot(auth, mineID, mineName, minePrice):
    try:
        headers = {
            'accept':
            '*/*',
            'accept-language':
            'en',
            'app-b':
            '7246500f-89c5-4178-bdc3-d265b960b294',
            'authorization':
            auth,
            'content-type':
            'application/json',
            'origin':
            'https://game.goblinmine.game',
            'priority':
            'u=1, i',
            'referer':
            'https://game.goblinmine.game/',
            'sec-ch-ua':
            '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile':
            '?0',
            'sec-ch-ua-platform':
            '"Windows"',
            'sec-fetch-dest':
            'empty',
            'sec-fetch-mode':
            'cors',
            'sec-fetch-site':
            'same-site',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
        json_data = {
            'operationName':
            'buyMiner',
            'variables': {
                'input': {
                    'minerId': mineID,
                },
            },
            'query':
            'mutation buyMiner($input: BuyMinerInput!) {\n  buyMiner(input: $input) {\n    message\n    status\n    __typename\n  }\n}',
        }
        response = requests.post('https://api.goblinmine.game/graphql',
                                 headers=headers,
                                 json=json_data)
        data = json.loads(response.text)
        message = data["data"]["buyMiner"]["message"]
        if message.find("The miners are successfully hired") >= 0:
            print("Buying", mineName, "for", minePrice)
    except Exception as e:
        # print("[ Buying Slot ]",e)
        pass


def getMines(auth):
    headers = {
        'accept':
        '*/*',
        'accept-language':
        'en',
        'app-b':
        '7246500f-89c5-4178-bdc3-d265b960b294',
        'authorization':
        auth,
        'content-type':
        'application/json',
        'origin':
        'https://game.goblinmine.game',
        'priority':
        'u=1, i',
        'referer':
        'https://game.goblinmine.game/',
        'sec-ch-ua':
        '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'same-site',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName':
        'minesAndCheckTasksCompleted',
        'variables': {
            'worldId': 1,
        },
        'query':
        'query minesAndCheckTasksCompleted($worldId: Int!) {\n  mines(worldId: $worldId) {\n    ...MINE_FRAGMENT\n    __typename\n  }\n  check_tasks_completed(worldId: $worldId)\n}\n\nfragment MINE_FRAGMENT on MineFool {\n  deposit_day\n  goblin_image\n  id\n  image\n  income_per_day\n  level\n  miner_amount\n  name\n  price\n  user_miners_count\n  volume\n  userMine {\n    auto\n    cart_level\n    deposit_day\n    deposit_day_default\n    extracted_amount\n    extracted_percent\n    id\n    income_hour\n    next_volume\n    updateIn\n    volume\n    updated_at\n    total_day\n    __typename\n  }\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  miningCurrency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}',
    }
    response = requests.post('https://api.goblinmine.game/graphql',
                             headers=headers,
                             json=json_data)
    data = json.loads(response.text)
    mines = data['data']["mines"]
    try:
        for x, mine in enumerate(mines):
            x += 1
            mineIndex = mine["id"]
            mine = mine["userMine"]
            mineID = mine["id"]
            print("[ Mine #",
                  x,
                  "] Cart level",
                  mine['cart_level'],
                  ">>",
                  format(mine["extracted_amount"], ".2f"),
                  "/",
                  mine["volume"],
                  end=" | ")
            collect(auth, mineID)
            getInventory(auth, mineIndex)
            getTnt(auth, mineIndex)
            getCarts(auth, mineIndex, mineID)
            getMiners(auth, mineIndex)
    except Exception as e:
        # print(e)
        # sys.exit()
        pass
    print("==============================")


def buyInventory(auth, upgradeID, inventoryName):
    try:
        for _ in range(10):
            headers = {
                'accept':
                '*/*',
                'accept-language':
                'en',
                'app-b':
                '7246500f-89c5-4178-bdc3-d265b960b294',
                'authorization':
                auth,
                'content-type':
                'application/json',
                'origin':
                'https://game.goblinmine.game',
                'priority':
                'u=1, i',
                'referer':
                'https://game.goblinmine.game/',
                'sec-ch-ua':
                '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile':
                '?0',
                'sec-ch-ua-platform':
                '"Windows"',
                'sec-fetch-dest':
                'empty',
                'sec-fetch-mode':
                'cors',
                'sec-fetch-site':
                'same-site',
                'user-agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            }
            json_data = {
                'operationName':
                'buyInventory',
                'variables': {
                    'id': upgradeID,
                },
                'query':
                'mutation buyInventory($id: Int!) {\n  buyInventory(id: $id) {\n    message\n    volume\n    status\n    __typename\n  }\n}',
            }
            response = requests.post('https://api.goblinmine.game/graphql',
                                     headers=headers,
                                     json=json_data)
            data = json.loads(response.text)
            message = data["data"]["buyInventory"]["message"]
            if message.find("Level upgraded") >= 0:
                print("Inventory Upgrade", inventoryName)
            else:
                break
    except Exception as e:
        # print("[Buy Inventory]",e)
        pass


def getInventory(auth, mineIndex):
    headers = {
        'accept':
        '*/*',
        'accept-language':
        'en',
        'app-b':
        '7246500f-89c5-4178-bdc3-d265b960b294',
        'authorization':
        auth,
        'content-type':
        'application/json',
        'origin':
        'https://game.goblinmine.game',
        'priority':
        'u=1, i',
        'referer':
        'https://game.goblinmine.game/',
        'sec-ch-ua':
        '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'same-site',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    json_data = {
        'operationName':
        'inventory',
        'variables': {
            'mineId': mineIndex,
        },
        'query':
        'query inventory($mineId: Int!) {\n  inventory(mineId: $mineId) {\n    disabled\n    id\n    image\n    income_hour\n    level\n    name\n    price\n    inventory_income_hour\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}',
    }
    response = requests.post('https://api.goblinmine.game/graphql',
                             headers=headers,
                             json=json_data)
    data = json.loads(response.text)
    upgrades = data["data"]["inventory"]
    for upgrade in upgrades:
        if upgrade["disabled"] == False:
            buyInventory(auth, upgrade["id"], upgrade["name"])


def upgradeTnt(auth, tntID, tntName, tntPrice):
    try:
        headers = {
            'accept':
            '*/*',
            'accept-language':
            'en',
            'app-b':
            '7246500f-89c5-4178-bdc3-d265b960b294',
            'authorization':
            auth,
            'content-type':
            'application/json',
            'origin':
            'https://game.goblinmine.game',
            'priority':
            'u=1, i',
            'referer':
            'https://game.goblinmine.game/',
            'sec-ch-ua':
            '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile':
            '?0',
            'sec-ch-ua-platform':
            '"Windows"',
            'sec-fetch-dest':
            'empty',
            'sec-fetch-mode':
            'cors',
            'sec-fetch-site':
            'same-site',
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }
        json_data = {
            'operationName':
            'buyUpgradeMine',
            'variables': {
                'id': tntID,
            },
            'query':
            'mutation buyUpgradeMine($id: Int!) {\n  buyUpgradeMine(id: $id) {\n    message\n    status\n    volume\n    __typename\n  }\n}',
        }
        response = requests.post('https://api.goblinmine.game/graphql',
                                 headers=headers,
                                 json=json_data)
        data = json.loads(response.text)
        message = data["data"]["buyUpgradeMine"]["message"]
        if message.find("Level upgraded") >= 0:
            print("Uprading", tntName, "for", tntPrice)
    except Exception as e:
        # print("[Upgrade TNT]",e)
        pass


def getTnt(auth, mineIndex):
    headers = {
        'accept':
        '*/*',
        'accept-language':
        'en',
        'app-b':
        '7246500f-89c5-4178-bdc3-d265b960b294',
        'authorization':
        auth,
        'content-type':
        'application/json',
        'origin':
        'https://game.goblinmine.game',
        'priority':
        'u=1, i',
        'referer':
        'https://game.goblinmine.game/',
        'sec-ch-ua':
        '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'same-site',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    json_data = {
        'operationName':
        'mineAndUpgradeMine',
        'variables': {
            'mineId': mineIndex,
        },
        'query':
        'query mineAndUpgradeMine($mineId: Int!) {\n  mine(mineId: $mineId) {\n    ...MINE_FRAGMENT\n    __typename\n  }\n  upgradeMine(mineId: $mineId) {\n    ...UPGRADE_MINE_FRAGMENT\n    __typename\n  }\n}\n\nfragment MINE_FRAGMENT on MineFool {\n  deposit_day\n  goblin_image\n  id\n  image\n  income_per_day\n  level\n  miner_amount\n  name\n  price\n  user_miners_count\n  volume\n  userMine {\n    auto\n    cart_level\n    deposit_day\n    deposit_day_default\n    extracted_amount\n    extracted_percent\n    id\n    income_hour\n    next_volume\n    updateIn\n    volume\n    updated_at\n    total_day\n    __typename\n  }\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  miningCurrency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}\n\nfragment UPGRADE_MINE_FRAGMENT on upgradeMine {\n  id\n  image\n  level\n  name\n  price\n  disabled\n  deposit_day\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  need_inventory {\n    level\n    name\n    __typename\n  }\n  __typename\n}',
    }
    response = requests.post('https://api.goblinmine.game/graphql',
                             headers=headers,
                             json=json_data)
    data = json.loads(response.text)
    tnts = data["data"]["upgradeMine"]
    for tnt in tnts:
        if tnt["disabled"] == False:
            upgradeTnt(auth, tnt["id"], tnt["name"], tnt["price"])


tken = [
    "54928203|UeW6xRyX2HCYMbqZ6T0qmkRKRFxRLaAxv3QrVdeV646fb833",
    "55260196|syEA7xurwKczsyOmvqF7grmNiL9wIv4obZrTsrEq41801573",
    "55301956|MbeW9JF0ppnBtJFvSigqVzU4lHjRXNBkA3SM4IeW14d986bc",
    "56122987|9Z9pUyEZe25DHLjMBWQEafwZJMs9YA4ejmO8pv3K76a44cb5",
    "68447305|OXxm63JIhoC1LerQmLNF9FZ9OVHNSTpp9WcVc29Ac4141616",
    "68489663|D3inUlyuDbKLfD19TGqvfJQAAwLbKZjntdnN3ayGccdc4caa"
]
aliases = ["CA", "DI", "MA", "CON", "VIA", "VIA-Dito"]

os.system("cls")

while True:
    for i in range(len(tken)):
        alias = aliases[i]
        token = tken[i]
        info = 'Bearer ' + token
        print('Bot is running . . .')
        print(f"Processing Acount {alias}...")
        buyMines(info)
        giveBonus(info)
        getMines(info)
        print('Sleeping for 1 minute . . .')
        time.sleep(20)

    print('Sleeping for 10 minutes . . .')
    print('This script is free and not for sale!')
    time.sleep(600)
