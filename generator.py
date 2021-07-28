import requests


def create_wallet(type):
    type = type.lower()
    if is_supported_symbols(type) == False:
        return None
    url = "https://tokenwallet.one/create/" + type
    result = requests.get(url)
    if result.status_code == 200:
        json_data = result.json()
        return json_data["symbol"], json_data["addr"], json_data["privateKey"]
    return None


def is_supported_symbols(type):
    supported_symbols = ["btc", "eth", "etc", "heco", "bsc", "okt", "trx",
                         "usdt_erc20", "usdt_trc20", "usdt_omni", "eos",
                         "bch", "fil", "bsv", "vet", "matic", "ltc", "dash", "doge",
                         "atom", "xmr", "waves", "xrp", "bnb", "neo", "ont", "xlm", "pote", "club"]
    if type in supported_symbols:
        return True
    return False


if __name__ == "__main__":
    print(create_wallet("btc"))
    print(create_wallet("eth"))
    print(create_wallet("etc"))
    print(create_wallet("heco"))
    print(create_wallet("bsc"))
    print(create_wallet("okt"))
    print(create_wallet("trx"))
    print(create_wallet("usdt_erc20"))
    print(create_wallet("usdt_trc20"))
    print(create_wallet("usdt_omni"))
    print(create_wallet("eos"))
    print(create_wallet("bch"))
    print(create_wallet("fil"))
    print(create_wallet("bsv"))
    print(create_wallet("vet"))
    print(create_wallet("matic"))
    print(create_wallet("ltc"))
    print(create_wallet("dash"))
    print(create_wallet("doge"))
    print(create_wallet("atom"))
    print(create_wallet("xmr"))
    print(create_wallet("waves"))
    print(create_wallet("xrp"))
    print(create_wallet("bnb"))
    print(create_wallet("neo"))
    print(create_wallet("ont"))
    print(create_wallet("xlm"))
    print(create_wallet("pote"))
    print(create_wallet("club"))
