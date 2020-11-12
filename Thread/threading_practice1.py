import time
from threading import Thread
from typing import Any, List


def get_array_to(numbers_value: int) -> List:
    """Return the array with values from 0 to numbers_value"""

    return [x for x in range(numbers_value)]


def get_numbers_which_share_to(divider: int, numbers_value: Any) -> List:
    """Print the array with numbers with share to number from numbers_range"""

    answer = []
    if isinstance(numbers_value, int):
        range_numbers = get_array_to(numbers_value)
    elif isinstance(numbers_value, list):
        range_numbers = numbers_value
    else:
        raise ValueError('Not corrected type')

    for number in range_numbers:
        time.sleep(0.02)
        if number % divider == 0:
            answer.append(number)

    return answer


if __name__ == '__main__':
    t1 = Thread(target=get_numbers_which_share_to, args=([3, 123]))
    t1.start()

    name = input('\nWrite the name: ')
    print('Hello {}'.format(name))
