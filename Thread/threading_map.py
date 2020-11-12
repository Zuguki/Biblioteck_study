from Thread.threading_practice1 import get_numbers_which_share_to
from concurrent.futures import ThreadPoolExecutor


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = executor.map(get_numbers_which_share_to, (20, 24), (100, 100))

        for result in results:
            print(result)
