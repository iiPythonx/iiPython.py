# Copyright 2021 iiPython

# Modules
from typing import Iterable
from datetime import datetime

# Functions
def avg(v: Iterable) -> float:
    return float(sum(v) / len(v))

def itergen(v: Iterable) -> list:
    return [i for i in v]

def parseBool(v: str) -> bool:
    return True if v.lower() in ["true", "1", "yes"] else False

def normalize(*args) -> list:
    _normd = []
    for arg in args:
        if type(arg) in [tuple, list]:
            _normd += itergen(arg)

        else:
            _normd.append(arg)

    return _normd

def now() -> str:
    dt = datetime.now()
    return dt.strftime("%a. %B %-d{}, %Y".format("th" if 11 <= dt.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(dt.day % 10, "th")))

def xrange(mn: int, mx: int = None) -> list:
    return list(range(0 if mx is None else mn, mn + 1 if mx is None else mx + 1))
