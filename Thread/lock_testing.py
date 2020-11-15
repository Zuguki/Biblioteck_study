import time
from concurrent.futures import ThreadPoolExecutor
import threading


class Market:
    def __init__(self):
        self.goods = {'Дыня': 100}
        self.lock_obj = threading.Lock()

    def update(self, product_name, discount):
        with self.lock_obj:
            if product_name in self.goods:
                result = self.goods[product_name] * (1 - discount)
                time.sleep(4)
                self.goods[product_name] = result
            else:
                raise ValueError()


if __name__ == '__main__':
    my_market = Market()
    with ThreadPoolExecutor(max_workers=3) as ex:
        ex.submit(my_market.update, 'Дыня', 0.1)
        ex.submit(my_market.update, 'Дыня', 0.2)
        ex.submit(my_market.update, 'Дыня', 0.3)

    print(my_market.goods)
