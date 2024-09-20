from typing import List


def contains_any(tags: List[List[str]], name: str, values: List[str]) -> bool:
    for t in tags:
        if len(t) < 2:
            continue

        if "#" + t[0] != name:
            continue

        if values.__contains__(t[1]):
            return True

    return False
