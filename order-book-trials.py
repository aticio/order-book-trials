import requests

BINANCE_URL = "https://api.binance.com"
DEPTH_PATH = "/api/v3/depth"


def main():
    depth = get_depth()


def get_depth():
    PARAMS = {"symbol": "BTCUSDT", "limit": 10}
    response = requests.get(url=f"{BINANCE_URL}{DEPTH_PATH}", params=PARAMS)
    data = response.json()
    return data


if __name__ == "__main__":
    main()
