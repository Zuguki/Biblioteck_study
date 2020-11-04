"""
from typing import Literal, Final, Dict, Any, TypedDict


def open_file(path, mode: Literal['r', 'w']):
    pass


open_file('fsf', 'b')

PI: Final = 3.14
PI = 2.5

person: Dict[str, str] = {'name': 'Kim', 'l_name': 'Jorgeng', 'age': '12'}
person: Dict[str, Any] = {'name': 'Kim', 'l_name': 'Jorgeng', 'age': 12}
person['l_name'] = 100


class Person(TypedDict):
    name: str
    l_name: str
    age: int


person: Person = {'name': 'Kim', 'l_name': 'Jhorgen', 'age': 12}
person['l_name'] = 19
"""

"""
from typing import overload, Literal, Union, TypedDict, Final


@overload
def parse_roman(val1: str, val2: str, convert: Literal[True]) -> int: ...


@overload
def parse_roman(val1: str, val2: str, convert: Literal[False]) -> str: ...


def parse_roman(val1: str, val2: str, convert: bool) -> Union[str, int]:
    if convert:
        return 3
    else:
        return val1 + val2


res1 = parse_roman('I', 'II', True)
res2 = parse_roman('I', 'II', False)

print(res1 / 10)
print(res2 / 10)

PI: Final = 3.14
PI = 10


class Answer(TypedDict):
    ans1: int
    ans2: str
    

ans: Answer = {'ans1': 1, 'ans2': '2'}
ans['ans2'] = 10
"""
