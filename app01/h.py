import time

import requests

num = 0
while True:
    url = 'https://www.haedal.xyz/api/v1/farming/pools'
    r = requests.get(url)
    if requests.get(url).status_code == 200:
        time.sleep(1)
        num = num + 1
        print(f"成功:{num}")
    else:
        print(f"失败:{num}")

