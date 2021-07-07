# Copyright 2021 iiPython

# Modules
import json
from iipython import ReadOnly

# Better dictionary class
class BetterDict(object):
    def __init__(self, input_dict: dict = {}, ignore_keyerror: bool = False) -> None:

        # Lock states
        self.UNLOCKED = 0
        self.READONLY = 1

        # Main data
        self._orig = input_dict
        self._dict = self._orig.copy()
        self._lockstate = self.UNLOCKED

        # Extra options
        self._ignore_keyerr = ignore_keyerror
        for _ in dir(self._dict):
            if not str(_).startswith("__"):
                self.__setattr__(_, self._dict.__getattribute__(_))

    def __repr__(self, indent: int = 4) -> str:
        return f"<BetterDict values={json.dumps(self._dict, indent = indent)} lock={self._lockstate}>"

    def __getitem__(self, key: any) -> any:
        if key in self._dict:
            return self._dict[key]

        elif self._ignore_keyerr:
            return None

        raise KeyError(key)

    def __setitem__(self, key: any, value: any) -> None:
        if self._lockstate == 1:
            raise ReadOnly("this dictionary is readonly")

        self._dict[key] = value

    def set_lock(self, lock: int = 0) -> None:
        self._lockstate = lock

    def getKeysByValue(self, value: any, continue_iter: bool = True) -> any:
        keys = []
        for kp in self.items():
            if kp[1] == value:
                keys.append(kp[0])
                if not continue_iter:
                    break

        return keys

    def getFirstKeyByValue(self, value: any) -> any:
        keys = self.getKeysByValue(value, continue_iter = False)
        return keys[0] if keys else None
