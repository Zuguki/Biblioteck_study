import time
import concurrent.futures
from Thread.threading_practice1 import get_numbers_which_share_to


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(get_numbers_which_share_to, 3, 250),
                   executor.submit(get_numbers_which_share_to, 5, 250)]

        while futures[0].running() or futures[1].running():
            time.sleep(0.2)
            print('*', end='')
        else:
            print()

        for result in futures:
            print(result.result())
