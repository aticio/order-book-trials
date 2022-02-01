import requests
import schedule
import time

BINANCE_URL = "https://api.binance.com"
DEPTH_PATH = "/api/v3/depth"


def main():
    schedule.every().second.do(init)

    while True:
        schedule.run_pending()
        time.sleep(1)


def init():
    depth = get_depth()
    bids = depth["bids"]
    asks = depth["asks"]

    total_bids = 0
    total_asks = 0

    for b in bids:
        total_bids = total_bids + (float(b[0]) * float(b[1]))

    for a in asks:
        total_asks = total_asks + (float(a[0]) * float(a[1]))

    print(total_bids - total_asks)


def get_depth():
    PARAMS = {"symbol": "BTCUSDT", "limit": 1000}
    response = requests.get(url=f"{BINANCE_URL}{DEPTH_PATH}", params=PARAMS)
    data = response.json()
    return data


if __name__ == "__main__":
    main()
