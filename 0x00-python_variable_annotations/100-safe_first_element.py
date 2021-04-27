#!/usr/bin/env python3

"""
Duck typing - first element of a sequence
Augment the following code with the correct duck-typed annotations:
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Duck typing - first element of a sequence
    Augment the following code with the correct duck-typed annotations:
    """
    if lst:
        return lst[0]
    else:
        return None
