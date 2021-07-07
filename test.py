from iipython import BetterDict
d = BetterDict({"value": "hello"}, ignore_keyerror = True)
d["b"] = "c"
d["c"] = "c"

print(d.getFirstKeyByValue("c"))
