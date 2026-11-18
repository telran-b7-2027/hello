from typing import Callable

def merge_in_place[T](items: list[T], start: int, len1: int, size: int, key: Callable[[T], T]|None=None)->None:
    left = start
    right = start + len1
    end = start + size

    while left < right < end:
        left_item = items[left]
        right_item = items[right]
        left_value = key(left_item) if key is not None else left_item
        right_value = key(right_item) if key is not None else right_item

        if right_value < left_value:
            for i in range(right, left, -1):
                items[i] = items[i - 1]
            items[left] = right_item
            right += 1

        left += 1





